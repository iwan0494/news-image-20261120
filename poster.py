# Poster renderer for the 20 November 2026 world-news poster (round 2).
# Reads stories.py, draws a dense 1024x1024 newspaper front page with
# PIL primitives only (no photos, no network, no random, no clock).

import os

from PIL import Image, ImageDraw, ImageFont

import stories

W = 1024
H = 1024
MARGIN = 16

NAVY = (15, 42, 68)
PAPER = (250, 246, 236)
INK = (22, 22, 22)
RED = (192, 57, 43)
TEAL = (14, 124, 107)
GREY = (122, 120, 114)
LIGHT = (238, 232, 216)
CARD = (255, 252, 244)
GOLD = (201, 162, 39)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
_fonts = {}


def font(bold, size):
    key = (bold, size)
    if key not in _fonts:
        name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
        _fonts[key] = ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    return _fonts[key]


def wrap(text, fnt, max_w, max_lines):
    """Greedy word wrap measured in pixels; raises if it cannot fit."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if not cur:
                raise ValueError("single word too wide: %r" % word)
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        raise ValueError("text overflows %d lines: %r" % (max_lines, text))
    return lines


def draw_lines(d, lines, x, y, fnt, color, leading):
    for line in lines:
        d.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def draw_badge(d, cx, cy, r, text, fill, fnt):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    w = fnt.getlength(text)
    d.text((cx - w / 2, cy - fnt.size / 2 - 1), text, font=fnt, fill=WHITE)


# ---------------------------------------------------------------- icons

def icon_missile(d, x, y, s, c):
    d.polygon([(x + s * 0.5, y), (x + s * 0.85, y + s * 0.55),
               (x + s * 0.5, y + s * 0.4), (x + s * 0.15, y + s * 0.55)],
              fill=c)
    for i in range(3):
        d.line([(x + s * 0.2 + i * s * 0.18, y + s * 0.62),
                (x + s * 0.1 + i * s * 0.18, y + s * 0.95)], fill=c, width=2)


def icon_draft(d, x, y, s, c):
    d.rectangle([x + s * 0.2, y + s * 0.05, x + s * 0.8, y + s * 0.95],
                outline=c, width=2)
    for i in range(3):
        yy = y + s * (0.25 + i * 0.2)
        d.line([(x + s * 0.3, yy), (x + s * 0.7, yy)], fill=c, width=2)
    d.line([(x + s * 0.7, y + s * 0.7), (x + s * 0.85, y + s * 0.85)],
           fill=RED, width=3)


def icon_down(d, x, y, s, c):
    pts = [(x + s * 0.1, y + s * 0.25), (x + s * 0.4, y + s * 0.45),
           (x + s * 0.55, y + s * 0.3), (x + s * 0.9, y + s * 0.6)]
    d.line(pts, fill=c, width=3)
    d.polygon([(x + s * 0.9, y + s * 0.6), (x + s * 0.72, y + s * 0.5),
               (x + s * 0.82, y + s * 0.78)], fill=c)


def icon_up(d, x, y, s, c):
    pts = [(x + s * 0.1, y + s * 0.75), (x + s * 0.4, y + s * 0.55),
           (x + s * 0.55, y + s * 0.7), (x + s * 0.9, y + s * 0.4)]
    d.line(pts, fill=c, width=3)
    d.polygon([(x + s * 0.9, y + s * 0.4), (x + s * 0.72, y + s * 0.5),
               (x + s * 0.82, y + s * 0.22)], fill=c)


def icon_tower(d, x, y, s, c):
    d.rectangle([x + s * 0.35, y + s * 0.25, x + s * 0.65, y + s * 0.95],
                fill=c)
    d.rectangle([x + s * 0.2, y + s * 0.45, x + s * 0.8, y + s * 0.55],
                fill=c)
    d.line([(x + s * 0.5, y + s * 0.05), (x + s * 0.5, y + s * 0.25)],
           fill=c, width=2)
    d.ellipse([x + s * 0.44, y, x + s * 0.56, y + s * 0.12], fill=RED)


def icon_bridge(d, x, y, s, c):
    d.arc([x, y + s * 0.3, x + s, y + s * 1.1], 180, 360, fill=c, width=3)
    d.line([(x, y + s * 0.55), (x + s, y + s * 0.55)], fill=c, width=3)
    for fx in (0.2, 0.5, 0.8):
        d.line([(x + s * fx, y + s * 0.32), (x + s * fx, y + s * 0.55)],
               fill=c, width=2)


def icon_virus(d, x, y, s, c):
    cx, cy, r = x + s * 0.5, y + s * 0.5, s * 0.26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    for k in range(8):
        import math
        a = k * math.pi / 4
        x1 = cx + r * 0.9 * math.cos(a)
        y1 = cy + r * 0.9 * math.sin(a)
        x2 = cx + r * 1.5 * math.cos(a)
        y2 = cy + r * 1.5 * math.sin(a)
        d.line([(x1, y1), (x2, y2)], fill=c, width=2)


def icon_percent(d, x, y, s, c):
    d.text((x, y - 2), "%", font=font(True, int(s * 0.95)), fill=c)


def icon_plane(d, x, y, s, c):
    d.polygon([(x + s * 0.5, y + s * 0.05), (x + s * 0.62, y + s * 0.5),
               (x + s * 0.95, y + s * 0.65), (x + s * 0.62, y + s * 0.68),
               (x + s * 0.55, y + s * 0.95), (x + s * 0.45, y + s * 0.95),
               (x + s * 0.38, y + s * 0.68), (x + s * 0.05, y + s * 0.65),
               (x + s * 0.38, y + s * 0.5)], fill=c)


def icon_game(d, x, y, s, c):
    d.rounded_rectangle([x + s * 0.05, y + s * 0.2, x + s * 0.95, y + s * 0.8],
                        radius=5, outline=c, width=2)
    d.line([(x + s * 0.3, y + s * 0.5), (x + s * 0.45, y + s * 0.5)],
           fill=c, width=2)
    d.line([(x + s * 0.375, y + s * 0.42), (x + s * 0.375, y + s * 0.58)],
           fill=c, width=2)
    d.ellipse([x + s * 0.6, y + s * 0.42, x + s * 0.68, y + s * 0.5],
              fill=RED)
    d.ellipse([x + s * 0.72, y + s * 0.52, x + s * 0.8, y + s * 0.6],
              fill=RED)


ICONS = {
    "missile": icon_missile, "draft": icon_draft, "down": icon_down,
    "up": icon_up, "tower": icon_tower, "bridge": icon_bridge,
    "virus": icon_virus, "percent": icon_percent, "plane": icon_plane,
    "game": icon_game,
}


# ------------------------------------------------------- lead illustrations

def art_scales(d, x, y, w, h, c):
    cx = x + w // 2
    base = y + h - 10
    d.line([(cx, y + 6), (cx, base)], fill=c, width=3)
    d.line([(x + 18, y + 20), (x + w - 18, y + 20)], fill=c, width=3)
    d.ellipse([cx - 5, y, cx + 5, y + 10], fill=c)
    for sgn in (-1, 1):
        px = cx + sgn * (w // 2 - 30)
        d.line([(px, y + 20), (px, y + 36)], fill=c, width=2)
        d.polygon([(px - 22, y + 36), (px + 22, y + 36), (px, base - 2)],
                  outline=c, width=2)
    d.line([(cx - 26, base), (cx + 26, base)], fill=c, width=3)


def art_summit(d, x, y, w, h, c):
    cols = [RED, GOLD, NAVY]
    table = y + h - 14
    for i, col in enumerate(cols):
        cx = x + w // 2 + (i - 1) * 74
        d.ellipse([cx - 22, y + 4, cx + 22, y + 48], fill=col)
        d.line([(cx, y + 48), (cx, table)], fill=c, width=2)
    d.line([(x + 30, table), (x + w - 30, table)], fill=c, width=3)
    for i in range(3):
        fx = x + w // 2 + (i - 1) * 74
        d.line([(fx, table), (fx, y + h - 4)], fill=c, width=2)


def art_cyclone(d, x, y, w, h, c):
    cx, cy = x + w // 2, y + h // 2 - 8
    max_r = h // 2 - 8
    for r in (max_r, int(max_r * 0.75), int(max_r * 0.5),
              int(max_r * 0.28)):
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300, fill=c, width=3)
    d.polygon([(cx + max_r, cy - 8), (cx + max_r + 14, cy + 2),
               (cx + max_r - 4, cy + 6)], fill=RED)
    d.line([(x + 10, y + h - 10), (x + w - 10, y + h - 10)], fill=TEAL,
           width=3)
    for i in range(5):
        rx = x + 30 + i * 52
        d.line([(rx, y + h - 26), (rx - 4, y + h - 18)], fill=TEAL, width=2)


# ---------------------------------------------------------------- sections

def section_masthead(d, y):
    d.rectangle([0, y, W, y + 58], fill=NAVY)
    d.text((MARGIN, y + 12), "THE WORLD IN ONE DAY",
           font=font(True, 34), fill=WHITE)
    tag = "36 STORIES \u00b7 7 REGIONS"
    tf = font(True, 15)
    tw = tf.getlength(tag) + 24
    d.rectangle([W - MARGIN - tw, y + 14, W - MARGIN, y + 48], fill=RED)
    d.text((W - MARGIN - tw + 12, y + 23), tag, font=tf, fill=WHITE)
    return y + 58


def section_date(d, y):
    d.text((MARGIN, y + 2), "FRIDAY, 20 NOVEMBER 2026",
           font=font(True, 30), fill=NAVY)
    sub = "One Friday, six continents \u2014 courts, summits, storms, markets and war."
    d.text((MARGIN, y + 34), sub, font=font(False, 13), fill=GREY)
    d.line([(MARGIN, y + 50), (W - MARGIN, y + 50)], fill=GREY, width=1)
    return y + 52


def section_rail(d, y):
    x0, x1 = MARGIN + 8, W - MARGIN - 8
    mid = y + 22
    for hr in (0, 6, 12, 18, 24):
        tx = x0 + (x1 - x0) * hr / 24.0
        d.line([(tx, mid - 4), (tx, mid + 4)], fill=GREY, width=2)
        lab = "%02d" % hr
        lf = font(False, 9)
        d.text((tx - lf.getlength(lab) / 2, y + 4), lab, font=lf,
               fill=GREY)
    d.line([(x0, mid), (x1, mid)], fill=GREY, width=2)
    for i, (hour, clock, label) in enumerate(stories.RAIL):
        tx = x0 + (x1 - x0) * hour / 24.0
        d.ellipse([tx - 5, mid - 5, tx + 5, mid + 5], fill=RED)
        tf = font(True, 10)
        full = clock + "  " + label
        tw = tf.getlength(full)
        lx = min(max(tx - tw / 2, MARGIN), W - MARGIN - tw)
        ly = mid + 8 if i != 1 else mid + 22
        d.text((lx, ly), full, font=tf, fill=RED)
    return y + 56


def section_stats(d, y):
    cells = stories.STATS
    cw = (W - 2 * MARGIN) / len(cells)
    for i, (num, lab) in enumerate(cells):
        cx = MARGIN + cw * i + cw / 2
        nf = font(True, 26)
        d.text((cx - nf.getlength(num) / 2, y), num, font=nf,
               fill=RED if i % 2 == 0 else NAVY)
        lf = font(True, 10)
        d.text((cx - lf.getlength(lab) / 2, y + 30), lab, font=lf,
               fill=INK)
        if i:
            d.line([(MARGIN + cw * i, y + 2), (MARGIN + cw * i, y + 40)],
                   fill=GREY, width=1)
    d.line([(MARGIN, y + 44), (W - MARGIN, y + 44)], fill=GREY, width=1)
    return y + 46


def section_leads(d, y):
    h = 216
    pw = (W - 2 * MARGIN - 2 * 10) / 3
    arts = {"scales": art_scales, "summit": art_summit,
            "cyclone": art_cyclone}
    for i, lead in enumerate(stories.LEADS):
        x = MARGIN + i * (pw + 10)
        d.rectangle([x, y, x + pw, y + h], outline=GREY, width=1,
                    fill=CARD)
        ix, iy, iw, ih = x + 12, y + 8, pw - 24, 76
        arts[lead["art"]](d, ix, iy, iw, ih, NAVY)
        ty = y + 94
        draw_badge(d, x + 24, ty + 10, 11, str(lead["num"]), RED,
                   font(True, 13))
        hf = font(True, 16)
        lines = wrap(lead["head"], hf, pw - 24, 2)
        hy = ty
        draw_lines(d, lines, x + 42, hy, hf, INK, 19)
        by = ty + 44
        bf = font(False, 12)
        blines = wrap(lead["body"], bf, pw - 24, 3)
        draw_lines(d, blines, x + 12, by, bf, INK, 15)
        tag = lead["src"] + "  \u00b7  " + lead["region"]
        d.text((x + 12, y + h - 22), tag, font=font(True, 10), fill=TEAL)
    return y + h


def section_cards(d, y):
    rows, cols = 2, 5
    ch = 120
    cw = (W - 2 * MARGIN - (cols - 1) * 8) / cols
    for idx, card in enumerate(stories.CARDS):
        r, c = divmod(idx, cols)
        x = MARGIN + c * (cw + 8)
        cy = y + r * (ch + 8)
        d.rectangle([x, cy, x + cw, cy + ch], outline=GREY, width=1,
                    fill=CARD)
        draw_badge(d, x + 18, cy + 16, 10, str(card["num"]), RED,
                   font(True, 12))
        ICONS[card["icon"]](d, x + cw - 34, cy + 5, 26, NAVY)
        hf = font(True, 12)
        lines = wrap(card["head"], hf, cw - 18, 2)
        draw_lines(d, lines, x + 9, cy + 32, hf, INK, 15)
        bf = font(False, 11)
        blines = wrap(card["body"], bf, cw - 18, 3)
        draw_lines(d, blines, x + 9, cy + 64, bf, INK, 13)
        tag = card["src"] + "  \u00b7  " + card["region"]
        d.text((x + 9, cy + ch - 16), tag, font=font(True, 9), fill=TEAL)
    return y + rows * ch + (rows - 1) * 8


def mixed_lines(segments, max_w, max_lines):
    """Wrap (word, font) segments into at most max_lines lines of
    (word, font) pairs, measured in pixels."""
    words = []
    for text, fnt in segments:
        for w in text.split():
            words.append((w, fnt))
    lines, cur, cur_w = [], [], 0
    space_w = font(False, 11).getlength(" ")
    for w, fnt in words:
        ww = fnt.getlength(w)
        add = ww if not cur else ww + space_w
        if cur_w + add <= max_w:
            cur.append((w, fnt))
            cur_w += add
        else:
            if not cur:
                raise ValueError("word too wide: %r" % w)
            lines.append(cur)
            cur, cur_w = [(w, fnt)], ww
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        raise ValueError("brief overflows %d lines" % max_lines)
    return lines


def draw_mixed(d, lines, x, y, leading):
    for line in lines:
        cx = x
        space_w = font(False, 11).getlength(" ")
        for j, (w, fnt) in enumerate(line):
            if j:
                cx += space_w
            d.text((cx, y), w, font=fnt, fill=INK)
            cx += fnt.getlength(w)
        y += leading
    return y


def section_briefs(d, y):
    d.text((MARGIN, y), "MORE ON 20 NOVEMBER",
           font=font(True, 13), fill=NAVY)
    d.line([(MARGIN + 190, y + 8), (W - MARGIN, y + 8)], fill=GREY,
           width=1)
    top = y + 18
    cols = 3
    per = [8, 8, 7]
    col_w = (W - 2 * MARGIN - (cols - 1) * 16) / cols
    entry_h = 25
    start = 0
    for c in range(cols):
        x = MARGIN + c * (col_w + 16)
        for k in range(per[c]):
            num, head, body, src, region = stories.BRIEFS[start + k]
            ey = top + k * entry_h
            segs = [
                ("%d. %s" % (num, head), font(True, 11)),
                (body, font(False, 11)),
                ("[%s \u00b7 %s]" % (region, src), font(True, 9)),
            ]
            lines = mixed_lines(segs, col_w, 2)
            draw_mixed(d, lines, x, ey, 13)
        start += per[c]
    return top + 8 * entry_h


def section_map(d, y):
    d.text((MARGIN, y), "WHERE IT HAPPENED",
           font=font(True, 13), fill=NAVY)
    my = y + 20
    mw, mh = 620, 72
    d.rectangle([MARGIN, my, MARGIN + mw, my + mh], fill=LIGHT,
                outline=GREY, width=1)
    blobs = [
        (28, 18, 150, 58), (210, 8, 130, 52), (330, 22, 170, 48),
        (500, 30, 100, 40),
    ]
    for bx, by, bw, bh in blobs:
        d.ellipse([MARGIN + bx, my + by, MARGIN + bx + bw,
                   my + by + bh], fill=(214, 226, 220))
    for num, dx, dy in stories.MAP_DOTS:
        cx, cy = MARGIN + dx, my + dy
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED)
        tf = font(True, 9)
        t = str(num)
        d.text((cx - tf.getlength(t) / 2, cy - 5), t, font=tf,
               fill=WHITE)
    lx = MARGIN + mw + 16
    lw = W - MARGIN - lx
    half = (len(stories.MAP_PLACES) + 1) // 2
    for col in range(2):
        cx = lx + col * (lw / 2)
        for j, (num, place) in enumerate(
                stories.MAP_PLACES[col * half:(col + 1) * half]):
            yy = my + 1 + j * 10
            d.text((cx, yy), "%d. %s" % (num, place),
                   font=font(False, 10), fill=INK)
    return my + mh


def section_footer(d, y):
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=RED, width=3)
    msg = ("FRIDAY 20 NOVEMBER 2026 \u2014 All 36 stories happened or were "
           "first reported on this day.")
    mf = font(True, 12)
    d.text((W / 2 - mf.getlength(msg) / 2, y + 6), msg, font=mf,
           fill=INK)
    src = "Sources: BBC, Reuters, IMD, UN News, Japan Times, wires."
    sf = font(False, 10)
    d.text((W / 2 - sf.getlength(src) / 2, y + 22), src, font=sf,
           fill=GREY)
    return y + 36


def build_poster(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    y = 0
    y = section_masthead(d, y)
    y = section_date(d, y)
    y = section_rail(d, y)
    y = section_stats(d, y)
    y = section_leads(d, y)
    y = section_cards(d, y)
    y = section_briefs(d, y)
    y = section_map(d, y)
    y = section_footer(d, y)
    if y > H:
        raise ValueError("layout overflows canvas: y=%d" % y)
    img.save(out_path)
    return out_path


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    build_poster(os.path.join(here, "poster-20261120.png"))
    print("poster written")
