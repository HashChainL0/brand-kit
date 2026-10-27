# Logo sizes and clear space

The logo files in [`logo/`](../logo) are square. This page turns the rules in the [README](../README.md#usage) into pixel values for each file and says which file to pick for a given display size. It adds no new rules.

## Rules this page uses

- Clear space is at least one quarter of the logo width on every side.
- The minimum size is 24px wide on screen.
- Scale proportionally, and do not enlarge a file past its own pixel size.

## Clear space per file

At the native size of each file, one quarter of the width is:

| File | Pixels | Clear space on each side |
| --- | --- | --- |
| `logo/logo-32.png` | 32 x 32 | 8px |
| `logo/logo-64.png` | 64 x 64 | 16px |
| `logo/logo-180.png` | 180 x 180 | 45px |
| `logo/logo-192.png` | 192 x 192 | 48px |
| `logo/logo-256.webp` | 256 x 256 | 64px |
| `logo/logo-512.png` | 512 x 512 | 128px |
| `logo/logo-1254.png` | 1254 x 1254 | 314px (313.5 rounded up) |

When the logo is shown at another size, clear space scales with it. At the 24px minimum, clear space is 6px, so the smallest footprint including clear space is 36px wide.

```css
.logo {
  width: 48px;
  height: 48px;
  margin: 12px; /* one quarter of 48px */
}
```

Clear space is empty. Do not put text, other marks or the edge of the container inside it.

## Which file for which size

Pick the smallest file that is at least as wide as the display width in device pixels. A file shown smaller than its own size stays sharp. A file stretched past its own size goes soft.

| Displayed width (CSS px) | At 1x density | At 2x density |
| --- | --- | --- |
| 24 | `logo-32.png` | `logo-64.png` |
| 32 | `logo-32.png` | `logo-64.png` |
| 48 | `logo-64.png` | `logo-180.png` |
| 64 | `logo-64.png` | `logo-180.png` |
| 96 | `logo-180.png` | `logo-192.png` |
| 128 | `logo-180.png` | `logo-256.webp` |
| 256 | `logo-256.webp` | `logo-512.png` |

For print and anything larger than 512px, use `logo-1254.png`, the original master.

```html
<img src="logo-64.png"
     srcset="logo-64.png 1x, logo-180.png 2x"
     width="48" height="48" alt="Hash Chain logo">
```

Always set `width` and `height` to the same value so the square is not stretched.

## Below the minimum

Under 24px the "#" stops reading. Do not shrink the logo further. Use the browser favicon, `logo/favicon.ico`, where a tab or a list needs an icon at that size, and write the name "Hash Chain" in text next to it if the context needs to say who it is.

## Checklist

1. The file is one of the originals in this kit.
2. The displayed width is 24px or more.
3. Width and height are equal.
4. A quarter of the width is free on every side.
5. The file is at least as wide as the display width in device pixels.
