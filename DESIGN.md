---
name: Midnight Enterprise
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#5de6ff'
  on-secondary: '#00363e'
  secondary-container: '#00cbe6'
  on-secondary-container: '#00515d'
  tertiary: '#ffafd3'
  on-tertiary: '#620040'
  tertiary-container: '#e364a7'
  on-tertiary-container: '#560038'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#a2eeff'
  secondary-fixed-dim: '#2fd9f4'
  on-secondary-fixed: '#001f25'
  on-secondary-fixed-variant: '#004e5a'
  tertiary-fixed: '#ffd8e7'
  tertiary-fixed-dim: '#ffafd3'
  on-tertiary-fixed: '#3d0026'
  on-tertiary-fixed-variant: '#85145a'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: '0'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  label-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  mono-sm:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base-unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

This design system embodies the "Midnight Enterprise" aesthetic: a high-performance environment for orchestrating multi-agent AI systems. The brand personality is authoritative, precise, and cutting-edge, designed for developers and enterprise operators who require a "mission control" experience.

The visual style is a fusion of **Modern Minimalism** and **Refined Glassmorphism**. It utilizes deep obsidian surfaces to reduce cognitive load during long sessions, punctuated by vibrant, luminous accents that signal AI activity and system health. The emotional response is one of absolute control within a sophisticated, futuristic digital landscape.

## Colors

The palette is anchored in deep space. The primary background is a near-black obsidian (`#020617`), providing maximum contrast for the technical interface elements.

- **Primary (Electric Indigo):** Used for primary actions, active agent states, and critical paths.
- **Secondary (Cyan):** Used for data visualization, secondary status indicators, and subtle highlights.
- **Tertiary (Rose):** Reserved for specialized agent functions or high-priority alerts.
- **Neutral:** A range of deep charcoals and slates used for surfaces, borders, and structural hierarchy.

Color application should favor high-value saturation on top of dark backgrounds to create a "glowing" effect without over-illuminating the workspace.

## Typography

The design system utilizes **Geist** for its exceptional clarity and technical "developer-first" feel. The geometric construction of Geist aligns with the precision of AI operations.

- **Headlines:** Use Bold weights with tight letter-spacing to create a sense of density and power.
- **Body:** Regular weights provide high legibility for logs, agent dialogues, and configuration settings.
- **Monospace:** For code snippets, terminal outputs, and agent logic, Geist Mono is utilized to maintain visual consistency while providing the necessary structural distinction.

## Layout & Spacing

This design system uses a **Fluid Grid** model built on a 4px baseline. The layout is optimized for high-density information display, essential for monitoring multiple concurrent AI agents.

- **Desktop:** 12-column grid with 24px gutters. Use flexible sidebars for agent inventories and status monitors.
- **Tablet:** 8-column grid with 16px gutters. Sidebars collapse into drawers.
- **Mobile:** 4-column grid with 16px margins. Information density is prioritized via vertical stacks and tabbed interfaces.

Spacing should be used to create clear logical groupings. Large `xl` gaps are used to separate major system modules, while `sm` and `xs` gaps are used for internal component properties.

## Elevation & Depth

Visual hierarchy is achieved through **Tonal Layering** and **Glassmorphism**, rather than traditional shadows.

1. **Floor:** The deepest obsidian (`#020617`).
2. **Surface:** Slightly lifted charcoal (`#0F172A`) with a subtle 1px border (`#1E293B`).
3. **Elevated (Active Agent):** Uses a translucent glass effect with a `12px` backdrop-blur and a faint outer glow matching the agent's accent color (e.g., 10% opacity Indigo).

Borders are critical. All elevated elements should feature a thin, low-contrast top highlight border to simulate a light source from above, typical of high-end hardware interfaces.

## Shapes

The shape language is "Technical-Soft." A consistent `0.25rem` (4px) corner radius is applied to most UI components to maintain a professional, structured feel. 

- **Cards & Containers:** Use `rounded-lg` (8px) to provide enough distinction from the base grid.
- **Inputs & Buttons:** Use the standard `0.25rem` for a precise, "button-like" click area.
- **Tags/Status Pills:** Can use `rounded-xl` for a distinct "pill" shape to separate metadata from functional controls.

## Components

- **Buttons:** Primary buttons are solid Indigo with a very subtle inner glow. Secondary buttons use a "Ghost" style with thin 1px borders.
- **AI Agent Cards:** These are the centerpiece. They feature a `10%` glass background, a subtle primary-colored glow when "Active," and a Geist Mono header for the agent ID.
- **Input Fields:** Darker than the surface background with a focused state that illuminates the entire border in Cyan.
- **Chips/Status Indicators:** Small, high-contrast badges. Use a pulsing animation (soft glow) for "Processing" states.
- **Data Terminal:** A dedicated list component using Geist Mono, featuring syntax highlighting for agent logs and JSON outputs.
- **Agent Nodes:** Circular or squircle icons with a halo effect to represent the "consciousness" of the AI agent within the workflow.