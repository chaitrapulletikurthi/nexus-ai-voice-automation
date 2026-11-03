# Publishing checklist

1. Obtain permission to describe employer work and share derivative n8n logic. **Removing passwords does not automatically make company workflows public-domain.**
2. Confirm the original embedded Vapi bearer credential has been revoked/rotated. Treat the original files as sensitive.
3. Review each workflow JSON for business logic, field names and operational information NexKey does not want shared. This package deliberately omits account IDs, real endpoints, customer records and internal names, but approval is still required.
4. Confirm whether the aggregate 100+ calls and approximately 80% no-human-request figure can be published. If not, remove the metrics paragraph.
5. Create a new GitHub repository and upload this folder's contents (not the sensitive original exports).
6. Do not test imports against the company's live n8n environment. Use a separate isolated instance and dummy CRM/SMTP data.

## What is NOT provided

The proprietary Vapi system prompt, Vapi tool parameter schemas, production assistant settings, API keys, real phone numbers, webhook paths, internal base/table IDs, customer-level logs and live deployment credentials.
