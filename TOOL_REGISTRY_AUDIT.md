# Tool Registry Audit — 2.43.19

## Changes

- Removed the duplicate `workspace` entry from `homeTools`.
- Removed the duplicate `plugincenter` entry from `homeTools`.
- Kept `wifi` in the NETWORK category; the category already contains 15 IDs.
- Kept Studio/Tool cross-entry points intentionally: they are navigation aliases, not duplicate implementations.
- Made the registry indexes defensive with `associateBy` / `distinctBy` so an accidental repeated ID cannot create duplicate search/customization rows.

## Intentional cross-entry points

- `Image Studio` can be opened from MEDIA & COLOR and Studio.
- `Workspace Center` can be opened from LAINNYA and Studio Center.
- Editor/JSON/Color aliases are retained because they route into shared implementations and are not duplicate home registry entries.
