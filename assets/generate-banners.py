import random, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
F = 'Apple SD Gothic Neo'

# 캔버스는 1200x1200(qlmanage 정사각 렌더용), 실제 배너 영역은 y=285..915 (1200x630)
TOP, BOT, H = 285, 915, 630


def frame(defs, art, badge, title, tagline, accent, slug):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200" viewBox="0 0 1200 1200">
<defs>
{defs}
<linearGradient id="scrim" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#000" stop-opacity=".78"/>
  <stop offset="55%" stop-color="#000" stop-opacity=".35"/>
  <stop offset="100%" stop-color="#000" stop-opacity="0"/>
</linearGradient>
<clipPath id="band"><rect x="0" y="{TOP}" width="1200" height="{H}"/></clipPath>
</defs>
<rect width="1200" height="1200" fill="#05060a"/>
<g clip-path="url(#band)">
{art}
  <rect x="0" y="{TOP}" width="820" height="{H}" fill="url(#scrim)"/>

  <!-- 장르 배지 -->
  <rect x="80" y="{TOP+92}" width="{28+len(badge)*23}" height="48" rx="24" fill="{accent}" fill-opacity=".18" stroke="{accent}" stroke-opacity=".55"/>
  <text x="{94}" y="{TOP+125}" font-family="{F}" font-size="26" font-weight="600" fill="{accent}" letter-spacing="2">{badge}</text>

  <!-- 타이틀 -->
  <text x="80" y="{TOP+252}" font-family="{F}" font-size="104" font-weight="800" fill="#fff" letter-spacing="-2">{title}</text>

  <!-- 태그라인 -->
  <text x="80" y="{TOP+318}" font-family="{F}" font-size="34" fill="#fff" fill-opacity=".72">{tagline}</text>

  <!-- 하단 브랜드 바 -->
  <rect x="80" y="{TOP+430}" width="56" height="4" rx="2" fill="{accent}"/>
  <text x="80" y="{TOP+488}" font-family="{F}" font-size="25" font-weight="700" fill="#fff" fill-opacity=".92" letter-spacing="3">NEWPLAY 웹스토어</text>
  <text x="80" y="{TOP+528}" font-family="{F}" font-size="23" fill="#fff" fill-opacity=".45" letter-spacing="1">/{slug}</text>
</g>
</svg>'''


# ---------- 1. 코스믹 드리프트 : 우주 레이싱 ----------
random.seed(11)
stars = ''.join(
    f'<circle cx="{random.randint(0,1200)}" cy="{random.randint(TOP,BOT)}" r="{random.choice([1,1,1.5,2,2.5])}" fill="#fff" fill-opacity="{random.uniform(.25,.95):.2f}"/>'
    for _ in range(190))
streaks = ''.join(
    f'<rect x="{random.randint(300,1000)}" y="{random.randint(TOP+40,BOT-40)}" width="{random.randint(90,300)}" height="{random.choice([2,2,3])}" rx="1.5" fill="url(#streak)" fill-opacity="{random.uniform(.3,.9):.2f}"/>'
    for _ in range(22))

g1_defs = '''<radialGradient id="space" cx="72%" cy="34%" r="88%">
  <stop offset="0%" stop-color="#2b3f8f"/><stop offset="45%" stop-color="#141a4a"/><stop offset="100%" stop-color="#05060f"/>
</radialGradient>
<linearGradient id="streak" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#5ad4ff" stop-opacity="0"/><stop offset="100%" stop-color="#9fe8ff"/>
</linearGradient>
<linearGradient id="planet" x1="0.2" y1="0" x2="0.9" y2="1">
  <stop offset="0%" stop-color="#7c8cff"/><stop offset="55%" stop-color="#3b3f9e"/><stop offset="100%" stop-color="#141640"/>
</linearGradient>
<linearGradient id="horizon" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#5ad4ff" stop-opacity="0"/><stop offset="50%" stop-color="#5ad4ff"/><stop offset="100%" stop-color="#5ad4ff" stop-opacity="0"/>
</linearGradient>'''

g1_art = f'''  <rect x="0" y="{TOP}" width="1200" height="{H}" fill="url(#space)"/>
  {stars}
  <circle cx="985" cy="{TOP+250}" r="185" fill="url(#planet)"/>
  <circle cx="985" cy="{TOP+250}" r="185" fill="none" stroke="#9fb4ff" stroke-opacity=".35" stroke-width="2"/>
  <ellipse cx="985" cy="{TOP+250}" rx="285" ry="52" fill="none" stroke="#8fd8ff" stroke-opacity=".55" stroke-width="7" transform="rotate(-18 985 {TOP+250})"/>
  <ellipse cx="985" cy="{TOP+250}" rx="325" ry="60" fill="none" stroke="#8fd8ff" stroke-opacity=".22" stroke-width="3" transform="rotate(-18 985 {TOP+250})"/>
  {streaks}
  <rect x="0" y="{BOT-92}" width="1200" height="3" fill="url(#horizon)" fill-opacity=".8"/>'''

# ---------- 2. 던전 오브 엠버 : 로그라이크 RPG ----------
random.seed(22)
embers = ''.join(
    f'<circle cx="{random.randint(560,1200)}" cy="{random.randint(TOP+30,BOT-20)}" r="{random.choice([2,2.5,3,4,5])}" fill="#ffae4d" fill-opacity="{random.uniform(.3,1):.2f}"/>'
    for _ in range(95))
bricks = ''
for row in range(9):
    y = TOP + row * 70
    off = 0 if row % 2 == 0 else 95
    for col in range(8):
        x = 620 + off + col * 190
        bricks += f'<rect x="{x}" y="{y}" width="180" height="60" rx="4" fill="none" stroke="#5a2a16" stroke-opacity=".55" stroke-width="2"/>'

g2_defs = '''<linearGradient id="stone" x1="0" y1="0" x2="1" y2="0.6">
  <stop offset="0%" stop-color="#120a08"/><stop offset="60%" stop-color="#2a120c"/><stop offset="100%" stop-color="#4a1d0e"/>
</linearGradient>
<radialGradient id="emberglow" cx="78%" cy="72%" r="62%">
  <stop offset="0%" stop-color="#ff7a29" stop-opacity=".85"/><stop offset="45%" stop-color="#c2400f" stop-opacity=".35"/><stop offset="100%" stop-color="#ff7a29" stop-opacity="0"/>
</radialGradient>
<linearGradient id="arch" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#ffb066" stop-opacity=".9"/><stop offset="100%" stop-color="#ff5a1f" stop-opacity=".15"/>
</linearGradient>'''

g2_art = f'''  <rect x="0" y="{TOP}" width="1200" height="{H}" fill="url(#stone)"/>
  <g opacity=".5">{bricks}</g>
  <rect x="0" y="{TOP}" width="1200" height="{H}" fill="url(#emberglow)"/>
  <path d="M 860 {BOT} L 860 {TOP+300} Q 960 {TOP+120} 1060 {TOP+300} L 1060 {BOT} Z" fill="none" stroke="url(#arch)" stroke-width="9"/>
  <path d="M 905 {BOT} L 905 {TOP+330} Q 960 {TOP+205} 1015 {TOP+330} L 1015 {BOT} Z" fill="#ff8c33" fill-opacity=".13"/>
  {embers}
  <rect x="0" y="{BOT-4}" width="1200" height="4" fill="#ff7a29" fill-opacity=".6"/>'''

# ---------- 3. 픽셀 팜 스토리 : 힐링 농장 시뮬 ----------
random.seed(33)
crops = ''
for row in range(3):
    y = BOT - 118 + row * 32
    for col in range(26):
        x = 430 + col * 31 + row * 15
        c = random.choice(['#3fae5f', '#59c46f', '#2f8f4a', '#f2c14e'])
        crops += f'<rect x="{x}" y="{y}" width="16" height="16" rx="2" fill="{c}" fill-opacity=".9"/>'
clouds = ''.join(
    f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{rx*0.34:.0f}" fill="#fff" fill-opacity="{op}"/>'
    for cx, cy, rx, op in [(760, TOP+95, 95, .5), (830, TOP+112, 70, .45), (1055, TOP+165, 78, .38), (1110, TOP+180, 55, .32)])

g3_defs = '''<linearGradient id="sky" x1="0" y1="0" x2="0.3" y2="1">
  <stop offset="0%" stop-color="#ffd9a0"/><stop offset="40%" stop-color="#8fd0e8"/><stop offset="100%" stop-color="#2f7f6a"/>
</linearGradient>
<radialGradient id="sunglow" cx="82%" cy="22%" r="35%">
  <stop offset="0%" stop-color="#fff3c4" stop-opacity=".95"/><stop offset="100%" stop-color="#ffd166" stop-opacity="0"/>
</radialGradient>'''

g3_art = f'''  <rect x="0" y="{TOP}" width="1200" height="{H}" fill="url(#sky)"/>
  <rect x="0" y="{TOP}" width="1200" height="{H}" fill="url(#sunglow)"/>
  <circle cx="985" cy="{TOP+150}" r="72" fill="#ffe9a8" fill-opacity=".95"/>
  {clouds}
  <path d="M 0 {BOT-215} Q 300 {BOT-300} 620 {BOT-225} T 1200 {BOT-260} L 1200 {BOT} L 0 {BOT} Z" fill="#2e7d4f"/>
  <path d="M 0 {BOT-150} Q 380 {BOT-225} 760 {BOT-160} T 1200 {BOT-185} L 1200 {BOT} L 0 {BOT} Z" fill="#3f9a5c"/>
  {crops}
  <g transform="translate(760 {BOT-320})">
    <rect x="0" y="60" width="140" height="112" fill="#c0442f"/>
    <path d="M -16 60 L 70 4 L 156 60 Z" fill="#8f2f20"/>
    <rect x="52" y="106" width="38" height="66" fill="#f5e6c8"/>
  </g>
  <rect x="0" y="{BOT-4}" width="1200" height="4" fill="#f2c14e" fill-opacity=".7"/>'''

GAMES = [
    (1, g1_defs, g1_art, 'SPACE RACING', '코스믹 드리프트', '은하를 가로지르는 초고속 레이싱', '#7fe3ff', 'cosmic-drift'),
    (2, g2_defs, g2_art, 'ROGUELIKE RPG', '던전 오브 엠버', '매번 새로 생성되는 던전을 탐험하라', '#ffab5c', 'dungeon-of-ember'),
    (3, g3_defs, g3_art, 'FARM SIM', '픽셀 팜 스토리', '느긋하게 즐기는 픽셀 농장 라이프', '#ffe08a', 'pixel-farm-story'),
]

for n, defs, art, badge, title, tagline, accent, slug in GAMES:
    svg = frame(defs, art, badge, title, tagline, accent, slug)
    open(f'{OUT}/game{n}.svg', 'w').write(svg)
    print(f'wrote {OUT}/game{n}.svg ({len(svg)} bytes)')
