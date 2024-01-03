#  SuperClass / Parent
class animal:
    nama = ""
    makanan = ""
    hidup = ""
    berkembang_biak = ""

    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print("Nama hewan \t :", self.nama,
            "\nMakanan \t :", self.makanan,
            "\nHidup di \t :", self.hidup,
            "\nBerkembang biak  :", self.berkembang_biak)