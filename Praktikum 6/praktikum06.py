print("Tugas Praktikum 06")
print("--------------------------------------------------------------------------------------------------------------------------------")

print('''Nama : Diah Ayu Puspasari
      Teknik Informatika 2302
      0110223052''')

#1. Print semua bilangan ganjil dari list berikut, hentikan perulangan ketika sudah melewati bilangan 553. Pakai perulangan while. 
#   numbers = [
#   951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 
#   501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 
#   236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 
#   248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 
#   831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]

#2. Buat lah output dari menggunakan bahasa pemprograman python dengan : 
#   1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 = ….

#3. Buat program untuk minta input jumlah baris dan buat rangkaian berikut ini
#   *
#   **
#   ***
#   ****
#   Dan seterusnya sejumlah baris yang diinputkan
#   Gunakan for loop dengan range

print ("1.")
index = 1
numbers = [ 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527 ]

# Menggunakan loop while untuk mencetak bilangan ganjil sampai bertemu dengan 553
while index < len(numbers):
    if numbers[index] % 2 != 0:  # Cek apakah bilangan ganjil
        print(numbers[index])
        if numbers[index] == 553:  # Hentikan perulangan jika sudah mencapai 553
            break
    index += 1

print("")

print("--------------------------------------------------------------------")

print ("2.")
y = 0
for i in range(1,20,2):
    y += i
print("Hasil penjumlahan bilangan ganjil dari 1 sampai dengan 19 adalah:", y)

print("--------------------------------------------------------------------")
print ("3.")
string = " "
bar = 1

x = int (input("masukan angka = "))

#looping baris
while bar <= x:
    kol = bar

    #looping kolom
    while kol > 0:
        string = string + "*"
        kol = kol - 1
    string = string + "\n"
    bar = bar + 1
    print(string)
