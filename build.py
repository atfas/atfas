"""Generates the banner and links for the profile README. Run: python3 build.py"""
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', Inter, Arial, sans-serif"
FEUP = "#8c2d19"
FEUP_ON_DARK = "#e07a5f"  # lighter FEUP tone so links stay readable on GitHub dark
GRAY = "#86868b"  # Apple's secondary text gray; readable on GitHub's light and dark backgrounds

NAME = "Afonso Saraiva"
SUFFIX = "MSc @ FEUP"

STYLE = """
  .up { opacity: 0; animation: up .9s cubic-bezier(.2,.8,.2,1) .1s forwards; }
  @keyframes up { from { opacity: 0; transform: translateY(6px) } to { opacity: 1; transform: none } }
  @media (prefers-reduced-motion: reduce) { .up { animation: none; opacity: 1 } }
"""


def banner():
    w, h = 1000, 112
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
  <defs>
    <radialGradient id="hi" cx=".5" cy="0" r=".7"><stop offset="0" stop-color="#fff" stop-opacity=".07"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    <clipPath id="c"><rect width="{w}" height="{h}" rx="20"/></clipPath>
  </defs>
  <style>{STYLE}</style>
  <g clip-path="url(#c)">
    <rect width="{w}" height="{h}" fill="{FEUP}"/>
    <rect width="{w}" height="{h}" fill="url(#hi)"/>
  </g>
  <text class="up" x="500" y="68" text-anchor="middle" font-size="34" fill="#fff" letter-spacing="-.8">
    <tspan font-weight="700">{NAME}</tspan><tspan font-weight="400" fill-opacity=".45" dx="10">·</tspan><tspan font-weight="500" fill-opacity=".78" dx="10">{SUFFIX}</tspan>
  </text>
</svg>'''


def link(label, color):
    """Apple-style text link: colored text with a chevron, no button chrome."""
    w, h = round(len(label) * 8.3 + 18), 34
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
  <text x="{w / 2}" y="22" text-anchor="middle" font-size="15" font-weight="500" fill="{color}" letter-spacing="-.1">{label} ›</text>
</svg>'''


def note(label):
    """Quiet secondary text, sized to sit beside a pill."""
    w, h = round(len(label) * 7.9 + 4), 34
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
  <text x="{w / 2}" y="22" text-anchor="middle" font-size="15" font-weight="400" fill="{GRAY}" letter-spacing="-.1">{label}</text>
</svg>'''


(OUT / "banner.svg").write_text(banner())
(OUT / "cv-light.svg").write_text(link("View CV", FEUP))
(OUT / "cv-dark.svg").write_text(link("View CV", FEUP_ON_DARK))
(OUT / "portfolio.svg").write_text(note("Portfolio coming soon"))
print("ok")
