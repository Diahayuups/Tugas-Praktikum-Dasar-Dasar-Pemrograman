#Lets Code

#1. Buat variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, warna kendaraan, roda kendaraan]
#   Tambahkan dari list tersebut di belakang dengan value :
#       [harga kendaraan, tipe kendaraan]
#   Tambahkan setelah jenis kendaraan dengan value [merk kendaraan]

#2. Buat Program python dengan match case untuk menghitung luas bangun datar :
#   jika pilih 1, maka menghitung luas persegi
#   jika pilih 2, maka menghitung luas lingkaran
#   jika pilih 3, maka menghitung luas segitiga
#   selain pilihan di atas maka keterangan : salah pilih angka

#print("1.") 
#mobil = ["GranCabrio", "kendaraan darat", "4691cc", "kuning", "beroda 4"]
#mobil.append("4 Milyar")
#mobil.append("Automatic")    
#mobil.insert(2, "Maserati GrandCabrio")
#print(mobil)

print("-------------------------------------------------------------------------------------------------")

print("2.")
ket = '''Selamat datang di aplikasi menghitung luas bangun datar
    masukan Opsi :
    1. Menghitung luas Persegi
    2. Menghitunng luas lingkaran
    3. Menghitung luas segitiga
    '''

Opsi = input (ket)

match Opsi:
    case "1":
        print("Luas Persegi")
        sisi = int (input ("masukan nilai sisi"))
        luasP = sisi * sisi
        print("luas persegi =", luasP )
    case "2":
        print("Luas Lingkaran")
        jari2 = int (input ("masukan nilai jarii jari"))
        luasL = 3.14 * jari2 * jari2
        print("luas lingkaran =", luasL)
    case "3":
        print("Luas Segitiga")
        alas = int (input ("masukan nilai alas"))
        tinggi = int (input ("masukan nilai tinggi"))
        luasS = 0.5 * alas * tinggi
        print("luas segitiga =", luasS)
    case _:
        print("salah memilih Opsi")
        