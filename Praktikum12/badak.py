# SubClass / Child
from animal import *
class badak(animal):
    bercula = ""
    spesies_badak = ""

    def __init__(self, nama, makanan, hidup, berkembang_biak, bercula, spesies_badak):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bercula = bercula
        self.spesies_badak = spesies_badak

    def cetak(self):
        super().cetak()
        print("Badak ini Bercula:", self.bercula,
            "\nTermasuk Spesies :", self.spesies_badak,
            "\n--------------------------------------------------")
