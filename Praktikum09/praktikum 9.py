print("Nama : Diah Ayu Puspasari")
print("NIM : 0110223052")
print("Rombel : TI2302")
print("------------------------------------------------------------------------------------------------------------------------------")

print("------------------------------------------------Praktikum DDP Pekan 09--------------------------------------------------------")
print("No. 1")
# Buat fungsi untuk menampilkan nama2 siswa yang lulus saja dari hasil_akhir di slide sebelumnya (nilai > 65)
# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}]
# lulus_saja(hasil_akhir) hasilnya:[‘Reza’, ‘Dian’]

hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}]

def lulus_saja(hasil_akhir):
    siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]
    return siswa_lulus

hasil = lulus_saja(hasil_akhir)
print("hasil:", hasil)

print("------------------------------------------------------------------------------------------------------------------------------")
print("No. 2")
# Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an menggunakan for dan materi yang sudah diajarkan. 
# (tidak boleh pakai fungsi dari python).
# balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) hasilnya :['jambu','durian', 'pisang', 'mangga', 'pepaya']

buah2an = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def balikan(buah2an) :
    buah_terbalik = []
    for i in range (len(buah2an) -1, -1, -1) :
        buah_terbalik.append(buah2an[i])
    return buah_terbalik

hasil_terbalik = balikan(buah2an)
print("hasilnya:", hasil_terbalik)

print("------------------------------------------------------------------------------------------------------------------------------")
print("No. 3")
# Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi terduplikasi.
# duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) 
# Hasilnya: ['pepaya', 'pepaya', 'mangga', 'mangga', 'pisang', 'pisang', 'durian','durian', 'jambu', 'jambu']

buah_awal= ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikat(buah_awal) :
    buah_duplikat = []
    for buah in buah_awal :
        buah_duplikat.extend([buah, buah])
    return buah_duplikat

hasil_duplikat = duplikat(buah_awal)
print("hasil:", hasil_duplikat)

print("------------------------------------------------------------------------------------------------------------------------------")
print("No. 4")
# Buat fungsi untuk membuat string baru berisi hanya konsonan dari string fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"

kalimat_awal = "Nurul Fikri"

def fungsi(kalimat_awal): 
    vokal = 'aiueoAIUEO' 
    hasil = ""
    for huruf in kalimat_awal: 
        if huruf not in vokal: 
            hasil += huruf 
    return hasil 

hasil_konsonan = fungsi(kalimat_awal)
print("Hasilnya:", hasil_konsonan)

