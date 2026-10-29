# Typography

This page expands the [Typography](../README.md#typography) table in the README. It adds no new fonts and no fixed sizes.

## Roles

| Role | Font | Use it for | Do not use it for |
| --- | --- | --- | --- |
| Display and body | Bricolage Grotesque | Headlines, body copy, buttons, navigation | Code, hashes, addresses |
| Labels | JetBrains Mono | Small uppercase labels, code, numbers in tables, hashes and addresses | Long paragraphs |

## Fallbacks

The fonts are not bundled in this kit. If they fail to load, the fallback stacks in [`tokens.css`](../tokens.css) apply:

- `--hc-font-display`: Bricolage Grotesque, then Inter, system-ui, sans-serif
- `--hc-font-mono`: JetBrains Mono, then ui-monospace, monospace

Test your layout with the fallbacks on. A page that only looks right with the brand fonts is too fragile.

## Casing

- Headlines and body copy use sentence case, not title case or all capitals.
- Small labels in JetBrains Mono may be uppercase.
- The project name is written **Hash Chain** in running text. See [Name](../README.md#name).

## Color on text

Pair text and background colors using [COLOR-PAIRINGS.md](COLOR-PAIRINGS.md). On light backgrounds, use `--hc-accent-on-light` for accent text and links. `--hc-accent` is for large display accents and for dark backgrounds.

## Do

- Use one display face and one mono face. That is the whole system.
- Keep line length comfortable for reading, and left-align body copy.
- Use the mono face for anything a reader may copy, such as an address, a hash or a command.

## Do not

- Do not add a third font.
- Do not stretch, outline or add shadows to text set in the display face.
- Do not use all capitals for body copy.
