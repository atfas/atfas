"""Generates the banner and buttons for the profile README. Run: python3 build.py"""
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Inter, Arial, sans-serif"
FEUP = "#8c2d19"

NAME = "Afonso Saraiva"
SUFFIX = "MSc @ FEUP"
# (file, label, live) — a button that isn't live yet renders faded, without the chevron
BUTTONS = [("cv", "CV", True), ("portfolio", "Portfolio  ·  Soon", False)]

STYLE = """
  .up { opacity: 0; animation: up 1s cubic-bezier(.2,.8,.2,1) forwards; }
  .d1 { animation-delay: .1s } .d2 { animation-delay: .3s }
  @keyframes up { from { opacity: 0; transform: translateY(10px) } to { opacity: 1; transform: none } }
  @media (prefers-reduced-motion: reduce) { .up { animation: none; opacity: 1 } }
"""


def banner():
    w, h = 1000, 180
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#94301b"/><stop offset="1" stop-color="{FEUP}"/></linearGradient>
    <radialGradient id="hi" cx=".5" cy="0" r=".7"><stop offset="0" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <clipPath id="c"><rect width="{w}" height="{h}" rx="24"/></clipPath>
  </defs>
  <style>{STYLE}</style>
  <g clip-path="url(#c)">
    <rect width="{w}" height="{h}" fill="url(#bg)"/>
    <rect width="{w}" height="{h}" fill="url(#hi)"/>
  </g>
  <text class="up d1" x="500" y="106" text-anchor="middle" font-size="50" fill="#fff" letter-spacing="-1.5">
    <tspan font-weight="700">{NAME}</tspan><tspan font-weight="400" fill-opacity=".45" dx="14">·</tspan><tspan font-weight="500" fill-opacity=".78" dx="14">{SUFFIX}</tspan>
  </text>
</svg>'''


def button(label, live):
    w, h = 26 * 2 + len(label) * 9.6 + 18, 44
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h}" viewBox="0 0 {w:.0f} {h}" font-family="{FONT}">
  <rect width="{w:.0f}" height="{h}" rx="22" fill="{FEUP}" fill-opacity="{1 if live else .5}"/>
  <text x="{w / 2:.0f}" y="28.5" text-anchor="middle" font-size="16" font-weight="600" fill="#fff">{label}{"  ›" if live else ""}</text>
</svg>'''


(OUT / "banner.svg").write_text(banner())
for name, label, live in BUTTONS:
    (OUT / f"{name}.svg").write_text(button(label, live))
print("ok")
