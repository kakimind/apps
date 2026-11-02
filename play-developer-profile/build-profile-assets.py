# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

PAPER     = (242, 240, 232)
INK       = (16, 16, 18)
INK_SOFT  = (85, 83, 76)
INK_FAINT = (148, 145, 138)
RULE      = (198, 194, 184)

SPOTS = [("01", (168,  85, 201)),   # PomPom Ville
         ("02", (193, 105,  79)),   # 어디뒀지?
         ("03", (255, 122,  61)),   # 불씨
         ("04", ( 46, 125, 154)),   # 동행
         ("05", (217, 172,  82)),   # Dear Star, My Wish
         ("06", (232,  80,  47)),   # Orbit Hop
         ("07", (155, 107, 255)),   # Top of Gravity
         ("08", ( 47, 124, 246)),   # Bubble Rumble
         ("09", ( 42, 125,  95))]   # 연화사

# The header spells the count out, and it went stale once already: the
# artwork still read SIX after two more titles had shipped. Spelling it
# from the list means adding a title above is the only edit needed.
COUNT_WORD = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
              6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN",
              11: "ELEVEN", 12: "TWELVE"}.get(len(SPOTS), str(len(SPOTS)))


def shoulders(size, wght=900):
    f = ImageFont.truetype(os.path.join(F, "BigShouldersDisplay.ttf"), int(size))
    f.set_variation_by_axes([wght])
    return f


def serif(size, wght=400, opsz=60, italic=False):
    name = "SourceSerif4-Italic.ttf" if italic else "SourceSerif4.ttf"
    f = ImageFont.truetype(os.path.join(F, name), int(size))
    f.set_variation_by_axes([opsz, wght])
    return f


def mono(size, bold=False):
    return ImageFont.truetype(
        os.path.join(F, "SpaceMono-Bold.ttf" if bold else "SpaceMono-Regular.ttf"),
        int(size))


def render_tracked(text, font, fill, track):
    """Draw letter-spaced text on its own layer, cropped tight to the ink."""
    pad = int(font.size * 1.5) + 8
    adv = sum(font.getlength(c) for c in text) + track * (len(text) - 1)
    layer = Image.new("RGBA", (int(adv) + pad * 2, int(font.size * 3) + pad * 2),
                      (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x = pad
    for ch in text:
        d.text((x, pad), ch, font=font, fill=fill + (255,), anchor="la")
        x += font.getlength(ch) + track
    return layer.crop(layer.getbbox())


def paste_center(img, layer, cx, top):
    img.paste(layer, (int(cx - layer.width / 2), int(top)), layer)
    return top + layer.height


def paste_at(img, layer, x, top, align="l"):
    if align == "r":
        x -= layer.width
    img.paste(layer, (int(x), int(top)), layer)
    return top + layer.height


def fit_to_width(text, target_w, track_ratio, wght=900):
    lo, hi = 10.0, 6000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        f = shoulders(mid, wght)
        w = sum(f.getlength(c) for c in text) + mid * track_ratio * (len(text) - 1)
        if w < target_w:
            lo = mid
        else:
            hi = mid
    return lo


def fit_to_height(text, target_h, track, wght=900):
    lo, hi = 10.0, 6000.0
    for _ in range(40):
        mid = (lo + hi) / 2
        h = render_tracked(text, shoulders(mid, wght), INK, mid * track).height
        if h < target_h:
            lo = mid
        else:
            hi = mid
    return lo


# ---------------------------------------------------------------- icon 512
def build_icon(path, size=512):
    S, W = 4, 512 * 4
    img = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(img)
    p = lambda v: int(round(v * S))
    cx = W / 2

    d.rectangle([p(16), p(16), W - p(16) - 1, W - p(16) - 1], outline=INK, width=p(11))
    d.rectangle([p(40), p(40), W - p(40) - 1, W - p(40) - 1], outline=INK, width=p(3))

    mg_track = -0.045
    mg_size = fit_to_height("KM", p(156), mg_track)
    mg = render_tracked("KM", shoulders(mg_size), INK, mg_size * mg_track)

    wm_f = mono(p(26), bold=True)
    wm = render_tracked("KAKIMIND", wm_f, INK, p(26) * 0.22)

    bar_w, bar_h, gap = p(26), p(9), p(9)
    bars_w = len(SPOTS) * bar_w + (len(SPOTS) - 1) * gap

    stack = mg.height + p(30) + p(5) + p(26) + wm.height + p(30) + bar_h
    y = p(40) + (W - p(80) - stack) / 2

    y = paste_center(img, mg, cx, y) + p(30)
    d.rectangle([cx - p(80), y, cx + p(80), y + p(5)], fill=INK)
    y += p(5) + p(26)
    y = paste_center(img, wm, cx, y) + p(30)

    bx = cx - bars_w / 2
    for _, colour in SPOTS:
        d.rectangle([bx, y, bx + bar_w, y + bar_h], fill=colour)
        bx += bar_w + gap

    img.resize((size, size), Image.LANCZOS).save(path, "PNG", optimize=True)


# ------------------------------------------------------------- header 16:9
def build_header(path, W=4096, H=2304):
    S = 2
    img = Image.new("RGB", (W * S, H * S), PAPER)
    d = ImageDraw.Draw(img)
    p = lambda v: int(round(v * S))
    L, R = p(300), W * S - p(300)
    cx = W * S / 2

    # running head
    fr = mono(p(34))
    y = p(185)
    paste_at(img, render_tracked("KAKIMIND", fr, INK_SOFT, p(34) * 0.22), L, y)
    paste_at(img, render_tracked("NO. 01 \u2014 2026", fr, INK_SOFT, p(34) * 0.22),
             R, y, align="r")
    d.rectangle([L, p(258), R, p(258) + p(5)], fill=INK)
    d.rectangle([L, p(276), R, p(276) + p(2)], fill=INK)

    # kicker
    y = paste_center(img, render_tracked("SOLO ANDROID STUDIO",
                                         mono(p(42), bold=True), INK_SOFT,
                                         p(42) * 0.36), cx, p(430))

    # masthead
    tr = -0.012
    ms = fit_to_width("KAKIMIND", p(2680), tr)
    y = paste_center(img, render_tracked("KAKIMIND", shoulders(ms), INK, ms * tr),
                     cx, p(590))

    # rule + dek
    y += p(64)
    d.rectangle([L, y, R, y + p(5)], fill=INK)
    y += p(5) + p(72)
    y = paste_center(img, render_tracked(
        "Apps and games made end to end by one person \u2014 after hours, "
        "on weekends.", serif(p(72), 400, 60, italic=True), INK_SOFT, 0), cx, y)

    # the six titles, as spot-colour register bars
    y += p(130)
    bar_w, gap, bar_h = p(330), p(44), p(24)
    bars_w = len(SPOTS) * bar_w + (len(SPOTS) - 1) * gap
    bx = cx - bars_w / 2
    fnum = mono(p(32), bold=True)
    for num, colour in SPOTS:
        d.rectangle([bx, y, bx + bar_w, y + bar_h], fill=colour)
        paste_at(img, render_tracked("\u00a7" + num, fnum, INK_FAINT, p(32) * 0.16),
                 bx, y + bar_h + p(26))
        bx += bar_w + gap

    paste_center(img, render_tracked(f"{COUNT_WORD} TITLES INSIDE \u2014 GOOGLE PLAY",
                                     mono(p(38)), INK_SOFT, p(38) * 0.28),
                 cx, y + bar_h + p(118))

    # quiet baseline (Play overlays the developer name down here)
    fy = H * S - p(190)
    d.rectangle([L, fy, R, fy + p(2)], fill=RULE)
    ff = mono(p(32))
    paste_at(img, render_tracked("KAKIMIND.GITHUB.IO", ff, INK_FAINT, p(32) * 0.20),
             L, fy + p(52))
    paste_at(img, render_tracked("PRINTED ON THE WEB", ff, INK_FAINT, p(32) * 0.20),
             R, fy + p(52), align="r")

    img.resize((W, H), Image.LANCZOS).save(path, "PNG", optimize=True)


icon_path = os.path.join(OUT, "kakimind-developer-icon-512.png")
head_path = os.path.join(OUT, "kakimind-developer-header-4096x2304.png")
build_icon(icon_path)
build_header(head_path)
for pth in (icon_path, head_path):
    im = Image.open(pth)
    print(os.path.basename(pth), im.size, im.mode, f"{os.path.getsize(pth)/1024:.0f} KB")

Image.open(head_path).resize((1400, 788), Image.LANCZOS).save(
    os.path.join(OUT, "preview-header.png"))
Image.open(icon_path).resize((48, 48), Image.LANCZOS).resize(
    (288, 288), Image.NEAREST).save(os.path.join(OUT, "preview-icon-48.png"))
