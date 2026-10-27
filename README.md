# From SPRAWL to MËSH

## Presentation for the 2026 SMC  Paper

*H. Windish and H. von Coler, “From SPRAWL to MËSH: Networked music systems for touring and stage integration,” in Proc. 23rd Sound and Music Computing Conf. (SMC 2026), Zagreb, Croatia, 2026*

**Show the presentation as GH page: https://l42i.github.io/SMC_2026_Talk/**

Conference website: https://smc26.mbz.hr/


---

## Build Instructions

One Markdown source, two outputs:

| Output | File | Use it for |
|---|---|---|
| Slides (reveal.js) | `_site/slides.html` | presenting (screen-share this window) |
| Web page | `_site/index.html` | the link you post in the chat; reading afterwards |



## Quick start

```bash
quarto render            # build both
make preview             # live slides while editing
make page                # live page while editing
make pdf                 # fallback PDF of the deck
```

Requires [Quarto](https://quarto.org) ≥ 1.5 (tested with 1.6).

## Writing conventions (all in `index.qmd`)

| You write | Slides | Page |
|---|---|---|
| `## Heading` | new slide | section |
| `# Heading {background-image="…"}` | photo divider slide | heading + photo |
| `::: prose` … `:::` | speaker notes (press **S**) | body text |
| `::: slides-only` | shown | hidden |
| `::: page-only` | hidden | shown |
| `::: {.fragment}` | steps in | always visible |
| `{.photo .ph}` on an image | height-capped photo | full-width photo |

The `prose` blocks are the point of the setup: you write what you'll say once;
it's your notes when presenting and the readable text for people who missed the talk.
This is handled by `filters/hybrid.lua`.

## Files


```
index.qmd              the talk
_timeline.qmd          HTML port of tikz/timeline.tex (steps in on slides, stacks on phones)
_quarto.yml            formats, sizes, bibliography
filters/hybrid.lua     prose → notes, slides-only / page-only, photo headings
theme/slides.scss      deck theme (paper colours, big type for video calls)
theme/page.scss        page theme
theme/components.css   timeline + big-number blocks, shared by both
figures/topology.svg   SPRAWL V2 ring vs. MËSH star (tools/make_topology.py)
pictures/              photos, downscaled to 2000 px (tools/prepare_images.py)
references.bib, ieee.csl
```

Re-create the photos from the paper's originals:
`python3 tools/prepare_images.py ../paper/pictures pictures`

## Presenting online

1. Open `slides.html`, press **S** for the speaker view (notes, timer, next slide) and move it to your second screen.
2. Share only the slides window. Press **F** for fullscreen.
3. Post the page URL in the chat at the start.
4. Keep `slides.pdf` around as a fallback.
5. `?view=scroll` on the slides URL gives a scrolling version; on phones that happens automatically.

## Publishing (GitHub Pages)

1. Create a repo, e.g. `mesh-smc2026-talk`, and push this folder to `main`.
2. In the repo: **Settings → Pages → Source: GitHub Actions**.
3. Every push to `main` now runs `.github/workflows/publish.yml`, which renders
   with Quarto and deploys. The **Actions** tab shows progress (~1–2 min).

Result:

- page:   `https://<owner>.github.io/<repo>/`
- slides: `https://<owner>.github.io/<repo>/slides.html`

Put that URL on the "Thank you" slide (`slides-only` block near the end).
