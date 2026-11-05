# MËSH talk — one source, slides + page
.PHONY: preview slides page render pdf publish clean

# quarto preview ignores {{< include >}}d files; tools/watch_includes.sh covers for that.
preview:          ## live preview of the slides (reloads on save)
	@tools/watch_includes.sh & W=$$!; trap 'kill $$W' EXIT INT TERM; \
	quarto preview index.qmd --to revealjs

page:             ## live preview of the web page
	@tools/watch_includes.sh & W=$$!; trap 'kill $$W' EXIT INT TERM; \
	quarto preview index.qmd --to html

render:           ## build both into _site/
	quarto render

pdf: render       ## fallback PDF of the deck (needs Node; downloads decktape once)
	npx --yes decktape@3.14.0 reveal --size 1600x900 _site/slides.html _site/slides.pdf

publish:          ## deploys via GitHub Actions: just push to main
	git push origin main

clean:
	rm -rf _site .quarto index_files
