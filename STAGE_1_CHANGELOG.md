# GITLS 2.43.12 — Tool Performance Pass

## Shared
- `ToolPerformance.kt`: limits + bounded shared executor for all `toolThread` work
- `toolThread` no longer spawns unlimited raw threads; uses pool (core size = CPU 2–4)

## File tools
- File Manager lists max **250** entries (message when truncated; use filter)
- Recursive file collect capped at **8000** files (`walkFilesCapped`)
- Duplicate UI groups capped via `DUPLICATE_GROUP_CAP`
- Search result takes use `SEARCH_RESULT_CAP` (200)

## Network
- Port scan pool **6** threads (was 8)
- Probe timeout **220ms**
- Result text capped at 500 lines displayed

## Goal
Lower peak threads, RAM from huge folders, and UI jank when listing/scanning.
## Tool Registry Cleanup — 2.43.19
- Removed duplicate `workspace` and `plugincenter` entries from the home tool registry.
- Added defensive unique-ID indexing for search and Tool Customization.
- Confirmed NETWORK retains all 15 registered tools, including `wifi`.

