TREE SPEC REPOSITORY

────────────────────────────────────────

IDENTITY

Name

    Repository 2

Alias

    Dynamic Data Repository

Type

    Dynamic Data Builder

Purpose

    Build all dynamic data required by the World Simulator.

Mission

    Continuously collect and generate dynamic data while
    preserving World DNA.

Final Output

    Actor Pool

    Weather Library

    News Library

Stop Condition

    Dynamic libraries successfully published.

────────────────────────────────────────

ONE SENTENCE

Repository 2 exists only to build dynamic data.

────────────────────────────────────────

BOUNDARY

Receive

    World DNA

    External News Sources

    External Weather Sources

Process

    Generate

    Collect

    Normalize

    Store

Publish

Produce

    Actor Pool

    Weather 24h

    Vietnam News 24h

    World News 24h

Never Produce

    Story

    Script

    Runtime Translation

    Episode

    Image Prompt

    Audio Prompt

────────────────────────────────────────

RESPONSIBILITY

Generate Actors

Collect Weather

Collect News

Normalize Dynamic Data

Publish Dynamic Libraries

────────────────────────────────────────

DATA FLOW

Repository 1

↓

World DNA

↓

Repository 2

↓

Actor Pool

Weather

News

↓

Repository 3

────────────────────────────────────────

DATA CONTRACT

Receive

World DNA

Purpose

Generate actors.

Status

Read Only

────────────────────────

Receive

Weather Sources

Purpose

Collect weather.

Status

Dynamic

────────────────────────

Receive

News Sources

Purpose

Collect news.

Status

Dynamic

────────────────────────

Produce

Actor Pool

Purpose

Reusable actor library.

────────────────────────

Produce

Weather Library

Purpose

Weather for current 24 hours.

────────────────────────

Produce

News Library

Purpose

Collected news.

────────────────────────────────────────

WORKERS

WORKER A

Actor Builder

Receive

World DNA

Process

Generate actors.

Generate personalities.

Generate identities.

Assign IDs.

Store.

Produce

Actor Pool

────────────────────────

WORKER B

Weather Collector

Receive

Weather Sources

Process

Collect.

Normalize.

Timestamp.

Store.

Produce

Weather 24h

────────────────────────

WORKER C

Vietnam News Collector

Receive

Vietnam News Sources

Process

Collect.

Attach metadata.

Store.

Produce

Vietnam News 24h

────────────────────────

WORKER D

Global News Collector

Receive

Global News Sources

Process

Collect.

Attach metadata.

Store.

Produce

World News 24h

────────────────────────

WORKER E

Publisher

Receive

Actor Pool

Weather

News

Process

Version.

Serialize.

Publish.

Produce

MongoDB 2

────────────────────────────────────────

QUALITY

Complete

Fresh

Traceable

Version Controlled

Reusable

Repository Independent

────────────────────────────────────────

GLOBAL CONTRACT

Receive

World DNA

Weather Sources

News Sources

Process

Generate.

Collect.

Normalize.

Publish.

Produce

Actor Pool

Weather Library

News Library

────────────────────────────────────────

GENERAL RULES

Repository 2 never edits World DNA.

Repository 2 never translates news.

Repository 2 never interprets news.

Repository 2 never generates stories.

Repository 2 never uses LLM.

Repository 2 only generates dynamic data.

All generated actors originate from World DNA.

All collected news must preserve the original title.

All weather data must preserve source values.

────────────────────────────────────────

GUARANTEE

Dynamic data always available.

News always remains original.

Actors always match World DNA.

Weather always represents current conditions.

Repository 3 receives complete dynamic libraries.

────────────────────────────────────────

CHILDREN

Phase 1

Actor Builder

Phase 2

Weather Collector

Phase 3

Vietnam News Collector

Phase 4

Global News Collector

Phase 5

Publisher
