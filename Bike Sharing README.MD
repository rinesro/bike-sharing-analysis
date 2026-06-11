🚲 Capital Bikeshare: Exploratory Data Analysis (EDA) & Data Visualization
Catatan Perekrut: Proyek ini merupakan bagian dari validasi sertifikasi Data Scientist (Expert) dari IDCamp & Dicoding Indonesia. Analisis difokuskan pada ekstraksi wawasan bisnis (actionable insights) dari data historis penyewaan sepeda untuk mendukung optimalisasi strategi operasional dan pemasaran.
📌 Latar Belakang Proyek
Sistem bike-sharing modern telah menjadi tulang punggung mobilitas perkotaan. Namun, ketersediaan armada dan tingkat penyewaan sering kali berfluktuasi karena sangat dipengaruhi oleh faktor lingkungan eksternal.
Proyek ini bertujuan untuk melakukan proses End-to-End Data Analysis—mulai dari Data Wrangling (Gathering, Assessing, Cleaning), hingga Exploratory Data Analysis (EDA) dan Visualisasi Data—guna membedah pola perilaku penyewa sepeda di Washington D.C. pada kurun waktu 2011-2012.
🎯 Pertanyaan Bisnis (Business Questions)
Analisis data dalam proyek ini dirancang untuk menjawab dua pertanyaan strategis operasional berikut:
1. Bagaimana pengaruh kondisi cuaca terhadap jumlah total penyewaan sepeda harian?
2. Bagaimana tren pertumbuhan penyewaan sepeda pada tahun 2011 dibandingkan tahun 2012?
📊 Ekstraksi Wawasan (Key Insights & Conclusion)
Berdasarkan eksplorasi dan visualisasi data yang dilakukan pada notebook, ditemukan beberapa insight krusial:
* Dampak Signifikan Kondisi Cuaca: Terdapat korelasi negatif yang kuat antara buruknya cuaca dan jumlah penyewa. Pengguna jauh lebih aktif saat cuaca cerah (Clear/Partly Cloudy dengan rata-rata 4.876 penyewa/hari). Sebaliknya, penurunan drastis terjadi saat cuaca berubah menjadi Light Rain/Snow. Bisnis perlu menyesuaikan alokasi armada saat perkiraan cuaca buruk tiba.
* Tren Pertumbuhan Positif (2011 vs 2012): Performa bisnis menunjukkan tren pertumbuhan yang sangat sehat. Total penyewaan pada tahun 2012 secara konsisten selalu lebih tinggi dibandingkan 2011 di setiap bulannya. Tren musiman juga terlihat jelas, di mana puncak permintaan terjadi pada bulan Juni hingga September (musim panas dan gugur).
* Preferensi Suhu Pengguna (Advanced Clustering Analysis): Melalui teknik manual clustering (pengelompokan suhu menjadi rentang Cold, Moderate, dan Hot), ditemukan bahwa cuaca Cold (dingin) adalah hambatan utama (bottleneck) ketertarikan pelanggan. Rekomendasi bisnis: Perusahaan dapat mengimplementasikan promosi khusus diskon musim dingin atau menyediakan perlengkapan penghangat di stasiun untuk mendongkrak retensi penyewa di suhu Cold.
🛠️ Tech Stack & Workflow
* Data Wrangling & Manipulation: Python, Pandas, NumPy
* Data Visualization: Matplotlib, Seaborn
* Environment: Jupyter Notebook
🚀 Cara Menjalankan Proyek (Reproducibility)
Proyek ini mengedepankan prinsip reproducibility (dapat direproduksi ulang dengan hasil yang sama). Anda dapat menjalankan ulang seluruh analisis ini secara lokal:
1. Clone repositori ini:
git clone [https://github.com/sandhikahamzah/bike-sharing-analysis.git](https://github.com/sandhikahamzah/bike-sharing-analysis.git)

2. Pastikan library prasyarat sudah terinstal di environment Anda:
pip install pandas numpy matplotlib seaborn jupyter

3. Buka Jupyter Notebook dan jalankan file eksekusi utama:
jupyter notebook "notebook (2).ipynb"

📂 Struktur Repositori
   * /data: Direktori yang berisi dataset mentah (day.csv, hour.csv).
   * notebook (2).ipynb: File utama Jupyter Notebook yang menampung seluruh logika data cleaning, analisis deskriptif, teknik clustering, dan explanatory analysis (visualisasi).
   * README.md: Dokumentasi proyek.
Data Source Acknowledgement:
Dataset original disediakan oleh Hadi Fanaee-T (University of Porto) berdasarkan data historis sistem Capital Bikeshare, Washington D.C., USA.
💼 Let's Connect!
Dibuat oleh Sandhika Hamzah - ID Dicoding: sandhika_hamzah_jvzn Silakan hubungi saya melalui email (sanvinzah@gmail.com) atau LinkedIn untuk diskusi lebih lanjut mengenai peluang kolaborasi analitik data!