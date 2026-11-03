# Technical review notes

This repository is a **sanitized educational adaptation**, not a supported production integration. Static checks validate JSON structure and node connections only.

- **Voice-agent layer:** The agent prompt expresses intended behavior. Exact Vapi assistant configuration and tool schemas are omitted.
- **Property retrieval:** Validate Airtable formula syntax, status filtering, sort field, single-result behavior, and empty-result logic before use. Do not assume the original export enforced every prompt instruction.
- **Buyer intake:** Validate linked-record metro mapping, duplicate handling, merge behavior when no matching buyer exists, and field-type compatibility.
- **Callback flag:** Test phone normalization for international formats, absent records and duplicate matches.
- **Email delivery:** Ensure that acknowledgement occurs only after successful delivery-provider handoff; configure a test SMTP service before testing.
- **Call logging:** Avoid copying transcripts and recording URLs into public fixtures; evaluate privacy and retention separately.
- **Missed-call trigger:** Use a test API key stored in an approved secrets store; prevent accidental outbound calls during development.

The original source exports contained production identifiers and one embedded authorization value. **Rotate/revoke that authorization value** and confirm appropriate access review. This repository cannot revoke credentials itself.
