# Object Inhertance 
from animal import *
from ikan import *
from badak import *
from ular import *

#  Membuat objek
print(f"="*50)

i1 = ikan('Ikan Koi', 'Pur Ikan','Perairan yang Bersih', 'Ovipar', 'Metalik Emas', 'Koi Ogon')
i2 = ikan('Ikan Salmon', 'Daging', 'di Air tawar & Laut',  'Ovipar', 'Merah Cerah', 'Salmon Sockeye')

i1.cetak()
i2.cetak()

print(f"="*50)

b1 = badak('Badak Jawa', 'Berbagai jenis tanaman', 'Hutan hujan daratan rendah', 'Vivipar', 'Satu', 'Rhinoceros Sondaicus')
b2 = badak('Badak Sumatera', 'Buah', 'Hutan rawa dataran rendah', 'Vivipar', 'Dua', 'Dicerorhinus Sumatrenis')

b1.cetak()
b2.cetak()

print(f"="*50)

u1 = ular('Ular Karpet', 'Hewan kecil', 'Padang rumput & Hutan', 'Ovipar', 'Pythonidae - Tidak berbisa', '1,5 s/d 3 meter')
u2 = ular('Ular Cobra', 'Hewan kecil', 'Hutan', 'Ovipar', 'Naja sputatrix- Berbisa', '1 s/d 1,5 meter')

u1.cetak()
u2.cetak()

print(f"="*50)

print('''Nama : Diah Ayu Puspasari
NIM : 0110223052
Rombel : Teknik Informatika 2302''')