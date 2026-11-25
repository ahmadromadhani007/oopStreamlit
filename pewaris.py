import streamlit as st

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    def harga_akhir(self):
        return self.harga
class ProdukFisik(Produk):
    def __init__(self, nama, harga, berat_kg):
        super().__init__(nama, harga)
        self.berat_kg = berat_kg
    def harga_akhir(self):
        return self.harga + (self.berat_kg * 10000)

class ProdukDigital(Produk):
    def harga_akhir(self):
        return super().harga_akhir() * 90 // 100

st.title("Aplikasi Penjualan Produk")
daftar = [ProdukFisik("Buku Cetak", 10000, 2), 
          ProdukDigital("Ebook", 10000)]
baris = []
for p in daftar:
    baris.append({"Produk": p.nama, "Harga Akhir": p.harga_akhir()})
st.table(baris)