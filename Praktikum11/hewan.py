from animal import *

# membuat object

katak = animal(4, 'memiliki paru paru', 'tidak berbulu', 'amfibi')
kucing = animal(4, 'memiliki paru paru', 'memiliki bulu yang lebat', 'mamalia')
merpati = animal(2, 'memiliki paru paru', 'memiliki bulu untuk terbang', 'avest')

print(animal.BKSDA,
        '\n=================================')

katak.cetak()
kucing.cetak()
merpati.cetak()