# Modul 2 Buatlah 10 Operasi Aritmatika 

import math
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print('Penjumlahan :',bil1, '+', bil2, '=', hasil)

def kurang(bil1, bil2):
    hasil = bil1 - bil2
    print('Pengurangan :',bil1, '-', bil2, '=', hasil)

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print('Penbagian :',bil1, '/', bil2, '=', hasil)

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print('Perkalian :',bil1, '*', bil2, '=', hasil)

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print('Perpangkatan :',bil1, '**', bil2, '=', hasil)

def log(bil1):
    hasil = math.log(bil1)
    print('Hasil dari log :',bil1, '=', hasil)

def akar(bil1):
    hasil = math.sqrt(bil1)
    print('Hasil dari akar :',bil1, '=', hasil)

def sin(bil1):
    hasil = math.sin(bil1)
    print('Hasil dari sin :',bil1, '=', hasil)

def cos(bil1):
    hasil = math.cos(bil1)
    print('Hasil dari cos :',bil1, '=', hasil)

def tan(bil1):
    hasil = math.tan(bil1)
    print('Hasil dari tan :',bil1, '=', hasil)