##Program Akun
##Dibuat oleh Tiara L200190176
import random
angka = random.randint(0,1000)


Nama = "Tiara Danirmala"
TanggalLahir = "2 Mei 2000"
NamaSingkat = Nama[0] + "." + Nama[6:16]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[6:10]
Password = Nama[0:5] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)

