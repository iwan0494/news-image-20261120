# Render the 20 November 2026 one-day news poster to poster-20261120.png.
# Deterministic: no randomness, no clock, no timestamps in the output.
# Run: python3 poster.py   (writes poster-20261120.png next to this file)

import hashlib
import os
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import stories

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (20, 20, 20)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
GREY = (201, 194, 176)
MUTED = (90, 83, 72)
LIGHT = (255, 255, 255)
CREAM = (238, 231, 214)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731
F_BODY = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731
F_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)  # noqa: E731


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, fill=INK, leading=0):
    lh = fnt.size + leading
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


def centre(draw, y, text, fnt, fill=INK):
    tw = draw.textlength(text, font=fnt)
    draw.text(((W - tw) / 2, y), text, font=fnt, fill=fill)


# ---------------------------------------------------------------- icons
def icon_scales(d, x, y, s, col):
    cx, cy = x + s // 2, y + s // 2
    d.line([(cx, y + 8), (cx, y + s - 14)], fill=col, width=4)
    d.line([(x + 8, y + 18), (x + s - 8, y + 18)], fill=col, width=4)
    d.polygon([(x + 2, y + 30), (x + 22, y + 30), (x + 12, y + s - 12)], outline=col)
    d.polygon([(x + s - 22, y + 30), (x + s - 2, y + 30), (x + s - 12, y + s - 12)], outline=col)
    d.ellipse([cx - 5, y + 2, cx + 5, y + 12], fill=col)


def icon_summit(d, x, y, s, col):
    cols = [RED, (200, 160, 40), NAVY]
    for i, c in enumerate(cols):
        cx = x + 16 + i * (s // 3)
        d.ellipse([cx - 13, y + 12, cx + 13, y + 38], fill=c, outline=INK)
    d.line([(x + 6, y + s - 14), (x + s - 6, y + s - 14)], fill=col, width=5)
    d.line([(x + 16, y + s - 14), (x + 16, y + s - 4)], fill=col, width=3)
    d.line([(x + s - 16, y + s - 14), (x + s - 16, y + s - 4)], fill=col, width=3)


def icon_chart(d, x, y, s, col):
    d.line([(x + 8, y + s - 12), (x + s - 6, y + s - 12)], fill=col, width=3)
    d.line([(x + 8, y + s - 12), (x + 8, y + 10)], fill=col, width=3)
    bars = [14, 22, 18, 30, 40]
    for i, bh in enumerate(bars):
        bx = x + 16 + i * 13
        d.rectangle([bx, y + s - 14 - bh, bx + 8, y + s - 14], fill=NAVY)
    d.line([(x + 12, y + 26), (x + 30, y + 18), (x + 46, y + 20), (x + s - 8, y + 6)],
           fill=RED, width=4)
    d.polygon([(x + s - 14, y + 2), (x + s - 2, y + 6), (x + s - 12, y + 14)], fill=RED)


def icon_missile(d, x, y, s, col):
    d.polygon([(x + 4, y + s - 8), (x + s // 2, y + 4), (x + s - 4, y + s - 8)], fill=col)
    d.rectangle([x + s // 2 - 3, y + s - 8, x + s // 2 + 3, y + s - 2], fill=RED)


def icon_bridge(d, x, y, s, col):
    d.arc([x + 2, y + 6, x + s - 2, y + s - 4], 180, 360, fill=col, width=3)
    d.line([(x + 2, y + s - 8), (x + s - 2, y + s - 8)], fill=col, width=3)
    d.line([(x + s // 4, y + s // 2), (x + s // 4, y + s - 8)], fill=col, width=2)
    d.line([(x + 3 * s // 4, y + s // 2), (x + 3 * s // 4, y + s - 8)], fill=col, width=2)


def icon_virus(d, x, y, s, col):
    cx, cy = x + s // 2, y + s // 2
    for dx, dy in [(-11, 0), (11, 0), (0, -11), (0, 11), (-8, -8), (8, -8),
                   (-8, 8), (8, 8)]:
        d.line([(cx, cy), (cx + dx, cy + dy)], fill=col, width=3)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=col)


def icon_debt(d, x, y, s, col):
    d.text((x + 2, y + 1), "%", font=F_BOLD(26), fill=col)
    d.line([(x + 4, y + s - 4), (x + s - 4, y + 4)], fill=RED, width=3)


def icon_plane(d, x, y, s, col):
    d.polygon([(x + s // 6, y + 2 * s // 3), (x + 9 * s // 10, y + s // 5),
               (x + 7 * s // 10, y + 9 * s // 10), (x + s // 2, y + 7 * s // 10)], fill=col)


def icon_game(d, x, y, s, col):
    d.rounded_rectangle([x + 4, y + 6, x + s - 4, y + s - 6], 6, outline=col, width=3)
    d.line([(x + 9, y + s // 2), (x + 15, y + s // 2)], fill=col, width=3)
    d.line([(x + 12, y + s // 2 - 3), (x + 12, y + s // 2 + 3)], fill=col, width=3)
    d.ellipse([x + s - 13, y + s // 2 - 5, x + s - 9, y + s // 2 - 1], fill=RED)
    d.ellipse([x + s - 9, y + s // 2 + 1, x + s - 5, y + s // 2 + 5], fill=RED)


def icon_crowd(d, x, y, s, col):
    for cx in (x + 8, x + s // 2, x + s - 8):
        d.ellipse([cx - 4, y + 4, cx + 4, y + 12], fill=col)
        d.line([(cx, y + 14), (cx, y + 24)], fill=col, width=3)
        d.line([(cx - 6, y + 19), (cx + 6, y + 19)], fill=col, width=2)
    d.line([(x + 4, y + s - 4), (x + s - 4, y + s - 4)], fill=RED, width=3)


def icon_strike(d, x, y, s, col):
    d.ellipse([x + 3, y + 3, x + s - 3, y + s - 3], outline=col, width=3)
    d.text((x + s // 2 - 4, y + 5), "!", font=F_BOLD(22), fill=RED)


def icon_vote(d, x, y, s, col):
    d.rectangle([x + 8, y + 12, x + s - 8, y + s - 8], outline=col, width=3)
    d.line([(x + 14, y + 32), (x + 24, y + 42), (x + 44, y + 18)], fill=RED, width=5)


ICONS = {
    "scales": icon_scales, "summit": icon_summit, "chart": icon_chart,
    "missile": icon_missile, "bridge": icon_bridge, "virus": icon_virus,
    "debt": icon_debt, "plane": icon_plane, "game": icon_game,
    "crowd": icon_crowd, "strike": icon_strike, "vote": icon_vote,
}


# ---------------------------------------------------------------- sections
def masthead(d):
    centre(d, 8, stories.MASTHEAD_TITLE, F_TITLE(50), INK)
    d.rectangle([0, 62, W, 102], fill=RED)
    centre(d, 68, stories.DATE_LINE, F_BOLD(32), LIGHT)
    centre(d, 108, stories.SUBHEAD, F_BODY(17), MUTED)


def stats_strip(d):
    top, bot = 128, 180
    d.line([(0, top), (W, top)], fill=GREY, width=2)
    d.line([(0, bot), (W, bot)], fill=GREY, width=2)
    cw = W // 4
    for i, (num, label) in enumerate(stories.STATS):
        x = i * cw
        if i:
            d.line([(x, top + 6), (x, bot - 6)], fill=GREY, width=2)
        nw = d.textlength(num, font=F_BOLD(28))
        d.text((x + (cw - nw) / 2, 134), num, font=F_BOLD(28),
               fill=NAVY if i % 2 == 0 else RED)
        tw = d.textlength(label, font=F_BOLD(13))
        d.text((x + (cw - tw) / 2, 164), label, font=F_BOLD(13), fill=MUTED)


def features(d):
    top, bot = 180, 478
    cols = [(14, 324), (350, 324), (686, 324)]
    for (x, w), feat in zip(cols, stories.FEATURES):
        d.rectangle([x, top + 6, x + w, bot - 4], outline=GREY, width=2)
        d.rectangle([x, top + 6, x + w, top + 118], fill=CREAM)
        ICONS[feat["icon"]](d, x + w // 2 - 30, top + 22, 60, NAVY)
        num = str(feat["num"])
        d.ellipse([x + 12, top + 128, x + 52, top + 168], fill=RED)
        nw = d.textlength(num, font=F_BOLD(24))
        d.text((x + 32 - nw / 2, top + 134), num, font=F_BOLD(24), fill=LIGHT)
        y = draw_wrapped(d, x + 62, top + 130, feat["headline"],
                         F_BOLD(19), w - 74, INK, leading=2)
        y = draw_wrapped(d, x + 14, y + 10, feat["body"],
                         F_BODY(14), w - 28, INK, leading=2)
        d.text((x + 14, bot - 26), feat["place"], font=F_BOLD(12), fill=RED)


def tiles(d):
    top = 478
    xs = [14, 266, 518, 770]
    tw, th = 242, 161
    for row in range(2):
        for col in range(4):
            tile = stories.TILES[row * 4 + col]
            x, y = xs[col], top + row * th
            d.rectangle([x, y, x + tw, y + th], outline=GREY, width=1)
            d.text((x + 10, y + 8), str(tile["num"]), font=F_BOLD(20), fill=RED)
            ICONS[tile["icon"]](d, x + tw - 42, y + 4, 32, NAVY)
            yy = draw_wrapped(d, x + 10, y + 40, tile["headline"],
                              F_BOLD(16), tw - 20, INK, leading=1)
            yy = draw_wrapped(d, x + 10, yy + 5, tile["body"],
                              F_BODY(13), tw - 20, INK, leading=2)
            d.text((x + 10, y + th - 20), tile["place"], font=F_BOLD(11), fill=MUTED)


def bottom(d):
    top, bot = 800, 958
    d.line([(0, top), (W, top)], fill=GREY, width=2)
    d.text((14, top + 10), "ALSO ON 20 NOVEMBER", font=F_BOLD(17), fill=NAVY)
    y = top + 38
    for item in stories.ALSO_ON:
        d.ellipse([18, y + 6, 26, y + 14], fill=RED)
        y = draw_wrapped(d, 34, y, item, F_BODY(15), 520, INK, leading=3)
        y += 4
    brief = stories.BRIEFS[0]
    d.text((18, y), "%d." % brief["num"], font=F_BOLD(15), fill=RED)
    d.text((50, y), "US Senate passes energy bill 62\u201333",
           font=F_BOLD(15), fill=INK)
    d.rectangle([580, top + 8, 1010, bot - 8], outline=GREY, width=2)
    d.rectangle([580, top + 8, 1010, top + 40], fill=NAVY)
    d.text((594, top + 13), "WHERE IT HAPPENED", font=F_BOLD(16), fill=LIGHT)
    for col in range(2):
        xx = 594 + col * 210
        yy = top + 50
        for num, place in stories.PLACES[col * 6:(col + 1) * 6]:
            d.text((xx, yy), "%d. %s" % (num, place), font=F_BODY(14), fill=INK)
            yy += 17


def footer(d):
    d.rectangle([0, 958, W, 964], fill=RED)
    centre(d, 972, stories.FOOTER_MAIN, F_BOLD(17), INK)
    centre(d, 998, stories.FOOTER_SRC, F_BODY(12), MUTED)


def render(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    stats_strip(d)
    features(d)
    tiles(d)
    bottom(d)
    footer(d)
    img.save(out_path, "PNG", optimize=True)
    return out_path


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "poster-20261120.png")
    render(out)
    size = os.path.getsize(out)
    with open(out, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print("poster: %s" % out)
    print("size: %d bytes" % size)
    print("sha256: %s" % digest)


if __name__ == "__main__":
    main()
