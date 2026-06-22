import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Sistem Penilaian Mahasiswa Menggunakan Logika Fuzzy")

nilai = st.slider("Masukkan Nilai Ujian", 0, 100, 50)

# Fungsi Keanggotaan
def rendah(x):
    if x <= 40:
        return 1
    elif 40 < x < 60:
        return (60 - x) / 20
    else:
        return 0

def sedang(x):
    if x <= 40:
        return 0
    elif 40 < x < 60:
        return (x - 40) / 20
    elif 60 <= x < 80:
        return (80 - x) / 20
    else:
        return 0

def tinggi(x):
    if x <= 60:
        return 0
    elif 60 < x < 80:
        return (x - 60) / 20
    else:
        return 1

# Hitung Derajat Keanggotaan
r = rendah(nilai)
s = sedang(nilai)
t = tinggi(nilai)

st.subheader("Derajat Keanggotaan")

st.write(f"Rendah : {r:.2f}")
st.write(f"Sedang : {s:.2f}")
st.write(f"Tinggi : {t:.2f}")

# Hasil
hasil = max(
    ("Rendah", r),
    ("Sedang", s),
    ("Tinggi", t),
    key=lambda x: x[1]
)

st.success(f"Kategori Nilai: {hasil[0]}")

# Grafik
x = np.arange(0, 101, 1)

rendah_y = [rendah(i) for i in x]
sedang_y = [sedang(i) for i in x]
tinggi_y = [tinggi(i) for i in x]

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x, rendah_y, label='Rendah')
ax.plot(x, sedang_y, label='Sedang')
ax.plot(x, tinggi_y, label='Tinggi')

ax.axvline(nilai, linestyle='--')
ax.set_title("Grafik Fungsi Keanggotaan")
ax.set_xlabel("Nilai")
ax.set_ylabel("μ(x)")
ax.legend()

st.pyplot(fig)
