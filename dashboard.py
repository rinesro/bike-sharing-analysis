import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# 1. Fungsi Load Data
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    
    # Konversi tanggal
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    # Mapping weathersit untuk kemudahan visualisasi
    day_df['weather_label'] = day_df['weathersit'].map({
        1: 'Cerah', 
        2: 'Berkabut', 
        3: 'Hujan Ringan', 
        4: 'Hujan Berat'
    })
    
    # Mapping tahun
    day_df['year'] = day_df['dteday'].dt.year
    
    return day_df, hour_df

day_df, hour_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Filter Data")
    
    # Filter rentang tanggal
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=day_df['dteday'].min(),
        max_value=day_df['dteday'].max(),
        value=[day_df['dteday'].min(), day_df['dteday'].max()]
    )

# Filter dataframe berdasarkan tanggal
main_df = day_df[(day_df['dteday'] >= str(start_date)) & 
                (day_df['dteday'] <= str(end_date))]

# --- HEADER DASHBOARD ---
st.title("Bike Sharing Analysis Dashboard 🚲")

# Menampilkan Metrics (KPI)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=f"{main_df['cnt'].sum():,}")
with col2:
    st.metric("Rata-rata Harian", value=f"{int(main_df['cnt'].mean()):,}")
with col3:
    st.metric("Penyewaan Maksimum", value=f"{main_df['cnt'].max():,}")

st.divider()

# --- BAGIAN 1: MENJAWAB PERTANYAAN CUACA ---
st.subheader("1. Pengaruh Kondisi Cuaca terhadap Penyewaan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='weather_label', y='cnt', data=main_df, palette='viridis', ax=ax, ci=None)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig)
st.write("Insight: Pengguna cenderung menyewa sepeda jauh lebih banyak saat cuaca Cerah dibandingkan kondisi lainnya.")

# --- BAGIAN 2: MENJAWAB PERTANYAAN TREN TAHUNAN ---
st.subheader("2. Tren Pertumbuhan Penyewaan (2011 vs 2012)")
# Menyiapkan data tren bulanan dari data harian
main_df['month'] = main_df['dteday'].dt.month
monthly_trend = main_df.groupby(['year', 'month'])['cnt'].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=monthly_trend, x='month', y='cnt', hue='year', marker='o', palette=['red', 'blue'], ax=ax2)
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig2)
st.write("Insight: Terdapat kenaikan signifikan jumlah penyewa di tahun 2012 dibandingkan 2011 pada hampir semua bulan.")

# --- BAGIAN 3: ANALISIS LANJUTAN (MANUAL CLUSTERING) ---
st.subheader("3. Analisis Lanjutan: Manual Clustering (Kategori Suhu)")
# Menggunakan data day_df untuk clustering suhu
def temp_clustering(temp):
    if temp < 0.3: return 'Dingin'
    elif temp < 0.6: return 'Nyaman'
    else: return 'Panas'

main_df['temp_category'] = main_df['temp'].apply(temp_clustering)

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.boxplot(x='temp_category', y='cnt', data=main_df, palette='coolwarm', ax=ax3)
ax3.set_title("Distribusi Penyewaan Berdasarkan Kategori Suhu")
st.pyplot(fig3)
st.write("Insight: Suhu 'Nyaman' memiliki rata-rata penyewaan tertinggi.")

# --- BAGIAN 4: PENGGUNAAN DATA HOUR.CSV ---
st.subheader("4. Detail Penyewaan Berdasarkan Jam (Insight Tambahan)")
# Filter data jam berdasarkan tanggal yang dipilih
hour_filtered = hour_df[(hour_df['dteday'] >= str(start_date)) & 
                        (hour_df['dteday'] <= str(end_date))]
hour_trend = hour_filtered.groupby('hr')['cnt'].mean().reset_index()

fig4, ax4 = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hr', y='cnt', data=hour_trend, marker='o', ax=ax4)
ax4.set_xticks(range(0, 24))
ax4.set_xlabel("Jam (0-23)")
ax4.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig4)
st.write("Insight: Jam sibuk penyewaan terjadi pada pagi hari (jam 7-8) dan sore hari (jam 17-18).")

st.caption("Copyright © 2024 - Bike Sharing Analysis Project")