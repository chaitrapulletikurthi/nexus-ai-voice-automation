# Voice Agent Design — Portfolio Overview

This document describes the **design responsibilities and rationale** for a real-estate buyer-support voice assistant built with Vapi. It deliberately excludes production prompts, tool definitions, API parameters, webhooks, authentication, customer data, and deployment settings.

## What I designed and why

| Area | Design decision | Business rationale |
| --- | --- | --- |
| Role and boundaries | Clear buyer-support scope and consistent, approachable voice | Keep interactions predictable and useful |
| Buyer intake | Guided, one-question-at-a-time collection and confirmation | Improve contact accuracy and reduce incomplete CRM records |
| Property discovery | Ask for a target city, provide a concise single-property summary where available | Make spoken results understandable without overwhelming callers |
| Interest-based follow-up | Offer property information via email when requested | Create a useful next step rather than unsolicited outreach |
| Human escalation | Recognize requests to speak with a person | Preserve a clear path to the team |
| Buyer education | Explain common wholesaling and financing concepts at a high level, with explicit limitations | Help first-time buyers understand terms without giving financial or legal advice |
| Conversational quality | Concise responses, careful confirmation, natural pauses, and respectful call closure | Improve clarity and phone-call usability |

## Conceptual architecture

1. A caller speaks with a voice assistant hosted on Vapi.
2. Speech recognition converts spoken input into text; the language model interprets the request using conversation guidance.
3. When a supported business action is needed, the assistant requests backend automation through n8n.
4. n8n coordinates CRM records, deal lookup, email follow-up, or call-event logging.
5. Vapi presents a spoken response and handles call lifecycle actions.

The voice stack was described during the project as using Deepgram for transcription and a GPT-family language model. Exact live model/voice selections are not published or independently verified here.

## Scope of the artifact

This is a **high-level design account**, not an export of the Vapi assistant or proof that every prompted behavior was successfully enforced. The `workflows/` directory contains sanitized, adapted n8n workflow examples; those examples are not configured for production execution.

No live caller data, call summaries, prompts, Vapi tool schemas, phone numbers, or confidential service configuration are included.
