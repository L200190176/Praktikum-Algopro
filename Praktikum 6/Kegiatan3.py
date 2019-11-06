Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Tiara Danirmala"
>>> NIM = "L200190176"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> #Karena data "X" telah berubah menjadi type data integer
>>> type(b)
<class 'int'>
>>> #Karena data "Nama" memiliki instruksi "len"
>>> a / b
78.4
>>> #Karena hasil dari 1176 dibagi 15 adalah 78.4
>>> a // b
78
>>> #Karena arti dari "//" pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
1770
>>> #Karena nilai "a" dikurangi 999 adalah 177, kemudian dikalikan dengan 10 dan menghasilkan nilai 1770
>>> b ** 2
225
>>> #Karena arti dari "**" adalah perpangkatan
>>> a % b
6
>>> #Karena arti dari "%" adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #Karena 12.5 adalah bilangan desimal
>>> a / c
94.08
>>> #Karena hasil dari 1176 dibagi 12.5 adalah 94.08
>>> a // c
94.0
>>> #Karena arti dari "//" adalah pembagian dengan pembulatan ke bawah
>>> a % c
1.0
>>> #Karena arti dari "%" adalah sisa hasil bagi dan sisa dari 1176 dibagi 12.5 adalah 1.0
>>> c > b
False
>>> #Karena nilai "c" lebih besar dari nilai "b" adalah salah
>>> type(c > b)
<class 'bool'>
>>> #Karena c > b hanya memiliki dua kemungkinan yaitu True atau False
>>> a > b and b > c
True
>>> #Karena logika "DAN" True and True menghasilkan nilai True
>>> a > 1100 or b < 10
True
>>> #Karena logika "ATAU" True or False menghasilkan nilai True
>>> 
