import streamlit as st

# ---------------- STYLE ----------------
st.set_page_config(page_title="Sistem Penilaian", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        color: #4CAF50;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- RULE ----------------
def hitung_nilai(nilai):
    if nilai >= 85:
        return "A", "Sangat Baik"
    elif nilai >= 70:
        return "B", "Baik"
    elif nilai >= 60:
        return "C", "Cukup"
    else:
        return "D", "Kurang"

# ---------------- DATA ----------------
if "data" not in st.session_state:
    st.session_state["data"] = []

if "login" not in st.session_state:
    st.session_state["login"] = False

# ---------------- LOGIN ----------------
def login():
    st.markdown('<p class="title">🔐 Login Sistem</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username.strip().lower() == "admin" and password.strip() == "123":
                st.session_state["login"] = True
                st.success("Login berhasil!")
            else:
                st.error("Username / Password salah!")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- APP ----------------
def app():
    st.markdown('<p class="title">📊 Sistem Penilaian Mahasiswa</p>', unsafe_allow_html=True)

    menu = st.sidebar.selectbox("Menu", ["Dashboard", "Tambah Data", "Data Mahasiswa"])

    # DASHBOARD
    if menu == "Dashboard":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📈 Statistik")

        total = len(st.session_state["data"])
        st.write("Total Mahasiswa:", total)

        st.markdown('</div>', unsafe_allow_html=True)

    # TAMBAH DATA
    elif menu == "Tambah Data":
        st.markdown('<div class="card">', unsafe_allow_html=True)

        nama = st.text_input("Nama Mahasiswa")
        nilai = st.slider("Nilai", 0, 100)

        if st.button("Simpan"):
            grade, ket = hitung_nilai(nilai)

            st.session_state["data"].append({
                "nama": nama,
                "nilai": nilai,
                "grade": grade,
                "ket": ket
            })

            st.success("Data berhasil disimpan!")

        st.markdown('</div>', unsafe_allow_html=True)

    # DATA
    elif menu == "Data Mahasiswa":
        st.markdown('<div class="card">', unsafe_allow_html=True)

        for i, d in enumerate(st.session_state["data"]):
            st.write(f"**{d['nama']}** | {d['nilai']} | {d['grade']} | {d['ket']}")

            col1, col2 = st.columns(2)

            if col1.button("Hapus", key=f"h{i}"):
                st.session_state["data"].pop(i)
                st.warning("Data dihapus!")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MAIN ----------------
if st.session_state["login"]:
    app()
else:
    login()
