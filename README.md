# 📦 Submission ETL Pipeline - Analisis Produk Kompetitor Fashion Studio

## 1. Deskripsi Proyek

Proyek ini bertujuan untuk membangun ETL pipeline yang mengambil data produk fashion dari situs [Fashion Studio](https://fashion-studio.dicoding.dev), melakukan transformasi dan pembersihan data, serta menyimpannya ke dalam CSV dan Google Sheets. Proyek ini mendukung analisis kompetitor di bidang fashion & design.

---

## 2. Fitur dan Fungsionalitas

### 🔄 ETL Modular
- Struktur kode dipisah menjadi:
  - `extract.py` – untuk scraping data
  - `transform.py` – untuk membersihkan dan memformat data
  - `load.py` – untuk menyimpan data
- Pipeline dijalankan dari `main.py`

### 🌐 Extract (Web Scraping)
- Mengambil data dari seluruh halaman (`page 1` sampai `page 50`)
- Data yang dikumpulkan meliputi:
  - `title`, `price`, `rating`, `colors`, `size`, `gender`
- Menambahkan kolom `timestamp` saat proses scraping dilakukan

### 🛠️ Transform
- Mengubah format dan tipe data:
  - Harga dari USD → IDR (x16.000)
  - Rating dari teks seperti `⭐ 4.8 / 5` → float
  - Colors dari `3 Colors` → int
  - Size dan Gender dibersihkan dari awalan seperti `Size:` atau `Gender:`
- Menghapus data:
  - `null`, `duplicated`, dan `"Unknown Product"`

### 💾 Load (Penyimpanan)
- Menyimpan data hasil transformasi ke:
  - `products.csv`
  - Google Sheets (dengan akses publik sebagai Editor)

---

## 3. Unit Test

- Unit test tersedia untuk setiap tahap:
  - `test_extract.py`, `test_transform.py`, `test_load.py`
- Menggunakan `unittest` dan `coverage` untuk validasi fungsionalitas dan pengujian kualitas
- Test coverage telah mencapai lebih dari **80%**

---

## 4. Cara Menjalankan Proyek

### ✅ Instalasi Dependensi
```bash
pip install -r requirements.txt
```

### ▶️ Jalankan Pipeline ETL
```bash
python main.py
```

### 🧪 Jalankan Unit Test
```bash
python -m unittest discover tests
```

### 📊 Jalankan Test Coverage
```bash
coverage run -m unittest discover tests
coverage report -m
```

---

## 5. Struktur Proyek

```
ETL_pipeline/
├── main.py
├── requirements.txt
├── submission.txt
├── products.csv
├── google-sheets-api.json
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
└── tests/
    ├── test_extract.py
    ├── test_transform.py
    └── test_load.py
```

---

## 6. Link Google Sheets

🔗 [https://docs.google.com/spreadsheets/d/1k92AH9CeNIfPGcev74udCj_TgyFNLS1tQ4tWfuQtyns](https://docs.google.com/spreadsheets/d/1k92AH9CeNIfPGcev74udCj_TgyFNLS1tQ4tWfuQtyns)

- Akses: **Anyone with the link** can **Edit**
- Service Account yang digunakan: `fashion@fashion-459301.iam.gserviceaccount.com`

---

## 7. Catatan Tambahan

- Jumlah data akhir setelah transformasi: ±1000 baris
- Semua kolom sudah sesuai spesifikasi: tidak ada null, invalid, atau duplikat
- Pipeline dapat dijalankan ulang tanpa kendala