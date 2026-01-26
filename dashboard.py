import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Fungsi Load Data
@st.cache_data
def load_data():
    # Menggunakan main_data.csv yang sudah dibersihkan di notebook
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

# Memanggil data di awal agar variabel 'day_df' tersedia untuk sidebar
day_df = load_data()

# SIDEBAR
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Filter Data")
    
    # Filter rentang tanggal berdasarkan data dteday
    min_date = day_df['dteday'].min()
    max_date = day_df['dteday'].max()
    
    try:
        start_date, end_date = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
    except ValueError:
        st.error("Silakan pilih rentang tanggal yang valid.")
        start_date, end_date = min_date, max_date

# Filter dataframe utama berdasarkan pilihan tanggal di sidebar
main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                (day_df['dteday'] <= pd.to_datetime(end_date))]

# HEADER DASHBOARD
st.title("Bike Sharing Analysis Dashboard 🚲")

# Menampilkan Metrics (KPI)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=f"{main_df['cnt'].sum():,}")
with col2:
    st.metric("Rata-rata Harian", value=f"{int(main_df['cnt'].mean()):,}")
with col3:
    st.metric("Penyewaan Maksimum", value=f"{main_df['cnt'].max():,}")

st.markdown("---") 

#  PENGARUH CUACA 
st.subheader("1. Pengaruh Kondisi Cuaca terhadap Penyewaan")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='weathersit', 
    y='cnt', 
    data=main_df, 
    palette='viridis', 
    ax=ax1, 
    ci=None
)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig1)

#  TREN TAHUNAN 
st.subheader("2. Tren Pertumbuhan Penyewaan (2011 vs 2012)")
# Membuat kolom bulan dan tahun untuk plotting
main_df['month'] = main_df['dteday'].dt.month
monthly_trend = main_df.groupby(['yr', 'month'])['cnt'].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(
    data=monthly_trend, 
    x='month', 
    y='cnt', 
    hue='yr', 
    marker='o', 
    palette=['red', 'blue'], 
    ax=ax2
)
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.set_xlabel("Bulan")
ax2.set_ylabel("Total Penyewaan")
ax2.legend(title="Tahun")
st.pyplot(fig2)

# ANALISIS LANJUTAN (CLUSTERING)
st.subheader("3. Analisis Lanjutan: Manual Clustering (Kategori Suhu)")

def temp_clustering(temp):
    if temp < 0.3: return 'Dingin'
    elif temp < 0.6: return 'Nyaman'
    else: return 'Panas'

main_df['temp_category'] = main_df['temp'].apply(temp_clustering)

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.barplot(
    x='temp_category', 
    y='cnt', 
    data=main_df, 
    palette='coolwarm', 
    ax=ax3, 
    order=['Dingin', 'Nyaman', 'Panas'],
    ci=None
)
ax3.set_title("Rata-rata Penyewaan Berdasarkan Kategori Suhu")
st.pyplot(fig3)

st.markdown("---")
st.caption("Copyright © 2024 - Bike Sharing Analysis Project")
