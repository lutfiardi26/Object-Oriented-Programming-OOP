class orang:
    def __init__(self,nama,gaji,karyawan):
        self.nama = nama
        self.gaji = gaji
        self.karyawan = karyawan

    def aku (self):
        print("nama :" + self.nama)
        print ("gaji :" + str(self.gaji))
    
    def kamu(self, dia):
        self.karyawan += dia.karyawan
        print ("Total karyawan :" + str(self.karyawan))
    
    
LUTFI = orang ("LUTFI ARDIANSYAH",2000000,1)
WISNU = orang("WISNU SRI UTOMO", 100000,1)

LUTFI.aku ()
WISNU.aku ()
LUTFI.kamu(WISNU)
