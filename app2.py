import streamlit as st

st.title("💻 Sistem Rekomendasi Laptop")

# Input user
budget = st.number_input("Masukkan Budget (juta)", min_value=1)
kebutuhan = st.selectbox("Kebutuhan", ["Office", "Gaming", "Desain"])
ram = st.selectbox("RAM", ["4GB", "8GB", "16GB"])
storage = st.selectbox("Storage", ["HDD", "SSD"])
ringan = st.radio("Butuh laptop ringan?", ["Ya", "Tidak"])

# Rule-based system
if st.button("Rekomendasi"):
    if budget < 7 and kebutuhan == "Office":
        st.success("👉 Rekomendasi: Laptop Basic (Cocok untuk Office)")
    
    elif budget > 10 and kebutuhan == "Gaming":
        st.success("👉 Rekomendasi: Laptop Gaming (RTX/GTX)")
    
    elif kebutuhan == "Desain" and ram in ["8GB", "16GB"]:
        st.success("👉 Rekomendasi: Laptop Desain (Core i5/i7, GPU)")
    
    elif ringan == "Ya":
        st.success("👉 Rekomendasi: Ultrabook Ringan")
    
    elif storage == "SSD":
        st.success("👉 Rekomendasi: Laptop dengan SSD (Lebih Cepat)")
    
    else:
        st.warning("👉 Rekomendasi tidak ditemukan, coba ubah input")