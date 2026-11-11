import streamlit as st

class Kalkulator:
    def tambah(self, a, b, c=0):
        return a + b + c
    def jumlah(self, *angka):
        return sum(angka)
k = Kalkulator()
st.write(k.tambah(1, 2))
st.write(k.tambah(1, 2, 3))
st.write(k.jumlah(1, 2, 3, 4, 5))