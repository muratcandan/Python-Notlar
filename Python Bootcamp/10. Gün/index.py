# Python paketleri(package,library,module)
# built in(gömülü paketler) python içinde olan paketlerdir

# Kütüphaneler
import os
import random
import sys
# import numpy as np  # eğer kütüphaneyi kısaltma olarak kullanmak istersek as kullanılır
# from  import name, getcwd # tüm kütüphane yerine sadece 1 metodu çağırmak istersek
# from os import path as p # sadece 1 modül eklediğimizde de as ile kısaltabiliriz
# from os import * #paketteki her şeyi import eder. os.name yerine sadece name kullanılarak erişilebilir
"""
import hesapla  # kendi kütüphanemizi bu şekilde yaratabiliriz
print(hesapla.hesabim)  # kendi kütüphanemizden modüle ulaşma
print(hesapla.islem(10, 15))  # kendi modülümüz ile toplama
"""


# Random Kütüphanesi
"""
# random modulü 0-1 arasında bir sayı üretir
print(random.random())

# random() örneği
for i in range(5):
    print("{:.2f}".format(random.random()))

# uniform modülü verilen aralın arasında rastgele değer üretir
print(random.uniform(3.5, 6.5))

# randint modülü verilen değerler arasında tam sayı değeri veren modül
print(random.randint(0, 100))

# dir yapısı kütüphanenin içindeki modülleri görmemizi sağlar
# ayrıca ctrl basılı tutarak random'a basarsak paket içerisinde neler var VSC'de görebiliriz
print(dir(random))
"""

# Os kütüphanesi
"""
# Operating system üzerine kütüphanedir

# name modülü İşletim sistemi ismini gösterir
print(os.name)

# name örneği

if os.name == "posix":
    print("program düzgün çalışmaz")
else:
    print("windows düzgün çalışır ")

# makedirs modülü bulunduğu dizinde klasör oluşturur
os.makedirs("hops")

# getcwd modülü bulunduğu klasör adresini gösteren modül
print(os.getcwd())
"""

# Sys Kütüphanesi
"""
# version modülü python versionu gösterir
print(sys.version)
"""

# eğer sadece 1 metodu çağırdıysak tüm kütüphane yerine sadece isim kullanılabilir. Ancak eğer çakışma olursa başka paket ismiyle en son import edilen kabul edilir
"""
print(getcwd)  # kütüphane içerisinde sadece 1 metodu çağırırsak bu şekilde kullanılır
"""

# Dosya İşlemleri

# open dosya açmak için kullanılır
"""
a = open("deneme.txt", "w")  # yazılabilir dosya oluşturma
print(a)  # <_io.TextIOWrapper name='deneme.txt' mode='w' encoding='cp1254'>
a.write("python bootcamp")  # işlem yaptık
a.close()  # kapatıyoruz çünkü hala açılan dosya arka planda çalışır yük bindirir
a = open("deneme.txt, "r") # sadece okunabilir bir dosya oluşturur
print(a.read()) #dosya içeriğinin hepsini okur
print(a.read(5)) # içerisine girilen değer kadar byte'lık veri okur
print(a.readline()) #satır satır okumayı sağlar. Eğer içerik 3 satır biz 5 kere bu kodu yazarsak 2 satır boş döndürür
print(a.readlines()) #liste şeklinde döndürür
"""

# readline imleç nerede kaldıysa ordan okur
"""
print(a.readline())  #birinci satır
print(a.readline()) #ikinci satır
print("---)
print(a.read()) #üçüncü satır ve devamını okur
"""

# readlines() ile tüm listeye ulaşma
"""
b = a.readlines()

for i i,n b:
    print(i)

"""

# with kullanımı
# with ile dosyayı açtığında iş bittikten sonra dosyayı kapatır
"""
with open("deneme.txt", "r") as a: 
    print(a.readlines())
"""

# seek metodu
# imleci konumlandırmamızı sağlayan metod
"""
a = open("deneme.txt", "r")
print(a.readline())
print("----")
a.seek(0)  # imleç 0'a konumlanır
print(a.read())
a.close()
"""

# tell metodu
# imlecin bulunduğu konumu verir
"""
a = open("deneme.txt", "r")
print(a.readline())
print("---")
print(a.tell())
a.seek(a.tell() + 6)  # bulunduğumuz kısım yerine başka yerlere imleci götürdük
a.close()
"""

# write metodu
# verilerin üzerine yazar. Dikkat edilmesi gerekir tüm verileri silebiliriz
"""
a = open("deneme.txt", "w")
a.write("ali")
a.close()
"""

# a metodu
# a kipi dosya içeriğini değiştirmeden dosyanın sonuna ekleyerek yazar
# ancak okunma konusunda hata verdirtir. Okuma konusunda çok da makül değildir.
"""
a = open("deneme.txt", "a")
a.write("hop")
print(a.read())
a.close()
"""

# r => sadece okumak için
# w => sadece yazma için
# a => dosyanın sonuna yazmak için
# r+ => hem okumak hem yazmak için
# w+ => yazma ve okuma için
# a+ => hem eklemek hem okumak

# Örnek - 1
"""
a = open("deneme.txt", "r+")  # r+ imleci başa yerleştirerek ekleme yaptırır
b = a.readlines()
b.insert(2, "murat candan\n")  # üçüncü satıra ekleme yaptık
print(b)
a.seek(0)  # baş satıra döndük
a.writelines(b)
a.close()
"""

# closed() bool döner. Dosyanın açık olup olmadığını söyler ancak tam tersini söyler. Kapalı ise True, açık ise False
# readable() , writable() dosyanın okunabilir-yazılabilir olup olmadığını döner.
"""
a = open("deneme.txt", "r+")
print(a.closed)
print(a.readable())
print(a.writable())
"""

# Pdf formatı ile uğraşma
# Bunun için biraz internetten farklı kaynaklardan çalışmam lazım
"""
a = open("string.pdf", "rb")
c = a.read()
d = c.index(b"endstream")
e = c[d:d+50].decode("utf-8")
f = e.split("\n")
print(f[0])
"""

# Comprehension

# for döngüsü ile yeni liste yapma
"""
sayilar = [1, 2, 3, 4, 5, 6]

yeniListe = []

for sayi in sayilar:
    yeniListe.append(sayi)

print(yeniListe)
"""

# comprehension ile tek satırda yazılabilir
# ifade for değişken in liste
"""
sayilar = [1, 2, 3, 4, 5, 6]
liste = [sayi for sayi in sayilar]
print(liste)
"""

# comprehension olmadan Örnek - 1
"""
sayilar = [1, 2, 3, 4, 5, 6]
yeniListe = []

for sayi in sayilar:
    yeniListe.append(sayi*3)
print(yeniListe)
"""

# comprehension ile Örnek - 1
"""
sayilar = [1, 2, 3, 4, 5, 6]
liste = [sayi * 3 for sayi in sayilar]
print(liste)
"""

# comprehension olmadan Örnek - 2
"""
sayilar = [1, 2, 3, 4, 5, 6]
yeniListe = []

for sayi in sayilar:
    if sayi % 2 == 0:
        yeniListe.append(sayi)

print(yeniListe)
"""

# comprehension ile Örnek - 2
"""
sayilar = [1, 2, 3, 4, 5, 6]
liste = [sayi for sayi in sayilar if sayi % 2 == 0]
print(liste)
"""

# comprehension olmadan Örnek - 3

"""
sayilar = [1, 2, 3, 4, 5, 6]
yeniListe = []

for sayi in sayilar:
    if sayi % 2 == 0:
        yeniListe.append(sayi*sayi)

print(yeniListe)
"""

# comprehension ile Örnek - 3
"""
sayilar = [1, 2, 3, 4, 5, 6]
liste = [sayi * sayi for sayi in sayilar if sayi % 2 == 0]
print(liste)
"""

# comprehension olmadan Örnek - 4
"""
sayilar = [1, 2, 3, 4, 5, 6]
yeniListe = []

for sayi in sayilar:
    if sayi > 3 and sayi % 2 == 0:
        yeniListe.append(sayi*sayi)
print(yeniListe)
"""

# comprehension ile Örnek - 4
"""
sayilar = [1, 2, 3, 4, 5, 6]
liste = [sayi * sayi for sayi in sayilar if sayi > 3 and sayi % 2 == 0]
print(liste)
"""

# comprehension olmadan Örnek - 5
"""
sayilar_1 = [1, 2, 3, 4, 5, 6]
sayilar_2 = [1, 2, 3]
yeniListe = []

for sayi in sayilar_1:
    if sayi not in sayilar_2:
        yeniListe.append(sayi*2)

print(yeniListe)
"""

# comprehension ile Örnek - 5
"""
sayilar_1 = [1, 2, 3, 4, 5, 6]
sayilar_2 = [1, 2, 3]
liste = [sayi * 2 for sayi in sayilar_1 if sayi not in sayilar_2]
print(liste)
"""

# comprehension olmadan Örnek - 6
"""
sayilar = [[12, 23], [1, 2, 3], [34, 56, 67]]
yeniListe = []

for sayi in sayilar:
    for i in sayi:
        yeniListe.append(i)

print(yeniListe)
"""

# comprehension ile Örnek - 6
"""
sayilar = [[12, 23], [1, 2, 3], [34, 56, 67]]
liste = [i for sayi in sayilar for i in sayi]
print(liste)
"""

# comprehension olmadan Örnek - 7
# random kütüphanesinde _ olanlar dışındakileri kaldır örneği
"""
a = []

for i in dir(random):
    if i.startswith("_"):
        continue
    a.append(i)

for i in a:
    print(i)
"""

# comprehension ile Örnek - 7
"""
a = []

liste = [i for i in dir(random) if not i.startswith("_")]

print(liste)
"""

# comprehension olmadan Örnek - 8
# dict ile örnek
"""
sayilar = [1, 2, 3, 4, 5, 6]
yeniDict = {}

for sayi in sayilar:
    if sayi % 2 != 0:
        yeniDict[sayi] = sayi ** 2

print(yeniDict)
"""

# comprehension ile Örnek - 8
"""
sayilar = [1, 2, 3, 4, 5, 6]
dict2 = {sayi: sayi ** 2 for sayi in sayilar if sayi % 2 != 0}
print(dict2)
"""

# comprehension olmadan Örnek - 9
# set ile örnek
"""
sayilar = [1, 2, 3, 4, 5, 6]
yeniSet = set()

for sayi in sayilar:
    if sayi % 2 == 0:
        yeniSet.add(sayi)

print(yeniSet)
"""

# comprehension ile Örnek - 9
"""
sayilar = [1, 2, 3, 4, 5, 6]
set2 = {sayi for sayi in sayilar if sayi % 2 == 0}
print(set2)
"""
