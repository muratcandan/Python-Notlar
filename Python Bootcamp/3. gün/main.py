#input kullanıcıdan girdi almayı sağlar:
""""
a = input( "Lütfen Doğum yılınızı  Giriniz:" )
print( "Yaşınız", 2022 - int ( a ) )
"""
#İnput örneği:
""""
sayi_1 = int(input("Birinci Sayı"))
sayi_2 = int(input("İkinci Sayı"))

topla = sayi_1 + sayi_2

print( "Birinci sayınız {} ve ikinci sayınız {} toplam sayınız {}" .format(sayi_1,sayi_2,topla) )
"""""

#Karekök bulan program:
"""""
sayi = int(input("Bir sayı giriniz:"))
karekok = sayi ** (0.5)
print("Sayınız {} ve sayınızın karekökü {} " .format(sayi,karekok))
"""
#Geçici değişken ile yer değiştirme(swap) işlemi
"""""
a = 10
b = 15
tmp = a
a = b
b = tmp 
print(a, b)
"""
#Diğer swap yöntemi
"""""
a = 10
b = 15
a = a + b
b = a - b
a = a - b
print(a , b)
"""
#Beden kitle endeksi hesaplama
"""""
kilo = float(input("Kilonuzu Giriniz:"))
boy = float(input("Boyunuzu Giriniz(m):"))
bki = kilo / (boy ** 2)
print("Beden kitle endeksiniz: " , bki)
"""
#Vize Notu - Final Notu Ortalaması
"""""
vizeNotu= float(input("Vizednizi Giriniz:"))
finalNotu= float(input("Finalinizi Giriniz:"))
ortalama = (vizeNotu * 0.4) + (finalNotu * 0.6)
print(ortalama)
"""
#List (Arrray) yapısı
"""""
ogrenciler = ["Bartu" , "Beste" , "İnci"]
print (ogrenciler)
notlar = ["ali" , 2 , True , 3.14 , (5 + 3j)]
print(type ( notlar ) )

a = "Murat"
b = list(a)
print(b)

c = ["a" , [10 , 20 , []] , [1 , 2 , 3 , [15 , 30]]]

print(c)
print(c[2])
print(c[-2])
print(c[1][0])

# istediğimiz değerden başlayıp hedef değere kadar gitmek : ile sağlanır
d = [1 , 2 , 3 , 4 , 5 , 6]
print(d[1:4])
#değer değiştirmek
d[0] = 99
print(d)
#sona değer eklemek istersek .append
d.append(55)
print(d)
#belirtilen indexe eleman eklemek için .insert
d.insert(2,77)
print(d)

#listeleri birleştirmek için extent
a = [3 , 5 , 7 ]
b = [9 , 11 , 13]
a.extend(b)
print(a)
#diğer liste birleştirme yolu
a+=b
print(a)

#listeden eleman silmek için .pop kullanılır

a.pop(3)
print(a)

#diğer silme yöntemleri
del a[1]
a.remove(0)
print(a)

#listeyi temizlemek için alternatif yöntemler
a.clear()
print(a)
a*=0

#listenin eleman sayısını öğrenmek için len kullanılır
e = [1 , 2 , 3 , 4 , 5]
print(len(e))
"""""

#Tuple veri yapısı
#değiştirilemez(inmutable) veri yapısıdır
"""""
a = (1 , 2 , 3 , 4 , 5)
print(type(a))

b = "ali" , "ahmet" , "ayşe" , "veli"
print(type(b))
#tuple elemana ulaşma
print(a[2])

#tuple'da eleman değiştirmek için önce list'e dönüştürüp sonra 
#tuple' geri döndürülmesi gerekir
a = (1,2,3)
b=list(a)
b[0]=99
b= tuple(b)
print(b)

#index metodu verilen değerin kaçıncı index'teyse onu  döndürür
#count metodu kaç tane aynı değerden geçildiğini söyler
c = 22,19,69,4,5,6,3,3
print(c.index(69))
print(c.count(3))
"""

# Set yapısı 
# tekrar eden elemanların bulunamadığı bir yapıdır
"""""
# a = set () boş set yaratılır
a = set ()
#içi dolu set yapısı
a = {1,2,3,4,4,4,4,2,5,8}
print(type(a),a)

#len fonksiyonu set yapısında sadece benzersiz değerleri sayar
print(len(a))
#eleman eklemek için .add kullanılır
a.add(17)
print(a)
#istenen değerdeki elemanı silmek için .remove kullanılır
a.remove(4)
print(a)

#.discard komutu da remove gibi siler ancak remove
#eğer istenen değer yoksa hata verir discard vermez
a.discard(91)
print(a)
#pop değeri burada da var ancak burada baştan siler
a.pop()
print(a)

#.update değeri ile iki set'i birleştirir ancak aynı değerleri almaz
a= {1,2,3,3,3,4}
b={3,4,4,4,5,6,}
a.update(b)
print(a)

# birleştirme işleminde .union kullanılır
A = {1,2,3,4,9}
B = {3,4,5,6,10}
C = {3,5,6,7,8,9}
print(A.union(B))
print(A.union(B.union(C)))
print(A.union(B , C) #yukardakinin aynısının farklı gösterimi

# ortak kesişimleri bulmak için .intersection kullanılır
print(A.intersection(B.intersection(C)))
# aradaki farkları bulmak için .difference kullanılır
print(A.difference(C))
"""

#Dictionary yapısı
#ilk değer: key , ikinci değer: value
"""""
# a = {}  bu da set gibi yazılır ancak key, value vardır
a = {"ali" : 76 , "veli" : 43 , "ayse" : 57}
print(a, type(a))

print(a[ "veli" ])

#clear copy metodları bunlar için de geçerli

#copy'nin mantığı orjinalinde işlem yapmak istemediğimizde
#farklı bir kopyası ile işlem yapabiliriz
b = a.copy()
print(b)
a.clear()
print(a)

#değer değiştirmek liste ile aynı
a = {1:"ahmet" , 2:"mehmet" , 5:"kamil"}
a[1] = "murat"
print(a)
#sadece key ve values görmek için .keys .values kullanılır
print(a.keys())
print(a.values())
#.items ile tuple olarak görülüyor
print(a.items())

#hata almadan key değerlerinde arama yapmak için .get kullanılır
print(a.get( 3, "eğer değer yoksa bu yazı yazsın") )

# key vererek value değerini dictinary'den çıkartmak için 
a.pop(5)
print(a)

#rastgele bir elemanı atmak için .popitem kullanılır
a.popitem()
print(a)

#
a = {"ali" : 76 , "veli" : 43 , "ayse" : 57}

# listede olan eleman varsa getirme listede yoksa getir
a.setdefault("ali", 20)
print(a)

a.setdefault("deniz", 10)
print(a)

#tuple'dan dict oluşturma
a ={1,2,3,4,5,6}
print(type(a))
b= dict.fromkeys(a,"hop")
print(type(b), b)

#.update ile güncellenmiş değerleri atayabiliyoruz
a = {"ali" : 20 , "veli" : 13 , "ayse" : 88}
b = {"ali" : 76 , "veli" : 43 , "ayse" : 57}
a.update(b)
print(a)

#Karşılaşabileceğimiz karmaşık dict örneği
a= {"productID":89787 ,
    "productCategory": 2,
    "productTitle": "Hp 27x",
    "productYear" : 2012 ,
    "product" : [{1:"a",
                2:"b",
                 3:"c"},2,3]
}
print(a["product"][0][2])
"""