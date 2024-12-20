import streamlit as st
from PIL import Image

# Halaman Utama
st.set_page_config(page_title="Curriculum Vitae", layout="centered")

# Foto dan Informasi Dasar
st.title("Curriculum Vitae")
foto = Image.open("foto.jpg")
st.image(foto, width=200)

# Biodata
st.header("Biodata")
st.write("""
- **Nama:** Zulham
- **Alamat:** Kota Bandung
- **Email:** dzoelham[at]gmail.com
""")

# Navigasi ke Halaman Tambahan
st.sidebar.title("Navigasi")
st.sidebar.write("""
Pilih halaman untuk melihat lebih detail:
- Pendidikan
- Pengalaman Kerja
- Pengalaman Pelatihan
- Skill
""")
