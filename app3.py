import streamlit as st

st.title("Sistem Pakar Diagnosa Penyakit Tanaman")

st.write("Pilih gejala pada tanaman:")

# Input gejala
daun_menguning = st.checkbox("Daun Menguning")
bercak_coklat = st.checkbox("Daun Bercak Coklat")
batang_busuk = st.checkbox("Batang Busuk")
tanaman_layu = st.checkbox("Tanaman Layu")
daun_berlubang = st.checkbox("Daun Berlubang")
pertumbuhan_lambat = st.checkbox("Pertumbuhan Lambat")
akar_membusuk = st.checkbox("Akar Membusuk")
daun_menggulung = st.checkbox("Daun Menggulung")

diagnosa = "Penyakit belum terdeteksi"

# Rule-based system
if daun_menguning and pertumbuhan_lambat:
    diagnosa = "Tanaman Kekurangan Nutrisi"

elif bercak_coklat and daun_menggulung:
    diagnosa = "Tanaman Terkena Jamur"

elif batang_busuk and akar_membusuk:
    diagnosa = "Tanaman Terkena Busuk Akar"

elif daun_berlubang:
    diagnosa = "Tanaman Terkena Hama Ulat"

elif tanaman_layu and daun_menguning:
    diagnosa = "Tanaman Kekurangan Air"

# Tombol diagnosa
if st.button("Diagnosa"):
    st.subheader("Hasil Diagnosa")
    st.success(diagnosa)
