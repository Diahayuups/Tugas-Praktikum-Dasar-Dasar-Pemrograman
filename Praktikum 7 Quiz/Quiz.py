print("Soal no. 1")

# inputan
kendaraan = input('''Masukkan jenis kendaraan anda :
            1. Mobil 
            2. Motor
            Masukkan Angka = ''')

jenis_bensin = input('''Pilih jenis bensin kendaraan anda : 
            1. Pertalite
            2. Pertamax
            3. Pertamax Turbo
            Masukkan Angka = ''')

kota = input ('''Ingin menuju kota apa ? 
            1. Jakarta
            2. Bekasi
            3. Depok
            4. Tangerang
            5. Bogor
            Masukkan Angka = ''')

match kendaraan:
    case '1':
        print("Baik, Anda akan mengendarai Mobil.")
    case '2':
        print("Baik, Anda akan mengendarai Motor.")

match jenis_bensin:
        case "1" | "pertalite" | "Pertalite" | "PERTALITE":
            tempuh = 12 
            harga = 10000
            print(f"{kendaraan}Anda menggunakan bensin Pertalite.")
        case "2"|"pertamax" | "Pertamax" | "PERTAMAX":
            tempuh = 13
            harga = 14000
            print(f"{kendaraan}Anda menggunakan bensin Pertamax.")
        case "3" | "pertamax turbo" | "PERTAMAX TURBO"|"Pertamax Turbo":
            tempuh = 13.5
            harga = 17000
            print(f"{kendaraan} anda menggunakan bensin Pertamax Turbo.")
        case _:
            print("salah inputnya, gaada angka itu dilist")

match kota:
    case "1"|"Jakarta":
        print("Anda menuju kota Jakarta")
        jarak = 20
    case "2"|"Bekasi":
        jarak = 35.7
        print("Anda menuju kota Bekasi")
    case "3"|"Depok":
        jarak = 5
        print("Anda menuju kota Depok")
    case "4"|"Tangerang":
        jarak = 99
        print("Anda menuju kota Tangerang")
    case "5"|"Bogor":
        jarak = 120.6
        print("Anda menuju kota Bogor")
    case _:
        print("tidak terdata")

pemakaian = jarak / tempuh
total_harga = pemakaian * harga

# output
print("")
print("Jadi, anda mengendarai",kendaraan)
print("dengan jenis bensin",jenis_bensin)
print("untuk menuju Kota",kota)

print("Dan anda akan menggunakan bensin sebanyak",pemakaian,"liter")
print("Total harga bensin yang dipakai adalah",total_harga,"rupiah")

print("-----------------------------------------------------------------------------------")

print("Soal no 2.")
# inputan
print('''Halo! Selamat Pagi!
    Sebelum memesan silahkan isi daftar pemesanan berikut''')
nama = input("Masukkan nama anda: ")
no_ponsel = input("Masukkan No Handphone anda: ")
pesan_menu = input('''Pesan Menu Apa? 
                    1. Makanan 
                    2. Minuman 
                    Masukan angka = ''')

if pesan_menu == "1":
    print('''Menu Makanan:"
            1. Nasi Goreng - Rp. 15,000
            2. Mie Goreng - Rp. 12,000
            3. Ayam Geprek - Rp. 18,000''')
    pesanan = input("Masukkan pesanan (e.g., Nasi Goreng): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan == "Nasi Goreng":
        harga_makanan = 15000
    elif pesanan == "Mie Goreng":
        harga_makanan = 12000
    elif pesanan == "Ayam Geprek":
        harga_makanan = 18000

    total_harga = harga_makanan * jumlah_pesanan
else:
    print(''''Menu Minuman:
            1. Aneka Jus - Rp. 15,000
            2. Soft Drink - RP. 10,000
            3. Sweet Ice Tea - RP. 5,000  ''')
    pesanan = input("Masukkan pesanan (e.g., Aneka Jus): ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan == "Aneka Jus":
        harga_minuman = 15000
    elif pesanan == "Soft Drink":
        harga_minuman = 10000
    elif pesanan == "Sweet Ice Tea":
        harga_minuman = 5000

    total_harga = harga_minuman * jumlah_pesanan

# Output
print("Nama Pembeli:", nama)
print("No Hp Pembeli:", no_ponsel)
print("Menu yang di Pesan:", pesanan)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus di bayarkan:", total_harga, "rupiah")

print("--------------------------------------------------------------------")

print("Soal no. 3")
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)