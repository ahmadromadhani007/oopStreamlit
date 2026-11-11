import streamlit as st

class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return '...'

class Kucing(Hewan):
    def suara(self):
        return "Meonggg"

class Ayam(Hewan):
    def suara(self):
        return "Crukuukkkk"

pilihan = st.selectbox("Pilih hewan anda !", ["Kucing", "Ayam", "Serangga/Hewan Umum"])
daftar = {"Kucing": Kucing, "Ayam": Ayam, "Serangga/Hewan Umum": Hewan}
h = daftar[pilihan]("Mini")
st.write(f"{h.nama} berkata: {h.suara()}")        
        