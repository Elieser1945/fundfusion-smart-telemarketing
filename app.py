import streamlit as st
import pandas as pd
import joblib
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman Web
st.set_page_config(page_title="FundFusion Smart Telemarketing", page_icon="🎯", layout="wide")

# 2. Injeksi Kustom CSS dengan Garis Abstrak (SVG) & Gradien
st.markdown("""
    <style>
    /* Mengurangi spasi kosong di atas */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Latar Belakang Gradien Abstrak dengan Garis Gelombang SVG */
    .stApp {
        background-color: #040114;
        background-image: 
            /* Cahaya Magenta di Kanan Bawah */
            radial-gradient(circle at 90% 80%, rgba(154, 0, 63, 0.7) 0%, transparent 60%),
            /* Cahaya Ungu di Kiri Atas */
            radial-gradient(circle at 10% 20%, rgba(21, 0, 48, 1) 0%, transparent 50%),
            /* Cahaya Ungu Terang di Kanan Atas */
            radial-gradient(circle at 70% 10%, rgba(70, 0, 75, 0.8) 0%, transparent 50%),
            /* Garis-garis Gelombang SVG */
            url("data:image/svg+xml,%3Csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3E%3Cg stroke='%23ffffff' stroke-width='1.5' fill='none' opacity='0.07'%3E%3Cpath d='M-100,200 C300,50 600,600 1200,300 C1600,100 1900,400 2200,300' /%3E%3Cpath d='M-100,230 C320,70 620,620 1220,320 C1620,120 1920,420 2220,320' /%3E%3Cpath d='M-100,260 C340,90 640,640 1240,340 C1640,140 1940,440 2240,340' /%3E%3Cpath d='M-100,290 C360,110 660,660 1260,360 C1660,160 1960,460 2260,360' /%3E%3Cpath d='M-100,320 C380,130 680,680 1280,380 C1680,180 1980,480 2280,380' /%3E%3Cpath d='M-100,350 C400,150 700,700 1300,400 C1700,200 2000,500 2300,400' /%3E%3Cpath d='M-100,380 C420,170 720,720 1320,420 C1720,220 2020,520 2320,420' /%3E%3Cpath d='M-100,410 C440,190 740,740 1340,440 C1740,240 2040,540 2340,440' /%3E%3C/g%3E%3C/svg%3E");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
        color: #ffffff;
    }

    /* Mempercantik Tombol Prediksi bergaya Neon Pill-Shape */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #9D00FF 0%, #FF007B 100%);
        color: white !important;
        border: none;
        border-radius: 50px;
        padding: 12px 28px;
        font-weight: 700;
        letter-spacing: 1.5px;
        width: 100%;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 15px rgba(255, 0, 123, 0.4);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 0, 123, 0.7);
        background: linear-gradient(90deg, #FF007B 0%, #9D00FF 100%);
    }

    /* Kustomisasi Header */
    .header-title {
        text-align: center;
        color: #ffffff; 
        font-weight: 800;
        margin-bottom: 0px;
        text-shadow: 0px 2px 10px rgba(255, 255, 255, 0.2);
    }
    .header-subtitle {
        text-align: center;
        color: #e2e8f0;
        margin-bottom: 30px;
        font-weight: 300;
    }
    
    /* Desain Footer Profil bergaya Glassmorphism */
    .profile-footer {
        text-align: center;
        margin-top: 60px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    hr { border-color: rgba(255,255,255,0.1) !important; }
    </style>
""", unsafe_allow_html=True)

# Muat Model K-Means
@st.cache_resource
def load_model():
    try:
        return joblib.load('kmeans_fundfusion_exp1.pkl')
    except Exception as e:
        return None

model = load_model()

# 3. Bagian Header
st.markdown("<h1 class='header-title'>🎯 FundFusion Smart Telemarketing</h1>", unsafe_allow_html=True)
st.markdown("<p class='header-subtitle'>Aplikasi rekomendasi produk cerdas berbasis pola demografi untuk menekan angka penolakan.</p>", unsafe_allow_html=True)
st.divider()

# 4. Layout Dashboard
col_context, col_form = st.columns([1, 1.5], gap="large")

with col_context:
    st.subheader("🧠 Konteks Bisnis")
    
    st.info("Saat ini, FundFusion belum memiliki strategi penawaran yang jelas, menyebabkan calon nasabah dapat dihubungi berulang kali oleh account manager yang berbeda untuk ditawarkan produk yang berbeda pula.")
    
    st.warning("Implikasinya, rejection rate yang didapatkan sangat tinggi dan dianggap sebagai spam oleh calon nasabah yang berujung pada pemblokiran nomor.")
    
    st.success("**💡 Objective Eksperimen:**\nMengelompokkan nasabah berdasarkan demografis untuk dicari pattern kepemilikan produk agar penawaran lebih tepat sasaran.")

with col_form:
    st.subheader("🪪 Masukkan Data Demografi Nasabah")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        usia = st.number_input("Usia", min_value=17, max_value=99, value=30)
        jumlah_anak = st.number_input("Jumlah Anak", min_value=0, max_value=10, value=0)
    with c2:
        area = st.selectbox("Area", ["Jakarta", "Bogor", "Bandung", "Surabaya", "Jogja", "Solo"])
        jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    with c3:
        status_perkawinan = st.selectbox("Status Perkawinan", ["Belum Menikah", "Menikah", "Cerai", "Janda/Duda"])
        pendidikan = st.selectbox("Pendidikan", ["Tidak Memiliki Pendidikan Formal", "SD", "SMP", "SMA", "Sarjana", "Magister", "Doktor"])
        vintage = st.selectbox("Vintage (Lama)", ["< 1 Tahun", "2 - 3 Tahun", "> 4 Tahun"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submit_button = st.button("GET STARTED")

# 5. Logika Prediksi dan Penampilan Hasil
if submit_button:
    if model is None:
        st.error("⚠️ Model 'kmeans_fundfusion_exp1.pkl' tidak ditemukan di direktori saat ini.")
    else:
        st.markdown("<div id='hasil-prediksi'></div>", unsafe_allow_html=True)
        st.balloons() 
        
        input_data = pd.DataFrame([{
            "Usia": usia,
            "Jumlah_Anak": jumlah_anak,
            "Area": area,
            "Jenis_Kelamin": jenis_kelamin,
            "Status_Perkawinan": status_perkawinan,
            "Pendidikan": pendidikan,
            "Vintage": vintage
        }])
        
        df_encoded = pd.get_dummies(input_data)
        if hasattr(model, "feature_names_in_"):
            df_encoded = df_encoded.reindex(columns=model.feature_names_in_, fill_value=0)
        
        cluster_pred = int(model.predict(df_encoded)[0])
        
        st.divider()
        st.subheader("✨ Hasil Analisis & Rekomendasi Kampanye")
        
        res_col1, res_col2 = st.columns([1, 2.5])
        
        with res_col1:
            st.metric(label="Hasil Klasterisasi", value=f"Klaster {cluster_pred}", delta="Pola Ditemukan", delta_color="normal")
            
        with res_col2:
            if cluster_pred == 0:
                st.info("👴 **Segmen: Klaster 0 (Senior / Usia Lanjut)**")
                st.write("- **Karakteristik Data:** Rata-rata usia matang/senior (~58 tahun) dengan proporsi status cerai yang lebih tinggi.")
                st.write("- **Rekomendasi Produk:** **Deposito Berjangka** atau produk pengelolaan dana pensiun/hari tua yang stabil.")
                st.write("- **Strategi Telemarketing:** Gunakan pendekatan yang sopan, formal, dan tawarkan produk low-risk.")
                
            elif cluster_pred == 1:
                st.warning("🧑 **Segmen: Klaster 1 (Muda / Usia Produktif Awal)**")
                st.write("- **Karakteristik Data:** Rata-rata usia muda (~29 tahun) dan didominasi status belum menikah.")
                st.write("- **Rekomendasi Produk:** **Tabungan Digital**, **Kartu Kredit**, atau produk investasi awal yang fleksibel.")
                st.write("- **Strategi Telemarketing:** Tawarkan kemudahan akses digital dan promo transaksi harian.")
                
            else:
                st.success("👨‍👩‍👧 **Segmen: Klaster 2 (Paruh Baya / Keluarga Mapan)**")
                st.write("- **Karakteristik Data:** Berada di kisaran usia produktif menengah (~45 tahun) dengan kestabilan finansial.")
                st.write("- **Rekomendasi Produk:** **Kredit Rumah (KPR)**, **Kredit Kendaraan**, atau **Asuransi Pendidikan Anak**.")
                st.write("- **Strategi Telemarketing:** Fokus pada penawaran pembiayaan aset jangka panjang untuk keluarga.")

        components.html(
            """
            <script>
            var target = window.parent.document.getElementById('hasil-prediksi');
            if (target) {
                target.scrollIntoView({behavior: 'smooth', block: 'start'});
            } else {
                window.parent.scrollTo({top: window.parent.document.body.scrollHeight, behavior: 'smooth'});
            }
            </script>
            """,
            height=0
        )

# 6. Footer Portofolio
st.markdown("""
<div class="profile-footer">
    <p style='margin: 0; color: #cbd5e1; font-size: 14px; font-weight: 400; text-transform: uppercase; letter-spacing: 1px;'>Developed by</p>
    <p style='margin: 5px 0; color: #ffffff; font-size: 24px; font-weight: 800; letter-spacing: 1.5px;'>Elieser Pasaribu</p>
    <p style='margin: 0; color: #ff007b; font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px;'>
        Data Analyst <span style="color:rgba(255,255,255,0.3);">|</span> Data Science <span style="color:rgba(255,255,255,0.3);">|</span> Machine Learning
    </p>
</div>
""", unsafe_allow_html=True)