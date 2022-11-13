class orang:
    def __init__(self,nama,gaji,karyawan):
        self.nama = nama
        self.gaji = gaji
        self.karyawan = karyawan

    def aku (self):
        print("nama :" + self.nama)
    
    def kamu (self):
        print ("gaji :" + str(self.gaji))

    def sum(self, total):
        self.TOTAL = 1+1
        print (TOTAL)
    
    def dia (self, karyawan):
        print("TOTAL KARYAWAN =" + str(self.karyawan))
    
    
LUTFI = orang ("LUTFI ARDIANSYAH",2000000,1)
WISNU = orang("WISNU SRI UTOMO", 100000,1)

LUTFI.aku ()
LUTFI.kamu ()
WISNU.aku()
WISNU.kamu()
print (sum)
