import streamlit as st

st.set_page_config(page_title="Logika Fuzzy", page_icon="🧠")

st.title("🧠 Sistem Logika Fuzzy")
st.write("Pilih salah satu studi kasus berikut:")

menu = st.sidebar.selectbox(
    "Pilih Kasus",
    [
        "Penilaian Mahasiswa",
        "Kelayakan Beasiswa",
        "Tingkat Kemacetan"
    ]
)

# ==========================
# KASUS 1
# ==========================
if menu == "Penilaian Mahasiswa":

    st.header("Kasus 1 - Penilaian Mahasiswa")

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
    st.write("Rendah :", round(r, 2))
    st.write("Sedang :", round(s, 2))
    st.write("Tinggi :", round(t, 2))

    hasil = max(
        {"Rendah": r, "Sedang": s, "Tinggi": t},
        key=lambda k: {"Rendah": r, "Sedang": s, "Tinggi": t}[k]
    )

    st.success(f"Hasil Penilaian: {hasil}")

# ==========================
# KASUS 2
# ==========================
elif menu == "Kelayakan Beasiswa":

    st.header("Kasus 2 - Kelayakan Beasiswa")

    ipk = st.slider("IPK", 0.0, 4.0, 2.5, 0.01)

    def tidak_layak(x):
        if x <= 1.5:
            return 1
        elif x < 2.5:
            return (2.5 - x)
        return 0

    def dipertimbangkan(x):
        if 1.5 < x < 2.5:
            return (x - 1.5)
        elif 2.5 <= x < 3.5:
            return (3.5 - x)
        return 0

    def layak(x):
        if 2.5 < x < 3.5:
            return (x - 2.5)
        elif x >= 3.5:
            return 1
        return 0

    tl = tidak_layak(ipk)
    dp = dipertimbangkan(ipk)
    ly = layak(ipk)

    st.subheader("Derajat Keanggotaan")
    st.write("Tidak Layak :", round(tl, 2))
    st.write("Dipertimbangkan :", round(dp, 2))
    st.write("Layak :", round(ly, 2))

    hasil = max(
        {"Tidak Layak": tl,
         "Dipertimbangkan": dp,
         "Layak": ly},
        key=lambda k: {
            "Tidak Layak": tl,
            "Dipertimbangkan": dp,
            "Layak": ly
        }[k]
    )

    st.success(f"Hasil Evaluasi: {hasil}")

# ==========================
# KASUS 3
# ==========================
elif menu == "Tingkat Kemacetan":

    st.header("Kasus 3 - Tingkat Kemacetan")

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
    st.write("Lancar :", round(l, 2))
    st.write("Padat :", round(p, 2))
    st.write("Macet :", round(m, 2))

    hasil = max(
        {"Lancar": l,
         "Padat": p,
         "Macet": m},
        key=lambda k: {
            "Lancar": l,
            "Padat": p,
            "Macet": m
        }[k]
    )

    st.success(f"Tingkat Kemacetan: {hasil}")
