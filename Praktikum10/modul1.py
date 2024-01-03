# Modul 1 Buatlah luas dan keliling bangun datar (minimal 7)

print("----------------------------------------Tugas Praktikum 11----------------------------------------------")
print("Nama : Diah ayu puspasari")
print("NIM : 0110223052")
print("Teknik Informatika 2302")
print("--------------------------------------------------------------------------------------------------------")

def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print('luas persegi :', sisi,'*', sisi, '=', luas)
    print('keliling persegi :', '4', '*', sisi, '=', keliling)

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print('luas persegi panjang :', panjang,'*', lebar, '=', luas)
    print('keliling persegi :', '2', '*', panjang,'+', lebar, '=', keliling)

def segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    keliling = 3 * alas
    print('luas segitiga :', alas, '*', tinggi, '/ 2','=', luas)
    print('keliling segitiga :', '3', '*', alas, '=', keliling)

def jajargenjang(alas, tinggi):
    luas = alas * tinggi
    keliling = 2 * (alas * tinggi)
    print('luas jajargenjang :', alas, '*', tinggi, '=', luas)
    print('keliling jajargenjang :', '2', '*', tinggi, '=', keliling)

def lingkaran(jari_jari):
    luas = 3,14 * jari_jari**2
    keliling = 2 * 3,14 * jari_jari
    print('luas lingkaran :', '3,14', '*', jari_jari, '**', '2', '=', luas)
    print('keliling lingkaran :', '2', '*', '3,14', '*', jari_jari,'=', keliling)

def belah_ketupat(diagonal_1, diagonal_2, sisi):
    luas = 0.5 * diagonal_1 * diagonal_2
    keliling = 4 * sisi
    print('luas belah ketupat :', '0.5', '*', diagonal_1,'*', diagonal_2, '=', luas)
    print('keliling belah ketupat :', '4', '*', sisi, '=', keliling)

def layang_layang(diagonal_1, diagonal_2, sisi1, sisi2):
    luas = 0.5 * diagonal_1 * diagonal_2
    keliling = 2 * (sisi1 + sisi2)
    print('luas layang-layang :', '0.5', '*', diagonal_1, '*', diagonal_2, '=', luas)
    print('keliling layang-layang :', '2', '*', (sisi1,'+', sisi2), '=', keliling)