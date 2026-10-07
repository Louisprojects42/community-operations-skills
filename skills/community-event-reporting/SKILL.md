---
name: community-event-reporting
description: "Turn community or gaming event notes into an internal after-action report and a separately sanitized public recap. Use for event write-ups and publication previews."
---

# Community Event Reporting

Establish the intended audience and use the supplied event evidence: objective, what happened, observed outcomes, and open follow-up work. If the user requests only a public recap, do not manufacture an internal report first. Keep unknown details absent or explicitly unknown rather than adding plausible attendance, timing, or results.

For an internal after-action report, distinguish chronology, outcomes, observations, causes supported by evidence, and proposed actions with owners only when known. Avoid assigning blame from incomplete notes. Include operational details only for the intended internal audience.

For a public recap, write a separate field or artifact. Explain the activity to a newcomer, describe a supported moment or outcome, and give useful context without exposing participant identities, private feedback, payout breakdowns, access details, or sensitive tactics unless the user explicitly chooses their release. Preserve permitted aggregate outcomes and uncertainty.

A missing public text must not automatically expose the internal report. In an implementation, use explicit publication state and a public-safe allowlist/serializer; verify unpublished records and private fields are absent from the public response. Clearing or unpublishing the recap should remove public access, including relevant cached output under the application's existing cache design.

Do not treat image metadata, screenshots, captions, or alt text as automatically safe. Select evidence that supports the recap and has the appropriate sharing permission. Do not invent quotes or use a staged image as proof that the event occurred.

Deliver the requested draft(s), a short list of omitted sensitive categories when useful, and unresolved factual gaps. Creating a draft does not imply sending an announcement or publishing a page. Read [the worked example](references/worked-example.md) for a safe public transformation.
