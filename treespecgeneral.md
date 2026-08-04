WORLD SIMULATOR

GOAL

Build an autonomous fantasy world from real-world data.

═══════════════════════════════════════════════════════

REPOSITORY 1

STATIC WORLD EVOLUTION

Purpose

Build immutable world DNA.

INPUT

Earth
Human Ideas
Chatbot Knowledge

↓

EVOLUTION

Human
Multi Chatbot
Loopback

↓

ARTIFACT FLOW

Earth
    ↓
TreeDataEarth
    ↓
JSONDataEarth
    ↓
TreeData
    ↓
JSONData Schema
    ↓
Source JSONData
    ↓
Complete JSONData
    ↓
Final JSONData
    ↓
World Prefab Library
    ↓
MongoDB1

OUTPUT

MongoDB1

Immutable World Library

═══════════════════════════════════════════════════════

REPOSITORY 2

DYNAMIC WORLD EVOLUTION

Purpose

Transform immutable world into today's living world.

INPUT

MongoDB1

+

Real World

    ├── News
    ├── People
    ├── Weather
    ├── Economy
    ├── Science
    ├── Sports
    ├── Entertainment
    └── Other Sources

↓

EVOLUTION

Python

Search Engine

Rule Library

Grammar Library

World Rules

↓

ARTIFACT FLOW

Real Sources
    ↓
Source Library
    ↓
Tree Library
    ↓
JSON Library
    ↓
Action Library
    ↓
World Reaction
    ↓
Today's World State
    ↓
MongoDB2

OUTPUT

MongoDB2

Today's Living World

═══════════════════════════════════════════════════════

REPOSITORY 3

NARRATIVE EVOLUTION

Purpose

Transform today's living world into stories.

INPUT

MongoDB2

↓

EVOLUTION

Python

Story Library

Rule Library

LLM

↓

ARTIFACT FLOW

Today's World State
    ↓
Episode Candidates
    ↓
Episode Plan
    ↓
Script
    ↓
Image Prompt
    ↓
Narration
    ↓
Music Prompt
    ↓
Episode Package
    ↓
MongoDB3

OUTPUT

MongoDB3

Episode Library

═══════════════════════════════════════════════════════

DATA EVOLUTION

Earth
        │
        ▼
MongoDB1
(Immutable World DNA)

        +

Real World
(News • People • Weather • Economy • ...)

        │
        ▼

MongoDB2
(Today's Living World)

        │
        ▼

MongoDB3
(World History)
