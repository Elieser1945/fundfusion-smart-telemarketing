# 🎯 FundFusion Smart Telemarketing: Customer Segmentation

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://fundfusion-smart-telemarketing-by-elieser.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-K--Means-FF007B?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![UI](https://img.shields.io/badge/UI-Glassmorphism-9D00FF)](https://streamlit.io/)

Aplikasi web berbasis **Machine Learning (K-Means Clustering)** untuk membantu tim telemarketing FundFusion menentukan strategi penawaran produk yang tepat sasaran berdasarkan pola demografi nasabah.

---

## 🚀 Live Demo
Coba aplikasinya langsung di sini: **[FundFusion Smart Telemarketing App](https://fundfusion-smart-telemarketing-by-elieser.streamlit.app/)**

---

## 📊 Konteks Bisnis & Problem Statement
**FundFusion**, sebuah institusi bank, sedang mengembangkan layanan telemarketing. Saat ini, bank belum memiliki strategi penawaran yang terarah. Dampaknya:
- Calon nasabah sering dihubungi berkali-kali oleh *account manager* yang berbeda.
- Produk yang ditawarkan seringkali tidak relevan dengan kondisi finansial/demografi nasabah.
- **Tingkat penolakan (rejection rate) sangat tinggi** dan bank sering dilaporkan sebagai *spam*, berujung pada pemblokiran nomor.

**💡 Solusi:**
Membuat model *Clustering* untuk memetakan nasabah ke dalam beberapa segmen berdasarkan profil demografis mereka. Dengan memahami karakteristik tiap klaster, tim telemarketing dapat memprioritaskan penawaran produk yang probabilitas penerimaannya lebih tinggi. Model ini dievaluasi dengan *Silhouette Score* > 0.7.

---

## ✨ Fitur Utama
- **Real-Time Prediction:** Memasukkan parameter demografi secara langsung dan mendapatkan hasil segmentasi secara *real-time*.
- **Business Insights:** Tidak hanya menampilkan label klaster, aplikasi juga memberikan *insight* profil karakteristik segmen dan rekomendasi kampanye/produk spesifik.
- **Modern & Responsive UI:** Dibangun dengan antarmuka bergaya abstrak gradien dan *glassmorphism* untuk pengalaman pengguna yang intuitif dan profesional.
- **Auto-Scroll & Auto-Reset:** UX yang mulus saat pengguna berinteraksi dengan form input data.

---

## 🧬 Variabel Demografi (Input)
Aplikasi memproses parameter berikut untuk memprediksi klaster nasabah:
1. **Usia:** (Contoh: 17 - 99 tahun)
2. **Jumlah Anak:** Numerik
3. **Area:** Lokasi nasabah (Jakarta, Bogor, Bandung, Surabaya, Jogja, Solo)
4. **Jenis Kelamin:** Laki-laki / Perempuan
5. **Status Perkawinan:** Belum Menikah, Menikah, Cerai, Janda/Duda
6. **Pendidikan:** Tingkat pendidikan terakhir (SD hingga Doktor)
7. **Vintage:** Lama durasi menjadi nasabah (< 1 Tahun, 2 - 3 Tahun, > 4 Tahun)

---

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python
- **Machine Learning:** Scikit-Learn (K-Means Clustering)
- **Data Manipulation & Model Serialization:** Pandas, Joblib
- **Web Deployment & UI:** Streamlit, Custom HTML/CSS/SVG

---

## 💻 Cara Menjalankan Secara Lokal (Local Installation)

Jika Anda ingin menjalankan proyek ini di mesin lokal, ikuti langkah-langkah berikut:

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/USERNAME_ANDA/fundfusion-smart-telemarketing.git
   cd fundfusion-smart-telemarketing
   ```

2. **Buat Virtual Environment (Opsional namun direkomendasikan):**
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Linux/Mac
   env\Scripts\activate     # Untuk Windows
   ```

3. **Instal dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit:**
   ```bash
   streamlit run app.py
   ```

---

## 🧑‍💻 Developed By
**Elieser Pasaribu**  
Data Analyst | Data Scientist | Machine Learning Enthusiast  

Terbuka untuk diskusi, masukan, dan peluang kolaborasi! Silakan hubungi saya melalui GitHub atau LinkedIn.
