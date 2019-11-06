Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Tiara Danirmala"
>>> NIM = 176
>>> Tinggi = 1.60
>>> Berat = 56
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> #Karena data "Aku" ditulis dengan menggunakan tanda kurung biasa dan item di dalamnya tidak dapat diubah
>>> Aku[0]
2000
>>> #Karena item pertama dari data "Aku" adalah "TahunLahir", dan nilai dari "TahunLahir" adalah 2000
>>> a = NIM % 4; Aku[a]
2000
>>> #Karena sisa hasil dari 176 dibagi 4 adalah 0, jadi hasil dari Aku[0] adalah 2000
>>> type(Aku[a])
<class 'int'>
>>> #Karena Aku[0] adalah "TahunLahir" dan nilainya 2000, 2000 adalah tipe data integer
>>> Aku[a:4]
(2000, 56, 1.6, 176)
>>> #Karena 4 item pertama dari data "Aku" adalah "TahunLahir", "Berat", "Tinggi", "NIM"
>>> type(Aku[4])
<class 'str'>
>>> #Karena item ke-lima dari data "Aku" adalah "Nama", dan nilai dari "Nama" adalah "Tiara Danirmala"
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> #Karena isi tuple tidak dapat diubah (immutable) sehingga terjadi error
>>> type(Data)
<class 'list'>
>>> #Karena data "Data" ditulis dengan menggunakan kurung siku dan koleksi item didalamnya dapat berubah, bertambah dan berkurang secara dinamis
>>> type(Data[4])
<class 'str'>
>>> #Karena item ke-lima dari data "Data" adalah "Nama", dan nilai dari "Nama " adalah "Tiara Danirmala"
>>> Data[4][5]
' '
>>> #Karena Data[4] atau objek ke-lima dari "Data" adalah "Nama" dan indeks 5 dari "Nama" adalah " " atau spasi
>>> Data[4][a:6]
'Tiara '
>>> #Karena Data[4] adalah "Nama" dan Nama[0:6] adalah objek pertama sampai objek ke-enam dari data "Nama" yaitu "Tiara "
>>> Data[0] = "ok"; Data
['ok', 56, 1.6, 176, 'Tiara Danirmala']
>>> #Karena list merupakan tipe data koleksi di mana objeknya dapat berubah (mutable)
>>> Data[-a]
'ok'
>>> #Karena a adalah 0 jadi indeks 0 dari "Data" adalah objek pertama yaitu "ok"
>>> range(a)
range(0, 0)
>>> #Karena a adalah 0 jadi range(0) menghasilkan range 0 sampai 0

>>> 
