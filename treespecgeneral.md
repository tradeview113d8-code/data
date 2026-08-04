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
(World History)│   ├── NOT execute workflows.
│   └── NOT replace repository specifications.
│
├── PROJECT ARCHITECTURE
│
│   ├── TreeSpec System
│   │
│   │   ├── TreeSpec General
│   │   ├── TreeSpec Repository
│   │   ├── Repository Phase
│   │   ├── Phase Specification
│   │   ├── Team Specification
│   │   ├── Leader
│   │   ├── Worker
│   │   ├── QA
│   │   └── Loopback
│   │
│   └── TreeData System
│
│       └── Independent data specification system.
│
├── GLOBAL CONTRACT
│
│   ├── RECEIVE
│   │
│   │   ├── Project Goal
│   │   ├── Project Constraints
│   │   ├── Design Philosophy
│   │   └── Repository Requirements
│   │
│   ├── PROCESS
│   │
│   │   ├── Partition project
│   │   ├── Build architecture
│   │   ├── Define repositories
│   │   ├── Define contracts
│   │   ├── Define hierarchy
│   │   ├── Define dependencies
│   │   ├── Validate consistency
│   │   ├── Version
│   │   └── Publish
│   │
│   └── PRODUCE
│
│       ├── TreeSpec Repository
│       ├── Global Rules
│       ├── Global Contracts
│       ├── Global Workflow
│       ├── Dependency Graph
│       └── Project Architecture
│
├── CORE PHILOSOPHY
│
│   ├── Contract First
│   ├── Tree First
│   ├── Single Responsibility
│   ├── Context Isolation
│   ├── Progressive Specification
│   ├── Human Validation
│   ├── Version Controlled
│   ├── Reusability First
│   ├── Explicit Dependencies
│   └── Scalable Hierarchy
│
├── EXECUTION MODEL
│
│   ├── Every node has exactly one responsibility.
│
│   ├── Every node answers only three questions.
│
│   │
│   │   Receive
│   │
│   │   Process
│   │
│   │   Produce
│   │
│   ├── Every node owns one contract.
│
│   ├── Every node communicates only through contracts.
│
│   ├── Every implementation must follow its contract.
│
│   └── Every contract must be representable in source code.
│
├── HIERARCHY
│
│   TreeSpec General
│
│       ↓
│
│   TreeSpec Repository
│
│       ↓
│
│   Repository Phase
│
│       ↓
│
│   Phase Specification
│
│       ↓
│
│   Team Specification
│
│       ↓
│
│   Leader
│
│       ↓
│
│   Worker
│
│       ↓
│
│   QA
│
│       ↓
│
│   Loopback
│
├── QUALITY
│
│   ├── Traceable
│   ├── Deterministic
│   ├── Reviewable
│   ├── Expandable
│   ├── Reusable
│   ├── Contract Driven
│   ├── Hierarchy Safe
│   └── Versioned
│
├── GENERAL RULES
│
│   ├── One tree, one responsibility.
│   ├── One node, one responsibility.
│   ├── Parent defines context.
│   ├── Child specializes context.
│   ├── Siblings never overlap.
│   ├── Dependencies are explicit.
│   ├── Communication only through contracts.
│   ├── Context flows downward.
│   ├── Validation flows upward.
│   ├── Loopback returns to the previous valid state.
│   └── Every specification must remain implementation-independent.
│
├── HANDOFF
│
│   Project
│
│      ↓
│
│   TreeSpec General
│
│      ↓
│
│   TreeSpec Repository
│
│      ↓
│
│   Repository Phase
│
│      ↓
│
│   Phase Specification
│
│      ↓
│
│   Team Specification
│
│      ↓
│
│   Source Code
│
└── CHILDREN
    │
    ├── TreeSpec Repository
    ├── Repository Phase
    ├── Phase Specification
    ├── Team Specification
    ├── Leader
    ├── Worker
    ├── QA
    └── Loopback
