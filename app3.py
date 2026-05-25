import streamlit as st

st.title("Sistem Pakar Diagnosa Penyakit")

st.write("Pilih gejala yang dialami:")

# Input gejala
demam = st.checkbox("Demam")
batuk = st.checkbox("Batuk")
sakit_tenggorokan = st.checkbox("Sakit Tenggorokan")
sesak_napas = st.checkbox("Sesak Napas")
hidung_tersumbat = st.checkbox("Hidung Tersumbat")
sakit_kepala = st.checkbox("Sakit Kepala")
mual = st.checkbox("Mual")
diare = st.checkbox("Diare")

diagnosa = "Belum ditemukan penyakit yang sesuai"

# Rule-based system
if demam and batuk and sakit_tenggorokan:
    diagnosa = "Flu"

elif demam and sesak_napas and batuk:
    diagnosa = "COVID-19"

elif hidung_tersumbat and sakit_tenggorokan:
    diagnosa = "Common Cold"

elif mual and diare and sakit_kepala:
    diagnosa = "Keracunan Makanan"

elif demam and sakit_kepala and mual:
    diagnosa = "Demam Berdarah"

# Tombol diagnosa
if st.button("Diagnosa"):
    st.subheader("Hasil Diagnosa")
    st.success(diagnosa)
