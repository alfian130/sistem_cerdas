import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sistem Logika Fuzzy",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 TUGAS PRAKTIKUM LOGIKA FUZZY")
st.write("Pilih salah satu studi kasus pada menu sidebar.")

# Fungsi menampilkan grafik
def tampilkan_grafik(x, y1, y2, y3, label1, label2, label3, judul):
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(x, y1, label=label1, linewidth=2)
    ax.plot(x, y2, label=label2, linewidth=2)
    ax.plot(x, y3, label=label3, linewidth=2)

    ax.set_title(judul)
    ax.set_ylabel("μ(x)")
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

# Sidebar
menu = st.sidebar.selectbox(
    "Pilih Kasus",
    [
        "Kasus 1 - Penilaian Mahasiswa",
        "Kasus 2 - Kelayakan Beasiswa",
        "Kasus 3 - Tingkat Kemacetan"
    ]
)

# ==================================================
# KASUS 1
# ==================================================
if menu == "Kasus 1 - Penilaian Mahasiswa":

    st.header("📚 Penilaian Mahasiswa")

    nilai = st.slider("Nilai Ujian", 0, 100, 50)

    def rendah(x):
        if x <= 40:
            return 1
        elif x < 60:
            return (60 - x) / 20
        return 0

    def sedang(x):
        if 40 < x < 60:
            return (x - 40) / 20
        elif 60 <= x < 80:
            return (80 - x) / 20
        return 0

    def tinggi(x):
        if 60 < x < 80:
            return (x - 60) / 20
        elif x >= 80:
            return 1
        return 0

    r = rendah(nilai)
    s = sedang(nilai)
    t = tinggi(nilai)

    st.subheader("Derajat Keanggotaan")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rendah", round(r, 2))
    col2.metric("Sedang", round(s, 2))
    col3.metric("Tinggi", round(t, 2))

    hasil = max(
        {"Rendah": r, "Sedang": s, "Tinggi": t},
        key=lambda x: {"Rendah": r, "Sedang": s, "Tinggi": t}[x]
    )

    st.success(f"Hasil Penilaian: {hasil}")

    x = np.arange(0, 101, 1)

    tampilkan_grafik(
        x,
        [rendah(i) for i in x],
        [sedang(i) for i in x],
        [tinggi(i) for i in x],
        "Rendah",
        "Sedang",
        "Tinggi",
        "Grafik Fungsi Keanggotaan Nilai Mahasiswa"
    )

# ==================================================
# KASUS 2
# ==================================================
elif menu == "Kasus 2 - Kelayakan Beasiswa":

    st.header("🎓 Kelayakan Beasiswa")

    ipk = st.slider("IPK", 0.0, 4.0, 2.5, 0.01)

    def tidak_layak(x):
        if x <= 1.5:
            return 1
        elif x < 2.5:
            return (2.5 - x) / (2.5 - 1.5)
        return 0

    def dipertimbangkan(x):
        if 1.5 < x < 2.5:
            return (x - 1.5) / (2.5 - 1.5)
        elif 2.5 <= x < 3.5:
            return (3.5 - x) / (3.5 - 2.5)
        return 0

    def layak(x):
        if 2.5 < x < 3.5:
            return (x - 2.5) / (3.5 - 2.5)
        elif x >= 3.5:
            return 1
        return 0

    tl = tidak_layak(ipk)
    dp = dipertimbangkan(ipk)
    ly = layak(ipk)

    st.subheader("Derajat Keanggotaan")

    col1, col2, col3 = st.columns(3)

    col1.metric("Tidak Layak", round(tl, 2))
    col2.metric("Dipertimbangkan", round(dp, 2))
    col3.metric("Layak", round(ly, 2))

    hasil = max(
        {
            "Tidak Layak": tl,
            "Dipertimbangkan": dp,
            "Layak": ly
        },
        key=lambda x: {
            "Tidak Layak": tl,
            "Dipertimbangkan": dp,
            "Layak": ly
        }[x]
    )

    st.success(f"Hasil Evaluasi: {hasil}")

    x = np.arange(0, 4.01, 0.01)

    tampilkan_grafik(
        x,
        [tidak_layak(i) for i in x],
        [dipertimbangkan(i) for i in x],
        [layak(i) for i in x],
        "Tidak Layak",
        "Dipertimbangkan",
        "Layak",
        "Grafik Fungsi Keanggotaan Beasiswa"
    )

# ==================================================
# KASUS 3
# ==================================================
else:

    st.header("🚦 Tingkat Kemacetan")

    kendaraan = st.slider("Jumlah Kendaraan", 0, 1000, 500)

    def lancar(x):
        if x <= 300:
            return 1
        elif x < 500:
            return (500 - x) / 200
        return 0

    def padat(x):
        if 300 < x < 500:
            return (x - 300) / 200
        elif 500 <= x < 700:
            return (700 - x) / 200
        return 0

    def macet(x):
        if 500 < x < 700:
            return (x - 500) / 200
        elif x >= 700:
            return 1
        return 0

    l = lancar(kendaraan)
    p = padat(kendaraan)
    m = macet(kendaraan)

    st.subheader("Derajat Keanggotaan")

    col1, col2, col3 = st.columns(3)

    col1.metric("Lancar", round(l, 2))
    col2.metric("Padat", round(p, 2))
    col3.metric("Macet", round(m, 2))

    hasil = max(
        {"Lancar": l, "Padat": p, "Macet": m},
        key=lambda x: {"Lancar": l, "Padat": p, "Macet": m}[x]
    )

    st.success(f"Tingkat Kemacetan: {hasil}")

    x = np.arange(0, 1001, 1)

    tampilkan_grafik(
        x,
        [lancar(i) for i in x],
        [padat(i) for i in x],
        [macet(i) for i in x],
        "Lancar",
        "Padat",
        "Macet",
        "Grafik Fungsi Keanggotaan Kemacetan"
    )
