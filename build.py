"""Generates the light/dark banner for the profile README. Run: python3 build.py"""
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Inter, Arial, sans-serif"

EYEBROW = "Afonso Saraiva  ·  MSc @ FEUP"
STATEMENT = "Thoughtful software. From database to pixel."

THEMES = {
    "light": dict(bg="#f5f5f7", text="#1d1d1f", g1="#8c2d19", g2="#b8472b", orb=".12"),
    "dark":  dict(bg="#161617", text="#f5f5f7", g1="#c4553a", g2="#e8957d", orb=".30"),
}

STYLE = """
  .up { opacity: 0; animation: up 1s cubic-bezier(.2,.8,.2,1) forwards; }
  .d1 { animation-delay: .1s } .d2 { animation-delay: .35s }
  @keyframes up { from { opacity: 0; transform: translateY(10px) } to { opacity: 1; transform: none } }
  @media (prefers-reduced-motion: reduce) { .up { animation: none; opacity: 1 } }
"""


def banner(t):
    w, h = 1000, 200
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="{FONT}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['g1']}"/><stop offset="1" stop-color="{t['g2']}"/></linearGradient>
    <radialGradient id="orb" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#8c2d19" stop-opacity="{t['orb']}"/><stop offset="1" stop-color="#8c2d19" stop-opacity="0"/></radialGradient>
    <clipPath id="c"><rect width="{w}" height="{h}" rx="24"/></clipPath>
  </defs>
  <style>{STYLE}</style>
  <g clip-path="url(#c)">
    <rect width="{w}" height="{h}" fill="{t['bg']}"/>
    <ellipse cx="500" cy="230" rx="460" ry="150" fill="url(#orb)"/>
  </g>
  <text class="up d1" x="500" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="url(#g)" letter-spacing=".3">{EYEBROW}</text>
  <text class="up d2" x="500" y="132" text-anchor="middle" font-size="44" font-weight="700" fill="{t['text']}" letter-spacing="-1.4">{STATEMENT}</text>
</svg>'''


for name, t in THEMES.items():
    (OUT / f"banner-{name}.svg").write_text(banner(t))
print("ok")
