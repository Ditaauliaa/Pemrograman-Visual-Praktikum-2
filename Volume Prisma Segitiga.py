# Dita Aulia Oktavian
# 20051397020
# MI2020B

class hasil :
    def hitung (angka):
        print (' ')
        print ('Panjang alas   : ', angka.bil1)
        print ('Tinggi         : ', angka.bil2)
        print ('Tinggi prisma  : ', angka.bil3)
        print (' ')
        print ('Volume Prisma Segitiga :', (1/2*angka.bil1*angka.bil2)*angka.bil3)
        print (' ')

        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang alas  : '))
        self.bil2 = int(input('Masukan Tinggi        : '))
        self.bil3 = int(input('Masukan Tinggi Prisma : '))
        



coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ("Menghitung Volume Prisma Segitiga")
    print (' ')
    
    objek = nilai()
    objek.hitung()
    print(' ')
    coba = input('Mau Menghitung Lagi : ')
    if coba == ('y') or coba == ('Y') :
        print (' ')
        continue
    elif coba == ('n') or coba == ('N') :
        print ('Terima Kasih')
        break
    else :
        print ('Pilihan yang Anda Masukan Salah')
        break
