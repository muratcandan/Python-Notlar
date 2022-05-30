# Decoratorler örnek - 1
"""
def diziOzellikleri(func):
    def wrapper(b):
        ortalama = 0
        maxSayi = 0
        minSayi = 0
        toplam = 0

        for i in b:
            if i > maxSayi:
                maxSayi = i
            if i < minSayi:
                minSayi = i
            toplam += i
        ortalama = toplam / len(b)
        print("Ortalaması:", ortalama)
        print("En küçük sayı:", minSayi)
        print("Maksimum sayı:", maxSayi)
        func(b)
    return wrapper


@diziOzellikleri
def diziTopla(a):

    sum = 0
    for i in a:
        sum += i
    print("Toplam:", sum)


k = [23, 34, 5, 65, 87, 99]
diziTopla(k)
"""

# Decorator örnek - 2

"""
def hop(func):
    def wrapper():
        print("Önce")
        func()
        print("sonra")
    return wrapper


@hop
def yeap():
    '''bu fonksiyon dizinin elemanlarını toplar'''
    print("Toplam: 234")


print(yeap.__name__)
print(yeap.__doc__)
print(yeap)  # <function yeap at 0x0000026574012F80> decoratore olmadan @hop silinince
print(yeap)  # <function hop.<locals>.wrapper at 0x000001D2AD9E3010> decorater ile
"""

# Decorator örnek - 2 wraps yapısı ile yazma
# @wraps ifadesi, fonksiyonların metadatalarının kaybolmamasını sağlar

"""
from functools import wraps
def hop(func):
    @wraps(func)
    def wrapper():
        print("Önce")
        func()
        print("sonra")
    return wrapper


@hop
def yeap():
    '''bu fonksiyon dizinin elemanlarını toplar'''
    print("Toplam: 234")


print(yeap.__name__)
print(yeap.__doc__)
print(yeap)  
"""

# Decoratore örneği - 3
"""
from functools import wraps

def ikiKati(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


def kareAl(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper


@ikiKati
@kareAl
def topla(a, b):  # Alttan üste işlem yapar önce kare sonra 2 katı alır
    return a + b

print(topla(7, 8)) # kendi fonksiyonunu yapacak sonra karesini alacak sonra 2 katını alacak
"""

# Decoratorler sadece kendi yazdığımız fonsiyonlarda değil built in(gömülü) fonksiyonlara da uyarlanabilir
"""
def yeap(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


toplamın_iki_kati = yeap(sum)
print(toplamın_iki_kati([5, 6, 7, 8, 9]))
"""

# Decorator örneği - 4
"""
def loginfo(func):
    def wrapper(*args, **kwargs):
        print("Fonsiyon isim:", func.__name__)
        print("Argümanlar isim:", args)
        print("Keywords argümanlar:", kwargs)
        result = func(*args, **kwargs)
        print("Result:",  result)
        return result
    return wrapper


@loginfo
def yeap(a):
    return "hi" + a


yeap("Ali")

k = loginfo(sum)
k([5, 6, 7])
"""

# String Metodları
# split, lower, upper vb.
# Genelde gelen veriler string oluyor onlarla uğraşırken dönüştürmemiz gerekiyor, bölmemiz gerekiyor vs.
# network => tcp/ip => string
# csv, xlsx => string 23,34,54,65,76,87
# json => {key:value} => robot süpürge verileri örneğin
# Split metodu
# string'i istenen değişkene göre bölme yapar
"""
a = "python bootcamp"
a = a.split(" ")  # boşluğa göre böl
print(a)  # ['python', 'bootcamp'] list halinde böldü

for i in a:
    print(i)
"""

# Split örneği - 1
"""
a = "12,23,45,67,89"
a = a.split(",")
print(a)
"""

# Split örneği - 2
"""
liste = ["V1-0088_9999179", "V1-0089_9999179", "V1-0090_9999179"]

for i in liste:
    a = i.split("-")  # V1   0088_9999179
    b = a[1].split("_")  # 0088   9999179
    print(b[0])
"""

# Upper - Lower metodu
# Tüm karakterleri büyütür - küçültür
"""
a = "murat candan"
a = a.upper()
print(a)
a = a.lower()
print(a)
"""

# Capitalize metodu
# sadece baş harfi büyütütür
"""
a = "python bootcamp"
a = a.capitalize()
print(a)
"""

# Title metodu
# tüm kelimelerin baş harfini büyütür
"""
a = "python bootcamp"
a = a.title()
print(a)
"""

# Strip metodu
# kelime içerisindeki boşlukları siler
"""
a = "     python   "
a = a.strip()
print(a)
"""

# Strip örnek - 1
# ayrıca strip ile istenmeyen karakterleri de silebiliriz
"""
a = "*%+  python -'-"
a = a.strip("*%+'- ")
print(a)
"""

# Count metodu
# cümle içinde kaç kere o eleman geçmişse sayar
"""
a = "python bootcamp"
b = a.count("o")
print(b)
"""

# Find metodu
# eğer kelime varsa kelimenin index numarasını döner
# yoksa -1 döner
"""
a = "python bootcamp"
b = a.find("boot")
print(b)
"""

# Find örnek - 1
"""
a = "ertcom-12-45-67-99"
b = a.find("com")
print(a[b:19+b])
"""

# Replace metodu
# harflerin istenenle yerini değiştirir
"""
a = "www.uşaküniversitesi.com"
a = a.replace("ş", "s")
a = a.replace("ü", "u")
print(a)
"""

# Startswith - Endswith metodu
# istenen değerle başladığını ve bittiğini kontrol eder.
# doğru ise True yanlış
"""
a = "www.alierbey.com"
a = a.startswith("www")
print(a)
a = a.endswith("com")
print(a)
"""


# String metodları örneği - 1
#a = "ali.erbey@usak.edu.tr"
# edu, . , @  var mı sırası doğru mu
# gibi bir soru gelebilir


# Exception
# program yürütülürken hatalar meydana gelebilir:
# yazılımcı kodlama hatası yapar
# yanlış input
# öngöremediğimiz durumlar
# exception - handling

# Exception yazımı
"""
try:
    statements => program hatasız çalıştığında
except:
    statements => program hata verirse çalışacak kodlar
"""

# Exception örneği - 1
"""
def bol(a, b):
    print(a/b)


try:
    bol(5, 0)
except:
    print("Bir şeyler yanlış gitti")
"""

# Hatanın nerden kaynaklandığını görmek istersek
# except Exception as e:
"""
def bol(a, b):
    print(a/b)


try:
    bol(5, 0)
except Exception as e:
    print("Bir şeyler yanlış gitti", e)
"""

# Exception örneği - 2
"""
try:
    print(a)
except Exception as e:
    print("Bir şeyler yanlış gitti", e)
"""

# Hata ismine göre programı çalıştırma
"""
try:
    x = 5 / 0
except (ZeroDivisionError,NameError): #birden fazla hata yazmak istersek
    print("Bir sayı sıfıra bölünemez")
except:
    print("Bir şeyler yanlış gitti")
"""

# Exception örneği - 3
"""
try:
    int("12s")
except ValueError:
    print("bir string ve sayıyı birlikte sayıya çeviremezsiniz")
except:
    print("Bir sorun bulundu")
"""

# try-except else örneği
"""
    try:
        statements
    except:
        statements
    except:
        statements
    else:
        statements = > programda hata varsa çalışmaz
"""
# Exception else örneği
"""
try:
    x = 1 / 1
except:
    print("Hata var")
else:
    print("sıkıntı yok devam")
"""


# try-except finally örneği
"""
 try:
    statements
except:
    statements
except:
    statements
else:
    statements
finally:
    statements => her zaman çalışır
"""


# Exception finally örneği
"""
try:
    x = 5 / 0
except:
    print("hata var")
finally:
    print("her zaman çalışır")
"""

# raise keyworldu
# hata fırlatır
"""
def selamVer(a):
    if (type(a) != str):
        raise ValueError("String giriniz")
    else:
        print("merhaba", a)


selamVer(12)
"""

# Python'daki Error'ler
"""
 https://docs.python.org/3/library/exceptions.html
 """


# Python keywords
"""
https://py4u.tech/keywords-and-identifier-in-python/
"""
