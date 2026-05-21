import streamlit as st

# Konfigurasi
st.set_page_config(
    page_title="Sistem Cerdas Diagnosa Penyakit",
    page_icon="🏥"
)

# Judul
st.title("🏥 Sistem Cerdas Diagnosa Penyakit")
st.write("Pilih gejala yang kamu rasakan")

st.markdown("---")

# Input Gejala
demam = st.checkbox("Demam")
batuk = st.checkbox("Batuk")
pilek = st.checkbox("Pilek")
sakit_kepala = st.checkbox("Sakit Kepala")
mual = st.checkbox("Mual")

# Tombol Diagnosa
if st.button("Diagnosa"):

    # Sistem Cerdas IF ELSE
    if demam and batuk and pilek:
        st.success("Kemungkinan Penyakit: Flu 🤧")
        st.info("Saran: Istirahat dan minum obat flu")

    elif demam and sakit_kepala and mual:
        st.warning("Kemungkinan Penyakit: Demam Berdarah 🦟")
        st.info("Saran: Segera periksa ke dokter")

    elif batuk and pilek:
        st.success("Kemungkinan Penyakit: Batuk Pilek 🤒")
        st.info("Saran: Minum obat dan istirahat")

    elif demam:
        st.warning("Kemungkinan Penyakit: Demam 🔥")
        st.info("Saran: Banyak minum air putih")

    else:
        st.info("Gejala belum cukup untuk diagnosa")

# Footer
st.markdown("---")
st.write("Sistem Cerdas Diagnosa Penyakit Sederhana")
