import os
from typing import AsyncGenerator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.callbacks import AsyncCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from app.tools import tavily_search, scrape_webpage

# Define the tools
tools = [tavily_search, scrape_webpage]

class PipelineCallbackHandler(AsyncCallbackHandler):
    """Callback handler to track and yield execution events in real time."""
    def __init__(self, event_queue):
        self.event_queue = event_queue

    async def on_chain_start(self, serialized, inputs, **kwargs):
        name = serialized.get("name", "Chain") if serialized else "Chain"
        await self.event_queue.put(f"[System] Starting {name}...")

    async def on_agent_action(self, action, **kwargs):
        tool_name = action.tool
        tool_input = action.tool_input
        await self.event_queue.put(f"[Researcher-A] Decision: Calling tool '{tool_name}' with input: {tool_input}")

    async def on_tool_start(self, serialized, input_str, **kwargs):
        name = serialized.get("name", "Tool") if serialized else "Tool"
        await self.event_queue.put(f"[Tool: {name}] Beginning execution...")

    async def on_tool_end(self, output, **kwargs):
        # Snippet of output
        summary = str(output)[:200] + "..." if len(str(output)) > 200 else str(output)
        await self.event_queue.put(f"[Tool Output] Completed. Result: {summary}")

    async def on_llm_start(self, serialized, prompts, **kwargs):
        await self.event_queue.put(f"[LLM] Generating reasoning path...")

def get_multi_agent_pipeline(event_queue):
    """Returns the multiagent LCEL pipeline configured with the real-time event callback handler."""
    
    # Check for API keys and initialize fallback model
    openai_key = os.getenv("OPENAI_API_KEY")
    google_key = os.getenv("GOOGLE_API_KEY")

    if google_key and not google_key.startswith("your_"):
        from langchain_google_genai import ChatGoogleGenerativeAI
        # Set environment variable so underlying libraries can find it if needed
        os.environ["GOOGLE_API_KEY"] = google_key
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2, google_api_key=google_key)
    elif openai_key and not openai_key.startswith("your_"):
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, openai_api_key=openai_key)
    else:
        raise ValueError("No valid API key configured. Please set GOOGLE_API_KEY or OPENAI_API_KEY.")
    
    # 1. Researcher Agent Prompt and Tool Binder
    researcher_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are Researcher-A, a semantic discovery and web research agent. Your goal is to gather detailed, factual information on the user's topic. Use the search tool to find relevant articles, and then use the scrape_webpage tool to retrieve more depth on key pages if needed. Summarize your raw research findings thoroughly with all details, URLs, and figures."),
        ("human", "Perform deep research on: {input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    researcher_agent = create_tool_calling_agent(llm, tools, researcher_prompt)
    
    # Define AgentExecutor (which is a Runnable)
    researcher_executor = AgentExecutor(
        agent=researcher_agent, 
        tools=tools, 
        verbose=True
    )
    
    # 2. Synthesizer Agent Prompt & Runnable
    synthesizer_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are Validator-X, a reasoning and synthesis engine. You receive raw research findings gathered by Researcher-A. Your job is to analyze the research, verify facts, resolve discrepancies, and write a comprehensive, professional, and beautifully structured markdown report. Use clear sections, tables, and lists. Do not call any tools, just synthesize the provided research findings into a premium executive briefing."),
        ("human", "Analyze and synthesize these research findings and compile the final report:\n\n{research_findings}"),
    ])
    
    synthesizer_runnable = synthesizer_prompt | llm | StrOutputParser()
    
    # 3. Create the Combined LCEL Multi-Agent Pipeline
    # Using Runnables: We pipe researcher output dict key "output" into synthesizer
    pipeline = (
        {
            "research_findings": researcher_executor | (lambda x: x["output"])
        }
        | synthesizer_runnable
    )
    
    return pipeline
