# Color pairings

Which foreground and background combinations from the [palette](../README.md#colors) are readable. Contrast ratios are calculated with the WCAG 2.1 relative luminance formula from the hex values in [`colors.json`](../colors.json) and rounded to two decimals. WCAG asks for at least 4.5:1 for body text, 3:1 for large text (about 24px, or 19px bold) and for interface graphics.

## Approved pairings

| Foreground | Background | Ratio | Use for |
| --- | --- | --- | --- |
| Ink `#11131a` | Surface `#f4f5f7` | 17.01 | Body text on light |
| Surface `#f4f5f7` | Ink `#11131a` | 17.01 | Body text on dark |
| Accent on light `#c2410c` | Surface `#f4f5f7` | 4.75 | Links and accent text on light, any size |
| Accent on light `#c2410c` | White `#ffffff` | 5.18 | Links and accent text on white |
| Accent `#ff6a13` | Ink `#11131a` | 6.47 | Links and accents on dark, any size |
| Accent `#ff6a13` | Logo dark `#2c2c2d` | 4.86 | Accents on dark panels |
| Surface `#f4f5f7` | Logo dark `#2c2c2d` | 12.79 | Text on dark panels |
| White `#ffffff` | Logo dark `#2c2c2d` | 13.95 | Text on dark panels, and the "#" on its square |

## Do not use for text

| Foreground | Background | Ratio | Why |
| --- | --- | --- | --- |
| Accent `#ff6a13` | Surface `#f4f5f7` | 2.63 | Below 3:1, fails even for large text. Use Accent on light instead |
| White `#ffffff` | Accent `#ff6a13` | 2.87 | Below 3:1. Do not put white text on an accent fill. Use Ink on the accent fill |

Ink on an Accent fill is 6.47 and is the pairing for buttons and badges with an accent background.

## Rules of thumb

1. On light backgrounds, accent text uses `#c2410c`. On dark backgrounds it uses `#ff6a13`.
2. The bright accent `#ff6a13` on a light background is for large decorative shapes only, never for text or thin lines.
3. Do not place the logo on an accent fill. Use a plain light or dark background, as in the [usage rules](../README.md#usage).
4. Use `--hc-accent-on-light` and `--hc-accent` from [`tokens.css`](../tokens.css) so the pairing is chosen by token and not by memory.

## Reproducing the numbers

```
channel = value / 255
linear  = channel / 12.92                      if channel <= 0.03928
        = ((channel + 0.055) / 1.055) ^ 2.4    otherwise
L       = 0.2126 * R + 0.7152 * G + 0.0722 * B
ratio   = (L_lighter + 0.05) / (L_darker + 0.05)
```

If a color in `colors.json` changes, recalculate this page.
