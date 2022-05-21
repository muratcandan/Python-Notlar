#kullanıcıya hata mesajı vermek için 
#try ve except komutları kullanılır
"""
try:
    x = int(input("Lütfen bir sayı giriniz:"))
except ValueError: #hangi hatayı verince hangi çıktıyı versin
    print("Bu bir sayı değildir")
"""

#Yukardaki örneğin geliştirilmiş hali
"""def main():
    x = get_int()
    print(f"Sayınız {x}")

def get_int():
    while True:
        try:
            return int(input("Lütfen Sayı giriniz:"))
        except ValueError: 
            print("Bu bir sayı değildir")

main()"""

#Uyarı mesajı vermek yerine sadece pass diyerek geçebiliriz

"""
def main():
    x = get_int()
    print(f"Sayınız {x}")

def get_int():
    while True:
        try:
            return int(input("Lütfen Sayı giriniz:"))
        except ValueError: 
            pass #burada pass diyerek bu hatayı geçtik

main()
"""

#Yukarıdaki örneğin başka yazım şekli
"""
def main():
    x = get_int("Lütfen Sayı giriniz:")
    print(f"Sayınız {x}")

def get_int(komut):
    while True:
        try:
            return int(input(komut))
        except ValueError: 
            pass #burada pass diyerek bu hatayı geçtik

main()
"""

#Library import etmek
#Yazı-Tura uygulaması
"""
import random

para = random.choice(["yazı", "tura"])

print(para)
"""

#import fonksiyonu tüm kütüphaneyi getiri
#onun yerine belli bir fonksiyonu kullanacaksa from kullanabilşriz

"""
from random import choice

para = choice(["yazı", "tura"])
print(para)
"""

#Liste içinde değil de belli sayı aralığında rastgele sayı almak istiyorsak
#.randint kullanılır
"""
import random

sayi = random.randint(1, 10)

print(sayi)
"""

#Bir listeki rastgele karmak istersek .shufle kullanılır
"""
import random

kartlar = ["papaz", "kız" , "vale"]

random.shuffle(kartlar)

for kart in kartlar:
    print(kart)
"""

#statistics Library
#matematiksel hesaplamaların olduğu bir kütüphanedir
#.mean fonksiyonu listenin ortalamasını verir
"""
import statistics
ortalama= statistics.mean([100, 90])

print(ortalama)
"""

#sys ile commend prompt içerisinde işlem yapabiliyoruz
#Çalıştırmak için commend promot içinde python index.py Murat yazmak gerek
"""
import sys

print("Selam benim adım", sys.argv[0]) #dosya adını söyleyecek boş bırakırsak
print("Selam benim adım", sys.argv[1]) # programı çağırdıktan sonra ismini yazınca çıkartacak

"""
#yukardaki örneğin hataya except eklenmesi

"""
import sys

if len(sys.argv) < 2:
    sys.exit("Çok az kelime girdiniz") #sys.exit ile önce print eder sonra çıkar  
elif len(sys.argv) >2:
    sys.exit("çok fazla kelime girdiniz")

print("Selam adınız", sys.argv[1]) 
"""

#İkiden daha fazla kişi veya bilgiyi sys ile ekleme

"""
import sys

if len(sys.argv) <2:
    sys.exit("Çok az kelime girdiniz")

for isim in sys.argv[1:]:
    print("İsminiz,", isim)
"""

#Package kütüphanelerden daha geniş ortamlardır
#package indirmek için commend prompta  pip install "paket adı" yazılır  
#cowsay adlı pakedi indirdir
"""
import cowsay #package yükledim ancak sonuç alamadım
import sys

if len(sys.argv) == 2:
    cowsay.cow("Selam sana" + sys.argv[1]) #bir eşek isminizi söyler
    cowsay.trex("Selam sana" + sys.argv[1]) #bir T-rex isminizi söyler
"""
    

#İnternet sitelerinde API almak için requests pakedini indirmek gerekir
#https://itunes.apple.com/search?entity=song&limit=1&term=weezer
#Örnek olarak yukaerıdaki dosyayı Google'a girersek
#JSON text format dosyasını indirir
"""
import json
from textwrap import indent #json kütüphanesi python ile geliyor indirmeye gerek yok. JSON dosyasını pythona göre güzel formatlamak için
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent = 2)) #çalıştırırken python index.py "şarkıcı ismi-weezer yazdık"
"""
#Burada şarkıcının sadece 1 şarkısı için bilgileri aldık. Ancak limit = 50 dersek
#ve sazece şarkıları almak istersek

"""import json #json kütüphanesi python ile geliyor indirmeye gerek yok. JSON dosyasını pythona göre güzel formatlamak için
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

sarkilar = response.json()

for result in sarkilar["results"]:
    print(result["trackName"]) #python index.py manga

"""

#Kendi kütüphanemizi yapmak istersek
#Örnek olarak alttaki fonksiyonu isim.py olarak kaydettik
#Başka bir dosyadayız ve kütüphane olarak kullanmak istiyoruz
# from isim import baybay diyerek fonksiyonu kullanabiliriz

#Bu isim.py dosyası
"""
def selam(isim):
    print(f"Selam, {isim}")

def baybay(isim):
    print(f"Güle Güle, {name}")
------
#Bu başka dosya
import sys

from isim import baybay

if len(sys.argv) == 2:
    baybay(sys.argv[1])
"""

