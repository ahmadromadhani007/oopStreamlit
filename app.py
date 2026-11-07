import streamlit as st

class Produk:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga
    @property
    def nama(self):
        return self.__nama
    @property
    def harga(self):
        return self.__harga
if 'daftar' not in st.session_state:
    st.session_state.daftar = []

nama = st.text_input("Nama Produk")
harga = st.number_input("Harga", min_value=1)
if st.button('Tambah'):
    st.session_state.daftar.append(Produk(nama, harga))
for p in st.session_state.daftar:
    st.write(f'{p.nama} - Rp{p.harga:,.0f}')