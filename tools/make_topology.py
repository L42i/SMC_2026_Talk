#!/usr/bin/env python3
"""Generate figures/topology.svg: SPRAWL V2 wired, fully connected mesh vs. MËSH wireless star.
Colours match the slide palette (V2 green / MËSH purple)."""
import math
TEAL, ORANGE, INK, MUTED = "#2ec27e", "#9141ac", "#1d232b", "#6e6e6e"
W, H = 1400, 620
out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
  'font-family="IBM Plex Sans, Helvetica, Arial, sans-serif" role="img" '
  'aria-label="SPRAWL V2 access points wired as a fully connected mesh versus MËSH nodes connected wirelessly to a router">')

def pts(cx, cy, r, n, off=-90):
    return [(cx + r*math.cos(math.radians(off + i*360/n)),
             cy + r*math.sin(math.radians(off + i*360/n))) for i in range(n)]

# ---- left: SPRAWL V2 fully connected mesh (every AP wired to every other) ----
cx, cy, r = 340, 300, 185
P = pts(cx, cy, r, 6)
for i in range(6):
    for j in range(i + 1, 6):
        (x1, y1), (x2, y2) = P[i], P[j]
        a(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{TEAL}" stroke-width="4"/>')
for x, y in P:
    a(f'<rect x="{x-38:.0f}" y="{y-28:.0f}" width="76" height="56" rx="6" fill="#fff" stroke="{TEAL}" stroke-width="4"/>')
    a(f'<text x="{x:.0f}" y="{y+8:.0f}" text-anchor="middle" font-size="22" font-weight="700" fill="{TEAL}">AP</text>')
a(f'<text x="{cx}" y="44" text-anchor="middle" font-size="40" font-weight="700" fill="{TEAL}">SPRAWL V2</text>')
a(f'<text x="{cx}" y="{H-54}" text-anchor="middle" font-size="22" fill="{MUTED}">fully connected mesh</text>')
a(f'<text x="{cx}" y="{H-24}" text-anchor="middle" font-size="25" fill="{INK}">wired Ethernet · audio + control</text>')

# divider
a(f'<line x1="{W/2}" y1="40" x2="{W/2}" y2="{H-80}" stroke="#d0d0d0" stroke-width="2" stroke-dasharray="4 8"/>')

# ---- right: MËSH star ----
cx, cy, r = 1060, 300, 200
P = pts(cx, cy, r, 8, off=-90+22.5)
for x, y in P:
    a(f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="3 11" stroke-linecap="round"/>')
for x, y in P:
    a(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="{ORANGE}"/>')
    a(f'<text x="{x:.0f}" y="{y+7:.0f}" text-anchor="middle" font-size="19" font-weight="700" fill="#fff">SC</text>')
# router
a(f'<rect x="{cx-66}" y="{cy-34}" width="132" height="68" rx="10" fill="{INK}"/>')
for dx in (-34, 34):
    a(f'<line x1="{cx+dx}" y1="{cy-34}" x2="{cx+dx*1.25:.0f}" y2="{cy-62}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
a(f'<text x="{cx}" y="{cy+8}" text-anchor="middle" font-size="22" font-weight="700" fill="#fff">router</text>')
a(f'<text x="{cx}" y="{cy+68}" text-anchor="middle" font-size="22" fill="{ORANGE}">OSC</text>')
a(f'<text x="{cx}" y="{H-24}" text-anchor="middle" font-size="25" fill="{INK}">wireless LAN · control only, audio made locally</text>')
a(f'<text x="{cx}" y="44" text-anchor="middle" font-size="40" font-weight="700" fill="{ORANGE}">MËSH</text>')
a('</svg>')
svg = "\n".join(out)
open("figures/topology.svg", "w").write(svg)
print("wrote figures/topology.svg")
# MËSH half only (right panel): same drawing, cropped by the viewBox
mesh = svg.replace(f'viewBox="0 0 {W} {H}"', f'viewBox="{W//2} 0 {W//2} {H}"', 1)
open("figures/topology_mesh.svg", "w").write(mesh)
print("wrote figures/topology_mesh.svg")
# SPRAWL V2 half only (left panel)
v2 = svg.replace(f'viewBox="0 0 {W} {H}"', f'viewBox="0 0 {W//2} {H}"', 1)
open("figures/topology_v2.svg", "w").write(v2)
print("wrote figures/topology_v2.svg")
