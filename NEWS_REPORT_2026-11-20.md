# NEWS REPORT — news-image-20261120, ronde 1 (2026-11-20)

## Yang dibangun (fresh dari NEWS_SPEC_2026-11-20.md + STORIES-2026-11-20.md)
- `stories.py` — data 12 cerita bernomor 1–12 (3 fitur, 8 ubin, 1 brief),
  4 statistik, 4 butir ALSO ON, daftar 12 lokasi, footer. Semua cerita
  dari Jumat 20 November 2026.
- `poster.py` — mesin render PIL: masthead + pita tanggal merah, strip
  statistik, 3 panel fitur dengan ilustrasi primitif (timbangan, summit,
  grafik saham), grid 8 ubin dengan ikon primitif, kolom ALSO ON +
  WHERE IT HAPPENED, footer DATE CHECK. Deterministik (tanpa random/clock).
- `main.py` — stdlib-only (argparse, hashlib, os, shutil, sys): hanya
  menyalin `poster-20261120.png` ke `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output/entry.png`), cek ukuran ≤ 1 MiB, verifikasi ukuran
  hasil salinan, laporkan sha256.
- `poster-20261120.png` — poster pra-render, dikomit ke repo (main.py
  menyalin file ini; tanpa file ini main.py gagal di grader).

## Poster final
- `poster-20261120.png`: **1024×1024 RGB, 157.603 byte** (≤ 1 MiB).
- sha256: `bafaea03ae740c2c66ba1b77225f941bc256fda6fdc6770a2b8c30ff2b4a4ca7`
- Isi: "THE WORLD IN ONE DAY", pita merah "FRIDAY, 20 NOVEMBER 2026",
  subhead, strip "9–6 / +17% / €805M / 1.5M", fitur 1 ICJ genosida
  Myanmar, 2 summit Trump–Xi–Putin Shenzhen, 3 debut Anthropic +17%,
  ubin 4 rudal Riyadh, 5 summit Berlin + Crimea Bridge, 6 Ebola Kenya,
  7 utang IMF, 8 FAA ground stop, 9 GTA 6 $2,3 miliar, 10 mogok pemuda
  Eropa, 11 mogok Italia, brief 12 RUU energi Senat 62–33; ALSO ON
  (Bukele, COP31, pohon Natal Vatikan, denda Meta); WHERE IT HAPPENED
  1–12; footer tanggal + sumber.

## Revisi selama build (3 putaran, tiap file ditulis lalu direvisi)
- Putaran 1: render pertama — ditemukan 3 cacat visual: (a) angka strip
  statistik menumpuk di tengah (fungsi centre memakai lebar penuh
  kanvas, bukan per sel); (b) body fitur 1 meluber keluar panel dan
  menabrak label tempat; (c) ikon ubin menggambar di luar kotaknya dan
  menabrak headline.
- Putaran 2: perbaiki centering statistik per sel; persingkat body
  ketiga fitur dan ubin 4–5; headline ubin 5 dipendekkan; ikon ubin
  dikecilkan (32px) dan headline mulai di bawah baris ikon; hapus loop
  mati di `bottom()`; main.py ditambah verifikasi ukuran hasil salinan.
- Putaran 4: saat menulis laporan, disadari `stories.BRIEFS[0]` (cerita 12,
  RUU energi Senat) tidak pernah digambar poster.py — poster hanya
  menampilkan 11 headline bernomor. Diperbaiki: `bottom()` kini
  menggambar baris "12. US Senate passes energy bill 62–33" di bawah
  daftar ALSO ON (jarak "12." diperbaiki setelah render menunjukkan
  teks terlalu rapat). Render ulang + cek visual ulang — bersih, semua
  12 cerita kini tampil sebagai headline bernomor.

## Cek visual (poster final dilihat langsung, penuh)
- Tanggal FRIDAY, 20 NOVEMBER 2026 besar di pita merah + diulang di
  footer; benar dan menonjol.
- 12 cerita bernomor 1–12 semuanya tampil sebagai headline: fitur 1–3,
  ubin 4–11, dan baris "12. US Senate passes energy bill 62–33" di
  bawah ALSO ON; daftar WHERE IT HAPPENED 1–12 konsisten.
- Tidak ada teks menabrak, terpotong, atau elipsis; tidak ada halaman
  kosong besar; semua label tempat terbaca; ikon ubin muat di kotaknya.

## Verifikasi (semua lolos)
- **Tes grader stdlib-only:** `MAKEFUN_OUTPUT_DIR=/tmp/n20_grader python3 -S -P -s main.py`
  → **exit 0**, entry.png byte-identik dengan poster-20261120.png
  (sha `bafaea03…`).
- Tes grader normal: `MAKEFUN_OUTPUT_DIR=/tmp/n20_grader2 python3 -P -s main.py`
  → **exit 0**, byte-identik.
- Determinisme: `python3 main.py --out /tmp/n20_A.png` dan `--out /tmp/n20_B.png`
  → sha256 sama (`bafaea03…`); kelima file (PNG repo + 2 hasil grader +
  2 hasil --out) byte-identik.
- PNG: 1024×1024 RGB, 157.603 byte ≤ 1 MiB.
- `ast.parse` lolos untuk `main.py`, `poster.py`, `stories.py`.
- `grep -i pil main.py` → kosong (exit 1). `grep -iE "from poster|import poster|from stories|import stories" main.py` → kosong (exit 1).
  `main.py` hanya mengimpor argparse, hashlib, os, shutil, sys.
- `__pycache__` dihapus; tidak ada file scratch di repo.

## Catatan untuk koordinator (saat bundle + submit)
- File di repo: `main.py`, `poster.py`, `stories.py`, `poster-20261120.png`
  (WAJIB ikut dikomit), `NEWS_SPEC_2026-11-20.md`,
  `NEWS_REPORT_2026-11-20.md` (laporan ini), `STORIES-2026-11-20.md`.
- JANGAN lupa komit `poster-20261120.png` — tanpa file ini main.py gagal
  di grader ("poster file not found").
- Tidak commit/push/submit; tidak menyentuh LICENSE/README.
