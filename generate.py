#!/usr/bin/env python3
"""Render entry.png: one image summing up the world news of Tuesday 17 Nov 2026.

Build script only -- the grader runs main.py, not this file.
Run:  python3 generate.py   (writes entry.png next to this script)
Uses Pillow + Noto Sans (system fonts). No network.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
NAVY = (16, 36, 62)        # header band
GOLD = (232, 184, 75)      # accent / kicker
INK = (18, 28, 40)         # headline text
BODY = (58, 68, 80)        # summary text
CELL = (244, 246, 248)     # story cell background
WHITE = (255, 255, 255)
FOOT = (120, 130, 140)     # footer text

FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_tracked(draw, cx, y, text, fnt, fill, tracking=5):
    """Draw text centered on cx with letter tracking."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking


def fit_font(draw, text, path, start_size, max_w):
    """Largest font size (<= start_size) at which text fits max_w."""
    size = start_size
    while size > 10:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, 10)


STORIES = [
    ("MIDDLE EAST", (169, 50, 38),
     "U.S. and Iran trade fire in the Gulf",
     "U.S. jets hit an IRGC missile site on Qeshm Island after Iran fired "
     "drones at a U.S. radar in Bahrain \u2014 its third attack there in five days."),
    ("UKRAINE", (26, 82, 118),
     "Kerch Bridge hit again; span falls",
     "Ukrainian drones struck the Crimea bridge a second day; a road section "
     "fell into the strait. Russia hit bridges in Kyiv in reply."),
    ("MARKETS", (125, 60, 152),
     "Stocks and oil slide worldwide",
     "Brent crude fell 3.6% to $92.44; the Nasdaq entered correction, "
     "down over 10% from its October peak."),
    ("TECH", (14, 102, 85),
     "Nvidia doubles sales to $115.8bn",
     "Revenue rose 103% in its first quarter since CEO Jensen Huang resigned; "
     "the board says it will not reinstate him."),
    ("DIPLOMACY", (126, 81, 9),
     "Trump in Manila, then on to China",
     "The U.S. president joined Quad talks in Manila and heads to Shenzhen "
     "for APEC with Xi and Putin; he may meet Kim Jong Un."),
    ("CLIMATE", (30, 132, 73),
     "COP31 draft urges faster fossil exit",
     "A draft deal at the climate summit calls for \u2018accelerated action\u2019 "
     "to phase out fossil fuels."),
]


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    # ---- header band ----
    d.rectangle([0, 0, W, 170], fill=NAVY)
    draw_tracked(d, W // 2, 26, "WORLD NEWS IN ONE IMAGE",
                 font(FONT_BOLD, 22), GOLD, tracking=6)
    date_font = fit_font(d, "TUESDAY 17 NOVEMBER 2026", FONT_BOLD, 58, W - 56)
    d.text((W // 2, 62), "TUESDAY 17 NOVEMBER 2026",
           font=date_font, fill=WHITE, anchor="ma")
    d.rectangle([0, 170, W, 174], fill=GOLD)

    # ---- story grid: 2 cols x 3 rows ----
    margin, gutter = 28, 20
    cell_w = (W - 2 * margin - gutter) // 2          # 474
    cell_h = 250
    top = 194
    text_w = cell_w - 36
    tag_font = font(FONT_BOLD, 18)
    head_font = font(FONT_BOLD, 27)
    body_font = font(FONT_REG, 20)

    for i, (tag, color, headline, summary) in enumerate(STORIES):
        row, col = divmod(i, 2)
        x = margin + col * (cell_w + gutter)
        y = top + row * (cell_h + gutter)

        d.rounded_rectangle([x, y, x + cell_w, y + cell_h], radius=10, fill=CELL)
        d.rectangle([x, y + 10, x + 6, y + cell_h - 10], fill=color)

        # tag pill
        tag_w = d.textlength(tag, font=tag_font) + 22
        d.rounded_rectangle([x + 18, y + 16, x + 18 + tag_w, y + 46],
                            radius=15, fill=color)
        d.text((x + 18 + tag_w / 2, y + 31), tag, font=tag_font,
               fill=WHITE, anchor="mm")

        # headline (max 2 lines)
        lines = wrap(d, headline, head_font, text_w)[:2]
        hy = y + 62
        for ln in lines:
            d.text((x + 18, hy), ln, font=head_font, fill=INK)
            hy += 34

        # summary (max 3 lines)
        slines = wrap(d, summary, body_font, text_w)[:3]
        sy = hy + 10
        for ln in slines:
            d.text((x + 18, sy), ln, font=body_font, fill=BODY)
            sy += 27

    # ---- footer ----
    d.text((W // 2, 1000), "Compiled from major wire reports  \u00b7  17 November 2026",
           font=font(FONT_REG, 16), fill=FOOT, anchor="mm")

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, img.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
