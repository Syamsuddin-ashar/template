import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === Data Penjualan (contoh warung makan) ===
data = pd.DataFrame({
    "Menu": ["Nasi Goreng", "Mie Ayam", "Soto Ayam", "Ayam Geprek", "Es Teh Manis", "Jus Alpukat"],
    "Minggu1": [40, 30, 20, 35, 50, 15],
    "Minggu2": [50, 25, 22, 40, 60, 18],
    "Minggu3": [55, 28, 18, 42, 65, 20],
    "Minggu4": [60, 35, 15, 48, 70, 22]
})
data["Total"] = data[["Minggu1", "Minggu2", "Minggu3", "Minggu4"]].sum(axis=1)

# === Judul Dashboard ===
st.title("📊 Dashboard Penjualan Warung Makan")

# === Tampilkan Tabel ===
st.subheader("Data Penjualan")
st.dataframe(data)

# === Analisis Ringkas ===
st.subheader("Ringkasan Analisis")
st.write("Total Penjualan:", int(data["Total"].sum()))
st.write("Rata-rata per Menu:", round(data["Total"].mean(), 2))
st.write("Menu Terlaris:", data.loc[data["Total"].idxmax()]["Menu"])
st.write("Menu Paling Tidak Laku:", data.loc[data["Total"].idxmin()]["Menu"])

# === Grafik Tren ===
st.subheader("Tren Penjualan per Minggu")
fig, ax = plt.subplots(figsize=(8,5))
for i in range(len(data)):
    ax.plot(["Minggu1","Minggu2","Minggu3","Minggu4"], 
            data.iloc[i,1:5], 
            marker='o', 
            label=data["Menu"][i])
ax.set_title("Tren Penjualan")
ax.set_xlabel("Minggu")
ax.set_ylabel("Jumlah Terjual")
ax.legend()
ax.grid(True)
st.pyplot(fig)
