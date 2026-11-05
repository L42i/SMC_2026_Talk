#!/bin/sh
# quarto preview only watches index.qmd, not the files it pulls in with
# {{< include >}}. This touches index.qmd whenever a section changes, so the
# preview re-renders. Polling (no inotify/fswatch needed), works on Linux + macOS.
cd "$(dirname "$0")/.." || exit 1
stamp=$(mktemp)
trap 'rm -f "$stamp"' EXIT INT TERM
while :; do
  if [ -n "$(find sections -name '*.qmd' -newer "$stamp" 2>/dev/null)" ]; then
    touch "$stamp" index.qmd
  fi
  sleep 1
done
