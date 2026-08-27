🚲 Capital Bikeshare: Exploratory Data Analysis (EDA) & Interactive Dashboard

Catatan Perekrut: Proyek ini merupakan bagian dari validasi sertifikasi Data Scientist (Expert) dari IDCamp & Dicoding Indonesia. Analisis difokuskan pada ekstraksi wawasan bisnis (actionable insights) dari data historis penyewaan sepeda untuk mendukung optimalisasi strategi operasional dan pemasaran.

## 📌 Latar Belakang Proyek

Sistem bike-sharing modern telah menjadi tulang punggung mobilitas perkotaan. Namun, ketersediaan armada dan tingkat penyewaan sering kali berfluktuasi karena sangat dipengaruhi oleh faktor lingkungan eksternal.

Proyek ini melakukan proses End-to-End Data Analysis — mulai dari Data Wrangling (Gathering, Assessing, Cleaning), Exploratory Data Analysis (EDA), Visualisasi Data, hingga penyajian hasil dalam **dashboard interaktif (Streamlit)** — guna membedah pola perilaku penyewa sepeda di Washington D.C. pada kurun waktu 2011-2012.

## 🎯 Pertanyaan Bisnis (Business Questions)

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah total penyewaan sepeda harian?
2. Bagaimana tren pertumbuhan penyewaan sepeda pada tahun 2011 dibandingkan tahun 2012?

Sebagai pelengkap, notebook juga membedah pola penyewaan per jam (commuting vs rekreasi) menggunakan data per-jam (`hour.csv`).

## 📊 Key Insights & Conclusion

* **Dampak Signifikan Kondisi Cuaca:** Terdapat korelasi negatif yang kuat antara buruknya cuaca dan jumlah penyewa. Pengguna jauh lebih aktif saat cuaca cerah (Clear/Partly Cloudy, rata-rata ~4.876 penyewa/hari). Sebaliknya, penurunan drastis terjadi saat cuaca berubah menjadi Light Rain/Snow.
* **Tren Pertumbuhan Positif (2011 vs 2012):** Total penyewaan pada tahun 2012 secara konsisten lebih tinggi dibandingkan 2011 di setiap bulannya. Puncak permintaan terjadi pada bulan Juni-September (musim panas-gugur).
* **Preferensi Suhu Pengguna (Manual Clustering):** Suhu Moderate-Hot memiliki rata-rata penyewaan jauh lebih tinggi dibanding suhu Cold, yang menjadi hambatan utama ketertarikan pelanggan.
* **Pola Per Jam:** Hari kerja menunjukkan dua puncak tajam (jam 08.00 dan 17.00-18.00) yang khas pola commuting, sementara akhir pekan menunjukkan satu puncak lebar di siang hari — menandakan dua segmen pengguna yang berbeda: komuter dan wisatawan/rekreasi.

## 🛠️ Tech Stack

* **Data Wrangling & Analysis:** Python, Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Dashboard:** Streamlit
* **Environment:** Jupyter Notebook

## 🚀 Cara Menjalankan Proyek

**1. Clone repositori ini:**
```bash
git clone https://github.com/rinesro/bike-sharing-analysis.git
cd bike-sharing-analysis
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Jalankan notebook analisis (opsional, untuk melihat proses EDA lengkap):**
```bash
jupyter notebook notebook.ipynb
```
Menjalankan notebook ini secara end-to-end juga akan menghasilkan ulang `main_data.csv`, yaitu data bersih yang menjadi sumber dashboard.

**4. Jalankan dashboard interaktif:**
```bash
streamlit run dashboard.py
```

## 📂 Struktur Repositori

* `day.csv`, `hour.csv` — dataset mentah (Capital Bikeshare, 2011-2012).
* `main_data.csv` — data harian hasil cleaning di notebook, dipakai langsung oleh `dashboard.py`.
* `notebook.ipynb` — file utama: data wrangling, EDA, visualisasi, dan analisis lanjutan.
* `dashboard.py` — dashboard Streamlit interaktif dengan filter rentang tanggal.
* `Metadata.txt` — deskripsi asli dataset dari penyedia data.
* `requirements.txt` — daftar dependency Python.

## 📎 Data Source Acknowledgement

Dataset original disediakan oleh Hadi Fanaee-T (University of Porto) berdasarkan data historis sistem Capital Bikeshare, Washington D.C., USA. Sitasi lengkap tersedia di `Metadata.txt`.

## 💼 Let's Connect!

Dibuat oleh Sandhika Hamzah — ID Dicoding: sandhika_hamzah_jvzn. Silakan hubungi saya melalui email (sanvinzah@gmail.com) atau LinkedIn untuk diskusi lebih lanjut mengenai peluang kolaborasi analitik data.
