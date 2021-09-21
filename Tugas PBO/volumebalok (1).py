#volume balok 

class VolumeBalok:
    Panjang = None
    Lebar = None
    Tinggi = None

#membangun instance/variable sebagai "objek nyata"
VB = VolumeBalok()
VolumeBalok.Panjang = 12
VolumeBalok.Lebar = 6
VolumeBalok.Tinggi = 8

Hasil = VolumeBalok.Panjang*VolumeBalok.Lebar*VolumeBalok.Tinggi

#output yang akan ditampilkan
print("Panjang Balok : ", VolumeBalok.Panjang)
print("Lebar Balok : ", VolumeBalok.Lebar)
print("Tinggi Balok : ", VolumeBalok.Tinggi)
print("Hasil Volume Balok : ", Hasil) 