import os
import asyncio
import json
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.agents import get_multi_agent_pipeline, PipelineCallbackHandler

load_dotenv()

app = FastAPI(title="Midnight OS Multi-Agent Research System")

# Enable CORS for development flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    # Serve the main dashboard code.html
    return FileResponse("code.html")

@app.post("/api/research")
async def research(request: Request):
    body = await request.json()
    query = body.get("query")
    if not query:
        return {"error": "Query is required"}

    async def event_generator():
        event_queue = asyncio.Queue()
        callback_handler = PipelineCallbackHandler(event_queue)
        
        try:
            pipeline = get_multi_agent_pipeline(event_queue)
        except ValueError as e:
            yield f"data: {json.dumps({'message': f'[ERROR] {str(e)}'})}\n\n"
            return

        async def run_pipeline():
            try:
                await event_queue.put("[System] Initiating Research Multi-Agent Network...")
                await event_queue.put("[System] Handshake completed with Researcher-A.")
                
                config = {"callbacks": [callback_handler]}
                # Run the pipeline with the input and custom callback
                result = await pipeline.ainvoke({"input": query}, config=config)
                
                await event_queue.put("[System] Synthesis complete. Ready for layout rendering.")
                await event_queue.put(f"[FINAL_RESULT] {result}")
            except Exception as e:
                await event_queue.put(f"[ERROR] Pipeline execution failed: {str(e)}")
            finally:
                await event_queue.put(None)

        # Run pipeline in a background task so we can stream immediately
        asyncio.create_task(run_pipeline())

        while True:
            msg = await event_queue.get()
            if msg is None:
                break
            yield f"data: {json.dumps({'message': msg})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
