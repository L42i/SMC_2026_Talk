# From SPRAWL to MËSH — talk (SMC 2026)

One Markdown source, two outputs:

| Output | File | Use it for |
|---|---|---|
| Slides (reveal.js) | `_site/slides.html` | presenting (screen-share this window) |
| Web page | `_site/index.html` | the link you post in the chat; reading afterwards |

Built from the SMC 2026 paper (Windish & von Coler).

## Quick start

```bash
quarto render            # build both
make preview             # live slides while editing
make page                # live page while editing
make pdf                 # fallback PDF of the deck
```

Requires [Quarto](https://quarto.org) ≥ 1.5 (tested with 1.6).

## Structure

`index.qmd` holds only the title block and one include per section:

```
sections/01-why.qmd          intro, problem, timeline, related work
sections/02-sprawl.qmd       SPRAWL, SPRAWL V2, Goat Farm, SC Symposium
sections/03-mesh.qmd         design goals, architecture, hardware, software
sections/04-on-the-road.qmd  Kuala Lumpur
sections/05-icmc.qmd         ICMC Hamburg: concert, installation, workshop
sections/06-wrap-up.qmd      summary and outlook, references
```

Reorder or delete include lines to restructure the talk. Paths inside the
section files (images, figures) are relative to the project root, because
includes are pasted into `index.qmd` before rendering. Don't put HTML
comments in `index.qmd` before the first section: they create an empty slide.

## Writing conventions (in the section files)

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
index.qmd              title block + section includes
sections/*.qmd         the talk, one file per section
sections/_timeline.qmd HTML port of tikz/timeline.tex (steps in on slides, stacks on phones)
_quarto.yml            formats, sizes, bibliography
filters/hybrid.lua     prose → notes, slides-only / page-only, photo headings
theme/slides.scss      deck theme (paper colours, big type for video calls)
theme/page.scss        page theme
theme/components.css   timeline + big-number blocks, shared by both
figures/topology.svg   SPRAWL V2 mesh vs. MËSH star (tools/make_topology.py)
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
