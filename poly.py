import streamlit as st
from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r
    def luas(self):
        return round(3.14 * self.r ** 2, 2)

baris = []
for b in [Persegi(4), Lingkaran(7)]:
    baris.append({"Bentuk": type(b).__name__, "Luas": b.luas()})
st.table(baris)