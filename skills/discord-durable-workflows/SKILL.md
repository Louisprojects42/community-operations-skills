---
name: discord-durable-workflows
description: "Build or repair Discord attendance, points, and background workflows that must survive restarts and duplicate events. Use for persistent bot state and cross-service side effects."
---

# Durable Discord Workflows

Identify the workflow's authoritative store and state transitions. Keep Discord display state separate from business state; a message, in-memory collector, or process cache alone cannot prove that an award was applied. Use the existing database and deployment pattern unless a change is needed for the requested behavior.

Define command/event identity and make consequential transitions idempotent. For attendance, represent join/leave intervals and event start/stop boundaries explicitly. Count interval overlap with the active event and the tracked channel set. Track channel moves as transitions; prevent overlap from double counting. Define what happens when an event ends while members remain connected.

Persist the state necessary to resume after a restart. Missing gateway events during downtime are unknown attendance; do not silently credit the entire gap. Reconcile current presence against the chosen recovery policy and keep estimates distinguishable from observed intervals. Handle repeated start/stop, duplicate gateway events, and events arriving out of order.

For points or rewards, enforce a unique operation key such as `(event_id, member_id, award_type)` in durable storage. A retry must return the previous result. If one service commits and another times out, use a durable outbox or reconciliation job; do not promise atomicity across unrelated databases. An announcement failure must not cause a second award.

Recheck authorization for each privileged command and component interaction. Use server-side member/role evidence with an explicit cache freshness policy. Defer long operations according to the installed Discord library's interaction contract; handle rate limits without replaying non-idempotent work blindly.

Verify the requested lifecycle with synthetic events and a restart/retry scenario. Deliver the transition model, focused source changes, migration/recovery behavior, and unresolved timing assumptions. Read [the timeline example](references/worked-example.md) for interval and retry cases.
