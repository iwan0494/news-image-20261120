# news-image-20261120 — Sum up 20 November's world news in one image

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/iwan0494/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/iwan0494/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for the [make.fun](https://make.fun/bounty/news-image-20261120) bounty `news-image-20261120`: a program that writes one image
summarising the world's news of Friday 20 November 2026 to `/output/entry.png`.

The image is a newspaper front page (1024x1024 PNG): the ICJ's 9–6 genocide
ruling against Myanmar, the first Trump–Xi–Putin three-way summit in Shenzhen,
and Anthropic's +17% Nasdaq debut lead the page, followed by the Houthi missile
that hit Riyadh's tallest tower, the Berlin Ukraine summit and the Crimea Bridge
hit, Kenya's last Ebola patient, the IMF debt warning, the FAA ground stop,
GTA 6's $2.3 billion launch, and strikes across Europe and Italy — twelve
stories from one Friday, with the date printed large.

## How it works

`main.py` (Python 3.13, standard library only) copies the image the repository
holds (`poster-20261120.png`) to `/output/entry.png`. The copy is deterministic:
both runs write the same bytes. No network is used.

## Files

- `main.py` — the entry program
- `poster-20261120.png` — the image (1024x1024, 157,603 bytes)
- `poster.py` — the script that rendered the poster (PIL, deterministic)
- `stories.py` — the twelve stories and their data
- `LICENSE` — MIT
