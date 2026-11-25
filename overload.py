import streamlit as st

class Kasir:
    def total(self, diskon=0, *biaya):
        total_biaya = sum(biaya)
        return total_biaya - total_biaya * diskon // 100

harga = st.number_input("Harga", min_value=1, value=100000)
diskon = st.number_input("Diskon (%)", min_value=0, value=10)
k = Kasir()
st.write(f"Tanpa diskon: {k.total(0, harga)}")
st.write(f"Dengan diskon: {k.total(diskon, harga)}")
st.write(f"Diskon + ongkir: {k.total(diskon, harga, 15000)}")