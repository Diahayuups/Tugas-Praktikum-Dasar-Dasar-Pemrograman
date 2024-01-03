# 1. buatlah fungsi untuk menampilakan data diri :
# contoh pemanggilan : profil(nama, alamat, gender, umur, hoby)

# 2. buatlah fungsi untuk mencari kelulusan nilai dari berikut : 
# jika nilai < 60 maka gagal 
# jika nilai = 61 - 70 maka baik 
# jika nilai = 71 - 80 maka sangat baik 
# jika nilai = 81 - 100 maka istimewa 
# ex:
# nilai (60)

# 3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
# ex : ganjil (100)

print("Soal no. 1")
def profil(nama, alamat, gender, umur, hoby):
    print("Nama saya adalah", nama)
    print("Saya tinggal di", alamat)
    print("Saya adalah seorang", gender)
    print("Saya berusia", umur)
    print("Saya gemar", hoby)

profil("Diah ayu puspasari", "Dramaga, Bogor", "Perempuan", "18 Tahun", "Mendengarkan musik")

print("---------------------------------------------------------------------------------------------------------------------------------")

print("Soal no. 2")
def validasi_nilai(nilai):
    if nilai < 60 :
        return "Gagal"
    elif 61 <= nilai <= 70 :
        return "Baik"
    elif 71 <= nilai <= 80 :
        return "Sangat Baik"
    elif 81 <= nilai <= 100 :
        return "Istimewa"
    else :
        return "Silahkan Input Ulang"

nilai = float(input("Masukan Nilai Anda :"))
hasil = validasi_nilai(nilai)
print(f"Hasil anda :{hasil}")

print("--------------------------------------------------------------------------------------------------------------------------------")

print("Soal no. 3")
def ganjil(b):
    for i in range(1, b+1, 2):
        print(i)

ganjil(100)
