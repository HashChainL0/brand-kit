<div align="center">

<img src="logo/logo-192.png" alt="Hash Chain logo" width="128" height="128">

# Hash Chain Brand Kit

Logo, colors and typography for referencing Hash Chain.

</div>

Hash Chain is the privacy Layer 0, currently pre-launch: its own network where accounts, payments, swaps, assets and apps are private by default. Website: https://hashchain.network. This kit is for press, integrators, community members and anyone who needs to show the Hash Chain name or logo correctly. The protocol itself is described in the [protocol spec](https://github.com/HashChainL0/protocol-spec).

## Logo

The mark is a white, stylized "#" on a dark rounded square. The dark square is part of the logo. Always use the logo with its square.

| Preview | File | Use |
| --- | --- | --- |
| <img src="logo/logo-32.png" width="32" alt="32px"> | `logo/logo-32.png` | Small icon, tab, list item |
| <img src="logo/logo-64.png" width="64" alt="64px"> | `logo/logo-64.png` | Small avatar |
| <img src="logo/logo-180.png" width="90" alt="180px"> | `logo/logo-180.png` | Touch icon |
| <img src="logo/logo-192.png" width="96" alt="192px"> | `logo/logo-192.png` | App icon, profile image |
| <img src="logo/logo-256.webp" width="128" alt="256px"> | `logo/logo-256.webp` | Web, lightweight |
| <img src="logo/logo-512.png" width="128" alt="512px"> | `logo/logo-512.png` | Large icon |
| <img src="logo/logo-1254.png" width="128" alt="original"> | `logo/logo-1254.png` | Original master, print and large formats |
| | `logo/favicon.ico` | Browser favicon |

## Usage

### Do

- Keep clear space around the logo equal to at least one quarter of its width on every side.
- Keep the minimum size at 24px wide on screen.
- Scale it proportionally.
- Place it on plain light or dark backgrounds.
- Use the original files from this kit.

Pixel values for clear space and a guide to picking a file by size are in [docs/LOGO-SIZES.md](docs/LOGO-SIZES.md).

### Do not

- Do not recolor the mark or the square.
- Do not stretch, squash, rotate or skew it.
- Do not add shadows, outlines, glows or effects.
- Do not remove the dark square and place the bare "#" on a busy background. On photos, gradients or patterns, the dark square must stay.
- Do not crop it or place other marks inside the clear space.
- Do not use it in a way that suggests endorsement, partnership or affiliation that does not exist.

## Colors

| Name | Hex | Usage |
| --- | --- | --- |
| Logo dark | `#2c2c2d` | Logo square, dark panels |
| Accent | `#ff6a13` | Highlights, links on dark, large display accents |
| Accent, text on light | `#c2410c` | Accent text and links on light backgrounds (passes contrast) |
| Ink | `#11131a` | Primary text on light, page background on dark |
| Surface | `#f4f5f7` | Light page and card background |

Machine-readable tokens are in [`colors.json`](colors.json) and [`tokens.css`](tokens.css). Contrast ratios and which colors to pair for text are in [docs/COLOR-PAIRINGS.md](docs/COLOR-PAIRINGS.md).

## Typography

| Role | Font | Notes |
| --- | --- | --- |
| Display and body | Bricolage Grotesque | Headlines, body copy, buttons |
| Labels | JetBrains Mono | Small uppercase labels, code, numbers in tables |

Both fonts are open source and available from common font libraries. Use a system sans-serif as the fallback.

Casing, fallbacks and do and do not rules for type are in [docs/TYPOGRAPHY.md](docs/TYPOGRAPHY.md).

## Design tokens

[`colors.json`](colors.json) holds the palette, fonts and logo rules as JSON. [`tokens.css`](tokens.css) holds the same values as CSS custom properties, prefixed `--hc-`. Keep the two files in sync. Run `python3 scripts/check-tokens.py` after editing either one. It lists any value that differs.

| Token | Value |
| --- | --- |
| `--hc-logo-dark` | `#2c2c2d` |
| `--hc-accent` | `#ff6a13` |
| `--hc-accent-on-light` | `#c2410c` |
| `--hc-ink` | `#11131a` |
| `--hc-surface` | `#f4f5f7` |
| `--hc-font-display` | Bricolage Grotesque, then Inter, system-ui, sans-serif |
| `--hc-font-mono` | JetBrains Mono, then ui-monospace, monospace |
| `--hc-logo-min-width` | `24px` |

```css
@import url("tokens.css");

body {
  background: var(--hc-surface);
  color: var(--hc-ink);
  font-family: var(--hc-font-display);
}

a {
  color: var(--hc-accent-on-light); /* on dark backgrounds use --hc-accent */
}

.label {
  font-family: var(--hc-font-mono);
  text-transform: uppercase;
}
```

The fonts are not bundled in the kit. Load them from a font library, or the fallbacks apply.

## Descriptions

Approved one-line, one-sentence and paragraph descriptions, plus the status line to use with them, are in [docs/BOILERPLATE.md](docs/BOILERPLATE.md).

## Name

- Write **Hash Chain**: two words, capital H and C.
- Do not write HashChain, Hashchain, hash chain or Hash-Chain in running text.
- **HASH CHAIN** in all capitals is allowed in monospace labels only.
- The X handle and GitHub organization are written `hashchainL0` and `HashChainL0`, exactly as registered.

## Files

```
brand-kit/
  README.md
  LICENSE.md
  colors.json
  tokens.css
  scripts/
    check-tokens.py
  docs/
    BOILERPLATE.md
    COLOR-PAIRINGS.md
    LOGO-SIZES.md
    TYPOGRAPHY.md
  logo/
    logo-32.png
    logo-64.png
    logo-180.png
    logo-192.png
    logo-256.webp
    logo-512.png
    logo-1254.png
    favicon.ico
```

## License

See [LICENSE.md](LICENSE.md). In short: the logo and name are trademarks of the project. You may use them to refer to Hash Chain. You may not use them to imply endorsement.
