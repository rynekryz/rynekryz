<div align="center">

# Pixel Art

Monochrome, animated pixel dividers and stickers for my profile.

<picture><source media="(prefers-color-scheme: dark)" srcset="divider-wave-dark.svg"><img src="divider-wave-light.svg" width="100%" alt=""></picture>

## Dividers

<picture><source media="(prefers-color-scheme: dark)" srcset="divider-dots-dark.svg"><img src="divider-dots-light.svg" width="100%" alt="dots divider"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="divider-sparkles-dark.svg"><img src="divider-sparkles-light.svg" width="100%" alt="sparkles divider"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="divider-wave-dark.svg"><img src="divider-wave-light.svg" width="100%" alt="wave divider"></picture>

## Sky

| <picture><source media="(prefers-color-scheme: dark)" srcset="sky-left-dark.svg"><img src="sky-left-light.svg" width="200" alt="night sky with moon"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="sky-right-dark.svg"><img src="sky-right-light.svg" width="200" alt="night sky with sparkles"></picture> |
| :---: | :---: |

## Stickers

| <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-heart-dark.svg"><img src="sticker-heart-light.svg" width="96" alt="heart"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-sparkle-dark.svg"><img src="sticker-sparkle-light.svg" width="96" alt="sparkle"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-moon-dark.svg"><img src="sticker-moon-light.svg" width="96" alt="moon"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-flower-dark.svg"><img src="sticker-flower-light.svg" width="96" alt="flower"></picture> |
| :---: | :---: | :---: | :---: |
| <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-cat-dark.svg"><img src="sticker-cat-light.svg" width="96" alt="cat"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-ghost-dark.svg"><img src="sticker-ghost-light.svg" width="96" alt="ghost"></picture> | <picture><source media="(prefers-color-scheme: dark)" srcset="sticker-lock-dark.svg"><img src="sticker-lock-light.svg" width="96" alt="lock"></picture> | |

## Usage

Move the SVG files into `assets/` and drop a block into the profile README.

Divider:

```html
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/divider-wave-dark.svg"><img src="assets/divider-wave-light.svg" width="100%" alt=""></picture>
```

Sticker:

```html
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/sticker-cat-dark.svg"><img src="assets/sticker-cat-light.svg" width="96" alt=""></picture>
```

## Files

```text
pixel-art
├── divider-dots-dark.svg
├── divider-dots-light.svg
├── divider-sparkles-dark.svg
├── divider-sparkles-light.svg
├── divider-wave-dark.svg
├── divider-wave-light.svg
├── sky-left-dark.svg
├── sky-left-light.svg
├── sky-right-dark.svg
├── sky-right-light.svg
├── sticker-cat-dark.svg
├── sticker-cat-light.svg
├── sticker-flower-dark.svg
├── sticker-flower-light.svg
├── sticker-ghost-dark.svg
├── sticker-ghost-light.svg
├── sticker-heart-dark.svg
├── sticker-heart-light.svg
├── sticker-lock-dark.svg
├── sticker-lock-light.svg
├── sticker-moon-dark.svg
├── sticker-moon-light.svg
├── sticker-sparkle-dark.svg
└── sticker-sparkle-light.svg
```

## Notes

All art is pure SVG, no dependencies. Every piece comes in a light and a dark version, so it stays monochrome on both GitHub themes. Animations use `steps()` for a chunky retro feel and turn off with `prefers-reduced-motion`.

</div>
