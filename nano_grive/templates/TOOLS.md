# Tool Usage Notes

Tool signatures are provided automatically via function calling.
This file documents non-obvious constraints and usage patterns.

## exec — Safety Limits

- Commands have a configurable timeout (default 60s)
- Dangerous commands are blocked (rm -rf, format, dd, shutdown, etc.)
- Output is truncated at 10,000 characters
- `restrictToWorkspace` config can limit file access to the workspace

## glob — File Discovery

- Use `glob` to find files by pattern before falling back to shell commands
- Simple patterns like `*.py` match recursively by filename
- Use `entry_type="dirs"` when you need matching directories instead of files
- Use `head_limit` and `offset` to page through large result sets
- Prefer this over `exec` when you only need file paths

## grep — Content Search

- Use `grep` to search file contents inside the workspace
- Default behavior returns only matching file paths (`output_mode="files_with_matches"`)
- Supports optional `glob` filtering plus `context_before` / `context_after`
- Supports `type="py"`, `type="ts"`, `type="md"` and similar shorthand filters
- Use `fixed_strings=true` for literal keywords containing regex characters
- Use `output_mode="files_with_matches"` to get only matching file paths
- Use `output_mode="count"` to size a search before reading full matches
- Use `head_limit` and `offset` to page across results
- Prefer this over `exec` for code and history searches
- Binary or oversized files may be skipped to keep results readable

## cron — Scheduled Reminders

- Please refer to cron skill for usage.

## get_weather — Servicio Meteorológico Externo

- **Endpoint:** https://api.open-meteo.com/v1/forecast
- **Parámetros requeridos:** `latitude` (float), `longitude` (float), `current_weather=true`
- **Ejemplo de llamada:** `https://api.open-meteo.com/v1/forecast?latitude=40.42&longitude=-3.70&current_weather=true`
- **Instrucción:** Cuando el usuario pregunte por el clima, la temperatura, si va a llover, si necesita paraguas, o cualquier consulta meteorológica, realiza una petición GET a este endpoint usando la herramienta `web_fetch`. No necesitas API key.
- **Interpretación:** Del JSON devuelto, extrae `current_weather.temperature` (°C) y `current_weather.windspeed` (km/h) para dar una respuesta útil y contextualizada al usuario.
- **Coordenadas comunes:** Madrid (40.42, -3.70), Barcelona (41.39, 2.15), México DF (19.43, -99.13), Buenos Aires (-34.60, -58.38).
