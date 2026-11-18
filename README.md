# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/lianyongmin-afk/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/lianyongmin-afk/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world news of Tuesday 17 November 2026. Entry for the [make.fun](https://make.fun/bounty/news-image-20261117) bounty "Sum up 17 November's world news in one image" ($250 in USDC).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=7hwn368j&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>

---

## What the image covers

`entry.png` (1024x1024) sums up Tuesday 17 November 2026 in six stories,
researched from wire reports published that day:

1. **Middle East** — U.S. jets struck an IRGC missile site on Qeshm Island after Iran fired drones at a U.S. radar in Bahrain, its third attack there in five days.
2. **Ukraine** — Ukrainian drones hit the Kerch Bridge a second day; a road section fell into the strait, and Russia hit bridges in Kyiv in reply.
3. **Markets** — Brent crude fell 3.6% to $92.44; the Nasdaq entered correction, down over 10% from its October peak.
4. **Tech** — Nvidia's revenue rose 103% to $115.8bn in its first quarter since CEO Jensen Huang resigned; the board says it will not reinstate him.
5. **Diplomacy** — Trump joined Quad talks in Manila and heads to Shenzhen for APEC with Xi and Putin; he may meet Kim Jong Un.
6. **Climate** — A COP31 draft deal calls for "accelerated action" to phase out fossil fuels.

## How it was built

The image is rendered with Pillow (Noto Sans) by `generate.py`, so every
headline is pixel-crisp text, never AI-generated imagery. `main.py` (Python
3.13, stdlib only, no network) copies the finished `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`, verifying the copy is byte-identical.
