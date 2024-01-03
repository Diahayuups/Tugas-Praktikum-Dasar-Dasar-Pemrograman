# SubClass / Child
from animal import *
class ikan(animal):
    warna_ikan = ""
    jenis_ikan = ""

    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak(self):
        super().cetak()
        print("Warna Ikan \t :", self.warna_ikan,
            "\nJenis ikan \t :", self.jenis_ikan,
            "\n--------------------------------------------------")
