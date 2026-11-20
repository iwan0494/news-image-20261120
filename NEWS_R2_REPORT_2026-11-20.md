# NEWS R2 REPORT — news-image-20261120, ronde 2 (2026-11-20)

## Perubahan vs ronde 1 (diagnosis)
- R1: 97,47% (10W 2D 0L), rank 1.392/8.619, 12 cerita; cutoff top-50 ~98,82%.
  Top 10 semuanya 33–38 cerita + ilustrasi gambar tangan + sourced/tagged +
  UTC stamps + date rail + peta. R2 meniru pola pemenang itu.
- R2: **36 cerita** (3 lead ilustrasi besar + 10 kartu bergambar + 23 briefs),
  7 region, setiap cerita bertag sumber + region, date rail UTC dengan 4
  penanda terverifikasi (02:00 Akvan, 03:19 Senate, 06:00 Nikkei, 21:00
  Anthropic), strip statistik 6 angka, peta "WHERE IT HAPPENED" dengan titik
  bernomor 1–13 + daftar lokasi. Palet baru (navy #0F2A44, kertas #FAF6EC,
  merah #C0392B, teal #0E7C6B), struktur kode baru, mesin layout kursor-y.

## Yang ditulis (fresh, file R1 dihapus pakai `rm` tanpa dibaca dulu)
- **Putaran 1:** `stories.py` (LEADS 3, CARDS 10, BRIEFS 23, STATS 6, RAIL 4,
  MAP_DOTS + MAP_PLACES), `poster.py` (mesin render: masthead, date band,
  rail UTC, stats, leads, cards, briefs mixed-font, map, footer; 10 ikon
  primitif + 3 ilustrasi lead), `main.py` (copy stdlib-only).
  Render pertama gagal: headline kartu 9 meluber 2 baris + total layout
  1066 px > 1024.
- **Putaran 2 (revisi):** headline kartu 9 dipendekkan; tinggi tiap seksi
  dipangkas (masthead 62→58, date 56→48, stats 50→46, leads 252→232,
  kartu 124→120, briefs 228→218); `main.py` direvisi (`--out` langsung
  copy ke path file). Render ke-2 gagal: 8 brief meluber 2 baris.
- **Putaran 3 (revisi):** 8 body brief dipendekkan (fakta sama). Render ke-3
  berhasil (sha `e0ca0911…`), tapi cek visual menemukan cacat: label rail
  "di atas garis" menabrak subhead, dan daftar lokasi peta terpotong footer.
- **Putaran 4 (revisi):** rail ditulis ulang (angka jam di atas garis, label
  penanda di bawah garis 2 baris berselang); date band diberi ruang
  (tanggal y+2, subhead y+34, garis y+50); leads 224→216 dengan ilustrasi
  `art_scales`/`art_summit`/`art_cyclone` dibuat relatif terhadap tinggi;
  daftar lokasi peta leading 11→10. Render ke-4 final, cek visual bersih.

## Poster final
- `poster-20261120.png`: **1024×1024 RGB, 208.149 byte** (≤ 1 MiB).
- sha256: `461320e5d6130f54030f44c698a589e820f45ca7a23137688dab2ee4d6ff84c0`
- Saya lihat langsung (penuh, 2x render): masthead navy + badge merah
  "36 STORIES · 7 REGIONS"; "FRIDAY, 20 NOVEMBER 2026" besar dan benar;
  rail UTC dengan 4 penanda; 6 angka statistik; 3 lead (timbangan, summit,
  siklon); 10 kartu bernomor 4–13 dengan ikon; 23 briefs bernomor 14–36
  semua tampil; peta + daftar lokasi 1–13 lengkap; footer DATE CHECK.
  **Tidak ada teks menabrak, terpotong, atau elipsis; tidak ada halaman
  kosong besar; penomoran 1–36 konsisten.**

## Verifikasi (semua lolos)
- **Tes grader stdlib-only (PALING PENTING):**
  `MAKEFUN_OUTPUT_DIR=/tmp/n20r2_grader python3 -S -P -s main.py` → **exit 0**,
  entry.png byte-identik dengan `poster-20261120.png` (sha `461320e5…`).
- Tes grader normal: `MAKEFUN_OUTPUT_DIR=/tmp/n20r2_grader2 python3 -P -s main.py`
  → **exit 0**, byte-identik.
- Determinisme: 2 run `--out` + 2 run grader → kelima file sha256 sama
  (`461320e5…`).
- `ast.parse` lolos untuk `main.py`, `poster.py`, `stories.py`.
- `grep -i pil main.py` → kosong (exit 1).
  `grep -iE "from poster|import poster|from stories|import stories" main.py`
  → kosong (exit 1). `main.py` hanya mengimpor argparse, hashlib, os,
  shutil, sys.
- `__pycache__` dihapus; file scratch hanya di /tmp.

## Catatan untuk koordinator (saat bundle + submit)
- File baru/berubah di repo: `main.py` (baru, copy stdlib-only), `poster.py`
  (baru), `stories.py` (baru), `poster-20261120.png` (baru, pra-render —
  WAJIB ikut dikomit), `STORIES-R2-2026-11-20.md`, `NEWS_R2_SPEC_2026-11-20.md`,
  `NEWS_R2_REPORT_2026-11-20.md` (laporan ini).
- File R1 (poster.py/stories.py/main.py/poster lama, NEWS_SPEC/REPORT R1,
  STORIES-2026-11-20.md) sudah dihapus sebelum build R2 dimulai; saya tidak
  membacanya. LICENSE (dengan baris SPDX) dan README tidak disentuh.
- Tiap file ditulis penuh lalu direvisi di pesan terpisah (main.py,
  poster.py, stories.py masing-masing ≥2 putaran tulis).
- README masih menyebut 12 cerita (teks R1) — koordinator sebaiknya
  memperbarui kalimat itu ke 36 cerita sebelum submit.
