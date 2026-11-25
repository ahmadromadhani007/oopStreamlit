import streamlit as st

st.title("Nama Aplikasi yang dibuat")
nama = st.text_input("Masukkan nama aplikasi")
if st.button("Proses"):
    st.write(f"Sistem anda adalah {nama}")