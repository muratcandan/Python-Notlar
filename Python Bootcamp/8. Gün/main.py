# Önceki ders tekrarı
# init contructor(yapıcı) metod
# self diğer metodlara ulaşmayı saylayan bir keyworld
"""
class Car:
    def __init__(self):
        print("Car sınıfı")

    def bilgiYazdir(self):
        print("Car sınıfı bilgileri")


c = Car()

c.bilgiYazdir()
"""

####Inheritace (Kalıtım)
# Base class'dan sub classlar oluşturulmasıdır
"""
class Arac():
    def __init__(self, marka, model, renk):
        self.marka = marka
        self.model = model
        self.renk = renk


class Otobus(Arac):  # parantez içine hangi sınıftan inherit olacaksa o yazılmalı
    def __init__(self):
        print("Car sınıfı")

    def bilgiYazdir(self):
        print("Car sınıfı bilgileri")


c = Otobus()
c.bilgiYazdir()
"""

# Inheritace örneği
# super keyworldu yukardaki insan sınıfındaki constructer'a ulaşmamızı sağlıyor
# super tekrar tekrar kod yazmamamızı sağlıyor
# yukarıdaki insan sınıfından aşağıdaki sınıfa değerleri alabiliyoruz

# Polimorfizim(birçok şekil)
# bir metodun farklı işler yapması anlamına gelir
"""
class Insan:
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        print("İnsan sınıfı")

    def info(self):
        print("{} {} {}".format(self.isim, self.soyisim, self.yas))


class Ogretmen(Insan):
    def __init__(self, isim, soyisim, yas, brans):
        # burada super ile yukarıdaki bilgileri buraya aldık
        super().__init__(isim, soyisim, yas)
        self.brans = brans  # burada yeni bilgi girdik
        print("Öğretmen sınıfı")

    def info(self):
        print("{} {} {} {}".format(self.isim, self.soyisim, self.yas, self.brans))

    def bransDegistir(self, yeniBrans):
        self.brans = yeniBrans
        print("Branş değiştirildi")


class Ogrenci(Insan):
    def __init__(self, isim, soyisim, yas, sinif):
        # burada super ile yukarıdaki bilgileri buraya aldık
        super().__init__(isim, soyisim, yas)
        self.sinif = sinif  # burada yeni bilgi girdik
        print("Öğrenci sınıfı")

    def info(self):
        print("{} {} {} {}".format(self.isim, self.soyisim, self.yas, self.sinif))

    def sinifDegistir(self, yeniSinif):
        self.sinif = yeniSinif
        print("Branş değiştirildi")


ogretmen_1 = Ogretmen("Ali", "Erbey", 37, "bilgisayar")
print(ogretmen_1.isim)
ogretmen_1.info()
ogretmen_1.bransDegistir("matematik")  # öğretmen branşı değiştirdik
ogretmen_1.info()


ogrenci_1 = Ogrenci("Murat", "Candan", 25, 4)
ogrenci_1.info()
ogrenci_1.sinifDegistir("3")  # öğrenci sınıfını değiştirdik
ogrenci_1.info()
"""

# override(baskılama) yazma kavramı
# yukarıdaki ana fonksiyondaki tanimla metodu aşaağıdaki tarafından baskılanmıştır

"""
class Arac:
    def tanimla(self):
        print("Araç sınıfı tanımlanması")


class Araba(Arac):
    def tanimla(self):
        print("araba sınıfı tanımlaması")

    def hizi(self, hiz):
        print("araba hızı:", self.hizi)


c = Araba()
c.tanimla()

c.hizi(120)

v = Arac()
v.hizi()  # 'Arac' object has no attribute 'hizi' overwrite'dan dolayı
"""

# Multiple Inheritance(Çoklu kalıtım)
# İki base sınıfın tek bir sınıfa kalıtım sağlamasıdır
"""
class yerdeGidenAraclar:
    def yerde(self):
        print("yerde giden araçlar")


class havadaGidenAraclar:
    def havada(self):
        print("havada giden araçlar")


class ucanAraba(yerdeGidenAraclar, havadaGidenAraclar):
    pass


u = ucanAraba()
u.havada()
u.yerde()
"""

#---- Dekoratorler
# Framework kullanmak istersek dekoratorleri kullanır
# Fonksiyonlara ekstra işlevsellik sağlayan yapılardır
# Fonksiyonlara dinamik olarak özellik ekleyebiliriz
# Kod tekrarı önlenir

# Hatırlatmalar
# tuple yapısı
"""
def yeap(*args):
    for i in args:
        print(i)


yeap(1, 2, 3, 4)
"""

# dictionary yapısı
"""
def yeap(**kwarg):
    print(kwarg)
    for k, v in kwarg.items():
        print(k, v)


yeap(a="ali", b="veli")
"""
# tüm keyworldleri alan bir yapı
"""
def yeap(*args, **kwargs):
    print(args)

    for i in args:
        print(i)

    print("----")

    for k, v in kwargs.items():
        print(k, v)
    print(kwargs)


yeap(1, 2, 3, 4, [1, 2, 3], {1, 2, 3}, a="ali", b="veli")
"""

# fonksiyonu bir değişkene atama
"""
def yeap(a):
    print("hop", a)


yeap("ali")
k = yeap
print(k)
k("veli")
"""

# Fonksiyon içerisinden fonksiyon
"""
def yeap():
    def hop():
        print("hop fonksiyonundan selam")
    hop()
    print("yap fonksiyonundan selam")


yeap()
hop()  # local fonksiyon olduğundan hata alırız çağıramayız
"""

# Fonksiyon içerisinde fonksiyon içinde işlem
"""
def yeap(*args):
    def hop(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(hop(args))


yeap(2, 3, 4, 5)
"""

# Argüman olarak fonksiyon geçtik ve
# func ile diğer fonksiyonları çalıştırdık
"""
def yeap():
    print("Yeap =>")


def hop():
    print("Hop <=")


def aha(func):
    func()


aha(yeap)
aha(hop)
"""

#
"""
def yeap():
    def hop(a):
        print("Hop", a)
    return hop


a = yeap()
a("Ali")
"""

#
"""
def yeap():
    def hop():
        print("Hop =>")
    return hop


a = yeap  # a'yı fonksiyon olarak aldık
print(a)
print(a())  # lokal olarak çıkartır


a()  # hiçbirşey yazdırmaz
a()()  # Hop => yazdırır
"""

#
"""
def yeap():
    def hop(a):
        print("Hop", a)
    return hop


a = yeap
print(a)
print(a())
a()(12)
"""

# Dekorartor örneği
# Bu yazacağımız yerine python özellik olarak @ ile yazablmemize izin veriyor
# dekorator kullanarak bir aşağıdaki kod bu kodun o özellik kazandırılmış hali
"""
def hop(func):
    def wrapper():
        print("fonksiyondan önce çağırıldı")
        func()
        print("fonksiyon çağırıldıktan sonra")
    return wrapper


def yeap():
    print("Yeap")


a = hop(yeap)
a()
"""

# Bu kod yukarıdakinin @ ile özellik kazandırılması ile dekorator kullanılmış hali
"""
def hop(func):
    def wrapper():
        print("fonksiyondan önce çağırıldı")
        func()
        print("fonksiyon çağırıldıktan sonra")
    return wrapper


@hop  # bu yapı yeap fonksiyonuna özellik kazandırmış oluyor
def yeap():
    print("Yeap")


# a = hop(yeap) #bu ve aşağısındaki yapı yerine yukarda @hop ile yeap'e özellik kazandırdık
# a()
yeap()
"""

# Decorator örneği -1
# eğer yeap() fonksiyonuna argüman göndermek istersek
"""
def hop(func):
    def wrapper(a):
        func(a)
        print("sonra")
    return wrapper


@hop
def yeap(a):
    print("Yeap", a)


yeap("ali")
"""

# yukarıdaki örnekteki fonksiyonların içine a yazmak yerine
# ne gönderirsek gönderelim hata almamak için
# args ve kwarg yazarsak hata almamış oluruz ve herhangi bir değişiklik olmaz
"""
def hop(func):
    def wrapper(*args, **kwargs):
        print("önce")
        func(*args, **kwargs)
        print("sonra")
    return wrapper


@hop
def yeap(a):
    print("Yeap", a)


yeap("ali")
"""

# eğer return döndürmek istersek aşağıdaki gibi yapı oluşturulur
"""
def hop(func):
    def wrapper(*args, **kwargs):
        print("önce")
        r = func(*args, **kwargs)
        print("sonra")
        return r
    return wrapper


@hop
def yeap(a):
    return "Yeap" + a


k = yeap("ali")
print(k)
"""

# 3 saniye bekle sonra diğer koda geç programı

"""
import time
def aha():
    print("Başladı")
    time.sleep(3)  # 3 saniye
    print("bitti")


aha()
"""

#
"""
import time

def ikiKatiniHesapla(a):
    l = list()  # boş liste
    begin = time.time()
    for i in a:
        l.append(i*2)
    end = time.time()
    print("işlem zamanı", str(end - begin))
    return l

    


ikiKatiniHesapla(range(10000))
"""

# decorator ile yukarıdaki yapının oluşturulması


"""
###time kütüphanesini çağırınca bu sayfada hata veriyor ancak yeni sayfada hata vermiyor. Çözemedim
#import time 
def hop_time(func):
    def wrapper(a):
        begin = time.time()
        r = func(a)
        end = time.time()
        print(func.__name__ + " -> " + str(end - begin))
    return wrapper


@hop_time
def ikiKatiniHesapla(a):
    l = list()
    for i in a:
        l.append(i * 2)
    return l


@hop_time
def kupunuHesapla(a):
    l = list()
    for i in a:
        l.append(i ** 3)
    return l


ikiKatiniHesapla(range(10000))
kupunuHesapla(range(10000))
"""
