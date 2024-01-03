# SubClass / Child
from animal import *
class ular(animal):
    jenis_ular = ""
    panjang_ular = ""

    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_ular, panjang_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_ular =  jenis_ular 
        self.panjang_ular = panjang_ular

    def cetak(self):
        super().cetak()
        print("Ular ini berjenis:", self. jenis_ular,
            "\nDengan panjang \t :", self.panjang_ular, "meter"
            "\n--------------------------------------------------")
