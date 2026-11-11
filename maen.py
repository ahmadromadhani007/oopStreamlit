import streamlit as st

class Kendaraan:
    def __init__(self, nama, tarif):
        self.nama = nama
        self.tarif = tarif
    def hitung_biaya(self, hari):
        return self.tarif * hari

class MobilMewah(Kendaraan):
    def hitung_biaya(self, hari):
        biaya = super().hitung_biaya(hari)
        return biaya + 100000

jenis = st.selectbox("Jenis Kendaraaan", ["Motor", "Mobil Mewah"])
hari = st.number_input("Lama Sewa (hari)", min_value=1, value=1)
if jenis == "Motor":
    k = Kendaraan(" PCX", 80000)
else:
    k = MobilMewah(" Alphard", 900000)

st.write(f"Biaya sewa{k.nama}: Rp{k.hitung_biaya(hari):,.0f}")