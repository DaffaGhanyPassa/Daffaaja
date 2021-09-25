#Superclass
class Pendidikan():
    
    def __init__(self, nama_sekolah, alamat_sekolah ) :
        self.nama_sekolah = nama_sekolah
        self.alamat_sekolah = alamat_sekolah

#Subclass Pendidikan Sekolah Menengah Pertama dan Sekolah Menengah Atas
class Pendidikan_SekolahMenengahPertama(Pendidikan):
    pass

class Pendidikan_SekolahMenengahAtas(Pendidikan):
    pass

SDNWILULANG = Pendidikan("SDNWILULANG", "CILEGON")
SMPN6CILEGON = Pendidikan_SekolahMenengahPertama("SMPN6CILEGON", "CILEGON")
MAN2CILEGON = Pendidikan_SekolahMenengahAtas("MAN2CILEGON", "CILEGON")

#Output
print(SDNWILULANG.nama_sekolah, SDNWILULANG.alamat_sekolah)
print(SMPN6CILEGON.nama_sekolah, SMPN6CILEGON.alamat_sekolah)
print(MAN2CILEGON.nama_sekolah, MAN2CILEGON.alamat_sekolah)
