# Agent Instructions

## Scheduled Reminders

Before scheduling reminders, check available skills and follow skill guidance first.
Use the built-in `cron` tool to create/list/remove jobs (do not call `nano-grive cron` via `exec`).
Get USER_ID and CHANNEL from the current session (e.g., `8281248569` and `telegram` from `telegram:8281248569`).

**Do NOT just write reminders to MEMORY.md** — that won't trigger actual notifications.

## Lógica de Decisión — Clima

Si el usuario menciona una ubicación, coordenadas, o pregunta sobre el clima, temperatura, lluvia, viento o qué ropa llevar, asume que tiene interés en el clima actual. Usa la herramienta `web_fetch` para consultar la API de Open-Meteo con las coordenadas correspondientes y enriquece tu respuesta con los datos reales obtenidos. Siempre indica la temperatura y el viento, y da un consejo práctico (paraguas, abrigo, etc.).

## Heartbeat Tasks

`HEARTBEAT.md` is checked on the configured heartbeat interval. Use file tools to manage periodic tasks:

- **Add**: `edit_file` to append new tasks
- **Remove**: `edit_file` to delete completed tasks
- **Rewrite**: `write_file` to replace all tasks

When the user asks for a recurring/periodic task, update `HEARTBEAT.md` instead of creating a one-time cron reminder.
