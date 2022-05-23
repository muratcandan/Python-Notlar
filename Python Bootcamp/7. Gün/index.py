####Global değişken ve Local değişken
"""
b = 7
def yeap():
    a = 12
    print(a)

yeap()
print(a) # a değikeni fonksiyon içindedir, Local değişken olduğundan tanımlanmamış görünür
print(b) # b ise global değişken olduğundan tanımlıdır
"""

#Global değişkeni lokalde değiştirirsek globalde etkilenmez
#local'deki a etkilenir
"""
a = 34

def hop():
    a = 2
    print(a)

hop()
print(a)
"""

#Eğer global a'yı değiştirme istersek global olarak belirtmemiz gerekir
"""
a = 34

def hop():
    global a 
    a = 2
    print(a)

hop()
print(a)
"""

#İşlem yapmak istersek ve tanımlamazsak hata alırız
#ya global olarak belirtmemiz lazım yada yeni a tanımlamamız lazım
"""
a = 34

def hop():
    a += 2 #bu kod çalışmaz çünkü işlem yaparken tanımlamamız gerekir
    print(a)

hop(a)
print(a)
"""

#Fonksiyon içinde fonksiyon yaparsak da içerisindeki lokal olduğundan
#a değerini değiştirirsek lokal'de değişecek
"""
def hop():
    a = 34

    def yeap():
        a = 2
        print(a) # a ==> 2

    yeap()
    print(a) # a ==> 34

hop()
"""

#iç içe fonksiyonlarda değişkene ulaşmak 
#için nonlocal anahtar kelimesi kullanılır
"""
def hop():
    a = 34

    def yeap():
        nonlocal a
        a = 2
        print(a) # a ==> 2

    yeap()
    print(a) # a ==> 34

hop()
"""

#Döngü örneği - 1
"""
a = int(input("sayı:"))
while a < 4:
    a += 2
    if a == 5:
        continue
else:
    a +=7

print(a)
"""

#Döngü örneği - 2
"""
dizi = [1,2,3]
def hesapla(a,b):
    return a*b

def islem(dizim):
    sum = 0
    for i in dizim:
        if i < 2:
            sum +=i
        return sum

print(hesapla(2,islem(dizi) + 1))
"""

#Döngü örneği - 3
"""
dizi = [4]
for i in dizi:
    if i == 6:
        break
    print(i)
"""

#Döngü örneği - 4
"""
a = 0
sum = 4
numaralar = [4,6]
while a < len(numaralar):
    for numara in numaralar:
        sum+= numara
    a += 1
print(sum)
"""

####Object Oriented Programming (Nesne yönelimli Programlama)

#--Birden fazla veri tutmak istediğimizde:
# Araba ==> renk, motor gücü, tekerlek sayısı, fiyat vb. özellikleri var
# Öğrenci ==> isim, yaş, mail, telefon, okul numarası, notları vb.

#--Kodlar daha okunaklı yazılabilir
#--Modüler yapı sunduğundan daha kontrol edilebilir sistemler kurgulanır
#--Büyük projelerde farklı ekipler daha senkron şekilde çalışabilir
#--Kolay geliştirelebilir
#--OOP olmadan da kodlama yapılabilir ancak diğer projeleri okumak zorlaşır
#--Büyük bir proje içinde yer alacak olursak bilmek gerekir

#--Nesnelerin özellikleri, Nesnelerin Metodları vardır
# Araba ==

#Aşağıdaki gibi OOP olmadan bir sürü değişken yapısı ile yazımı
"""
isim_1 = "Ahmet"
soyisim_1 = "Çelebi"
yas_1 = 22
notu_1 = 45

isim_2 = "Mehmet"
soyisim_2 = "Turan"
yas_2 = 20
notu_2 = 88

isim_3 = "Kamil"
soyisim_3 = "Berk"
yas_3 = 25
notu_3 = 77
"""

#Sınıf oluşturmak için class(sınıf) kullanılır
#sınıf ==> soyut bir kavramdır, ortak özellikleri buluşturan tanımlama örneğidir
"""
class Ogrenci:
    pass

class Ogrenci():
    pass
"""

#class'tan nesne oluşturma
"""
class Ogrenci():
    isim = "Ali"
    soyisim = "Erbay"
    yas = 37

print(Ogrenci.yas)
print(Ogrenci.isim)

ogr1 = Ogrenci() #ogr1 nesnesi Ogrenci class'ından oluşturuldu

print(ogr1)
print(ogr1.isim)
print(ogr1.soyisim)
print(ogr1.yas)

ogr2 = Ogrenci() #ogr2 nesnesi Ogrenci class'ından oluşturuldu

print(ogr1)
print(ogr1.isim)
print(ogr1.soyisim)
print(ogr1.yas)

ogr2.isim = "Veli" #Nesnenin değerini değiştirdik
print(ogr2.isim)
print(ogr1.isim)

ogr3 = Ogrenci()
ogr3.isim = "Ayşe"

print("Öğrenci adı:", ogr1.isim)
print("Öğrenci adı:", ogr2.isim)
print("Öğrenci adı:", ogr3.isim)
"""

#Yukarıdaki kullanım verimsizdir, init metodu ile kullanım daha kolaydır
#self, metodlara ulaşmamızı sağlayan bir anahtar kelimedir
#init constructor(yapıcı) metoddur. Nesne oluşur oluşmaz çağırılır
"""
class Ogrenci():
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas

    def bilgileriYazdir(self): #burada metod oluşturuyoruz
        print("İsim: {}, Soyisim: {}, Yaş: {}".format(
                        self.isim,self.soyisim,self.yas))


ogr1 = Ogrenci("Ali", "Erbey", 37)
ogr2 = Ogrenci("Veli", "Çelebi", 30)

ogr1.bilgileriYazdir()
"""

#Nesne oluşturma ve metod yaratma örneği
"""
class Ogretmen:
    def __init__(self,isim,yas,alan, maas):
        self.isim = isim
        self.yas = yas
        self.alan = alan
        self.maas = maas

    def bilgileriYazdir(self):
        print("Öğretmen Bilgileri: isim:{} yas: {}  alan: {} maas: {}".format(self.isim,self.yas,self.alan,self.maas))

    def zam(self):
        self.maas = self.maas*2
        return self.maas

    def yasArtir(self):
        self.yas = self.yas + 1
        return self.yas

ogretmen1 = Ogretmen("Berke", 45, "matematik", 1000)
ogretmen2 = Ogretmen("Ali", 30, "türkçe", 1500)
ogretmen3 = Ogretmen("Hasan", 27, "fizik", 2000)

ogretmen1.bilgileriYazdir()
ogretmen2.bilgileriYazdir()
ogretmen3.bilgileriYazdir()

print("-----")

ogretmen1.zam() #zam fonksiyonu ile maaşına zam yapmış olduk
ogretmen1.bilgileriYazdir()


ogretmen2.yasArtir()
ogretmen2.bilgileriYazdir()
"""

####Encaptulation(Kapsülleme):
#-privat, public, protected, friendly ==> erişim belirleyiciler
#-Eğer bir veriyi kısıtlamak istersek __(iki alt çizgi) kullanılır
#-Kapsülleme, kontrollü değişiklik için kullanılır. Önemli olan ve değiştirilirken 
#hata yaparsak sorun çıkartabilecek değişkenlerde kullanılır
"""
class Ogretmen:
    def __init__(self,isim,yas,alan, maas):
        self.isim = isim
        self.yas = yas
        self.alan = alan
        self.__maas = maas #şu an __ yaparak privat hale getirdik. 

    def bilgileriYazdir(self):
        print("Öğretmen Bilgileri: isim:{} yas: {}  alan: {} maas: {}".format(self.isim,self.yas,self.alan,self.maas))

    def zam(self):
        self.maas = self.maas*2
        return self.maas

    def __yasArtir(self): #metodu da __ ile erişilemez hale getirebiliyoruz
        self.yas = self.yas + 1
        return self.yas
    
    def getMaas(self):   #bu fonksiyonu oluşturarak privat değeri görebiliyoruz
        return self.__maas
    
    def setMaas(self,yeniMaas): #bu fonksiyonu oluşturarak privat değeri değiştirebiliyoruz
        if yeniMaas < 0: 
#             return "maas degeri 0 dan kucuk olamaz" #mesela maaşı - yazmak büyük bir hata olacağından burada daha dikkatli girebiliriz
#         else:
#             self.__maas = yeniMaas


    
ogretmen1 = Ogretmen("Berke", 45, "matematik", 1000)
ogretmen2 = Ogretmen("Ali", 30, "türkçe", 1500)
ogretmen3 = Ogretmen("Hasan", 27, "fizik", 2000)

#Yukarıdaki getMaas() ve SetMaas() oluşturmazsak göremez ve değiştiremeyiz
#Aşağıda o fonksiyonlar olmadan sonuçlar var hata alıyoruz

print(ogretmen1.isim)
print(ogretmen1.maas) #'Ogretmen' object has no attribute 'maas'. privat olduğundan hatası alıyoruz 
ogretmen1.maas = 3000 #değiştiremeyiz hata alırız


#Buradan itibaren yukarıda getMaas() ve setMaas() fonksiyonları oluşturduk
#böylece görebilir ve değiştirebiliyoruz 

print(ogretmen1.getMaas())

ogretmen1.setMaas(4000)
print(ogretmen1.getMaas())
"""

#Kapsülleme örneği 
"""
class Car:
    def __init__(self, stil, color, marka, fiyat):
        self.stil = stil
        self.color = color
        self.marka = marka
        self.__fiyat = fiyat

    def changeColor(self, yeniRenk):
        self.color = yeniRenk

    def getFiyat(self):
        return self.__fiyat

    def setFiyat(self, yeniFiyat):
        if yeniFiyat < 0:
            return "0 dan kucuk olamaz"
        else:
            self.__fiyat = yeniFiyat


c1 = Car("Sedan", "beyaz", "ford")
c1.changeColor("siyah")
print(c1.color)
"""

