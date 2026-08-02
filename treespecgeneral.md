TREE SPEC — GENERAL
World Simulator Project

│
├── IDENTITY
│
│   ├── Name
│   │   └── World Simulator
│   │
│   ├── Type
│   │   └── Global Project Specification
│   │
│   ├── Purpose
│   │   └── Define the complete architecture of the project.
│   │
│   ├── Mission
│   │   └── Build one unified specification that every repository,
│   │       team and source code implementation follows.
│   │
│   ├── Final Output
│   │   └── Complete Project TreeSpec
│   │
│   └── Stop Condition
│       └── Every repository has an approved TreeSpec.
│
├── ONE SENTENCE
│
│   └── TreeSpec General exists only to describe the whole project.
│
├── BOUNDARY
│
│   ├── Starts With
│   │
│   │   ├── Project Goal
│   │   ├── Project Scope
│   │   ├── Global Philosophy
│   │   └── System Requirements
│   │
│   ├── Ends With
│   │
│   │   └── Repository Specifications
│   │
│   └── Never Contains
│
│       ├── Repository implementation
│       ├── Source code
│       ├── Runtime data
│       ├── JSONData
│       └── Business logic
│
├── WORKING MODEL
│
│   ├── Participants
│   │
│   │   ├── Human
│   │   └── Chatbot
│   │
│   ├── Human
│   │
│   │   ├── Define vision
│   │   ├── Approve specification
│   │   └── Own final decision
│   │
│   ├── Chatbot
│   │
│   │   ├── Analyze
│   │   ├── Structure
│   │   ├── Improve
│   │   ├── Validate
│   │   └── Generate specification
│   │
│   └── Principle
│
│       └── Human decides.
│           Chatbot structures.
│
├── RESPONSIBILITY
│
│   ├── Define project identity.
│   ├── Define project scope.
│   ├── Define project architecture.
│   ├── Define repository boundaries.
│   ├── Define project workflow.
│   ├── Define project contracts.
│   ├── Define dependency rules.
│   ├── Define quality rules.
│   ├── Define version rules.
│   └── Define expansion rules.
│
├── NON GOALS
│
│   ├── NOT describe repository internals.
│   ├── NOT describe phase implementation.
│   ├── NOT describe source code.
│   ├── NOT store project data.
│   ├── NOT execute workflows.
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
