#  class harus ada di atas/awal
class mahasiswa():
    nama = 'nama'

    def belajar(self):
        print(self.nama, 'Sedang belajar Python Class')

    def tidur(self, kondisi):
        print(self.nama, 'Tidur di kelas', kondisi)
# main programnya
diah = mahasiswa()
eka = mahasiswa()
nuy = mahasiswa()
tata = mahasiswa()

diah.nama = "Diah ayu puspasari"
eka.nama = "Eka kartini"
nuy.nama = "Nurhayati"
tata.nama = "Octaviani Salsabila"

diah.belajar()
eka.belajar()
nuy.belajar()
tata.belajar()
print("--------------------------------------------------")

diah.tidur("dari pagi")
eka.tidur("matkul pertama")
nuy.tidur("matkul kedua")
tata.tidur("matkul akhir")
