#Sayının negatif pozitif ve 0 kontrolü örneği
"""
a = int(input("Sayı giriniz:"))

if a > 0:
    print("pozitif sayı")
elif a < 0:
    print("negatif sayı")
else:
    print("a 0'a eşittir")
"""

#Yukarıdaki örneğin daha iyi yazımı
"""
a = int(input("Sayı giriniz:"))

if a >= 0:
    if a == 0:
        print("0'a eşit")
    else:
        print("pozitif sayı")
else:
    print("negatif sayı")
"""

#En büyük sayıyı bulma uygulaması
"""
sayi_1 = int(input("1. sayıyı giriniz:"))
sayi_2 = int(input("2. sayıyı giriniz:"))
sayi_3 = int(input("3. sayıyı giriniz:"))

max = 0

if sayi_1 > sayi_2 and sayi_1 > sayi_3:
    max = sayi_1
elif sayi_2 > sayi_1 and sayi_2 >sayi_3:
    max = sayi_2
else:
    max = sayi_3
print("En büyük sayı {}".format(max))
"""

#Sayının çift veya tek olduğunu bulan program
"""
sayi = int(input("Sayıyı giriniz:"))

if sayi % 2 == 0:
    print("çift")
else:
    print("tek")

"""

#Asal sayı bulma programı
#Asal sayı 1 ve kendisinden başka böleni olmayan sayıdır
#1 sayısını da asal gösteriyor o bug'ı çözmem gerek 
"""
sayi = int(input("Sayıyı giriniz:"))

for i in range(2, sayi):
    print(i)
    if sayi % i == 0:
        print("sayı asal sayı değildir")
        break
else:
    print("sayı asal sayıdır.")
"""

# 1 ile 100 arasındaki asal sayıları gösteren program
"""
for sayi in range(1,101):  
   if sayi > 1:  
       for i in range(2,sayi):  
           if (sayi % i) == 0:  
               break  
       else:  
           print(sayi) 
"""

# 0 ile 1000 arasında kaç asal sayı vardır programı
"""
toplam = 0
for sayi in range(0,1001):  
   if sayi > 1:  
       for i in range(2,sayi):  
           if (sayi % i) == 0:  
               break  
       else:  
           toplam += 1
print(toplam, "asal sayı vardır")
"""

#Faktoriyel bulma programı (for ile)
"""
sayi = int(input("Sayıyı giriniz:"))

faktoriyel = 1

for i in range(1,sayi + 1):
    faktöriyel *= i
print(faktoriyel)
"""

#Faktoriyel bulma programı (while ile)
"""
sayi = int(input("Lütfen bir sayı giriniz:"))
faktoriyel = 1

while sayi > 1:
    faktoriyel *= sayi
    sayi -= 1
print(faktoriyel)
"""

#Aşağıdaskilerden hangisinde birden fazla aynı öge bulunabilir, değiştirilebilir , sıralı yapıdadır
#tuple:değiştirilemez , set:birden fazla aynı öge bulunamaz, dict: sıralı değildir, cevap list

#Hangi ifade döngüyü sonlandırır
#stop, exit, break(doğru), return

#Aşağıda iki tuple birleşiyor ama değiştirilemezdi. Neden, araştırma sorusu.
"""
a = (2 ,5, 2)
a += (7, 9, 10)
print(a)
print(type(a))
"""

#List hatırlatmalar
""""
meyveler = ["elma", "portakal", "muz"]
print(meyveler)

meyveler[2] = "armut"
print(meyveler)

meyveler.append("ayva") 
print(meyveler)

meyveler.insert(1,"çilek")
print(meyveler)

meyveler.remove("portakal") 
print(meyveler)

print(meyveler[-2])

print(meyveler[2:5])

#if ile içinde var mı uygulaması
if "muz" in meyveler:
    print("Listede muz var")
else:
    print("Listede muz yok")

#for ile içinde var mı uygulaması
for i in meyveler:
    if i == "muz":
        print("Listede muz var")
"""

#update ile set yapısı list ile birleşir set oluşturur
"""
listem = {"muz", "armut", "ayva"}
yeap = ["portakal", "ayva"]

listem.update(yeap)
print(listem)
print(type(listem))
"""

#dict hatırlatmalar
"""
ogrenci = {
    "isim": "John",
    "sinif": "3",
    "dogumYili": "1997"
}

print(ogrenci.get("sinif")) 
print(ogrenci["sinif"])

ogrenci["dogumYili"] = "1998" #doğum yılı değiştirme
print(ogrenci["dogumYili"])

ogrenci.pop("dogumYili") #doğum yılı çıkartma
print(ogrenci)

ogrenci.clear() #tüm dict temizleme
"""

#Dict - Notlara ulaşma örneği ve ortalama hesaplama
"""
notlar = {
    "Ali":   76,
    "Veli":  34,
    "Ayse":  45,
    "Deniz": 45
}

toplam = 0
for k, v in notlar.items():
    print(k, v)
    toplam += v

print("ortalama:", toplam / len(notlar))
"""

#yukarıdaki örneğin .value metoduyla notları alması
"""
notlar = {
    "Ali":   76,
    "Veli":  34,
    "Ayse":  45,
    "Deniz": 45
}

for i in notlar.values():
    print(i)
"""

 #tek satırda if - else yapısı yazımı
"""
a, b = 5 ,7

k = "a büyüktür" if a > b else "b büyüktür"
print(k)
"""

#Girilen sayının tersini veren program
"""
sayi = int(input("Lütfen sayı giriniz:"))
sayi_tersi = 0

while sayi!= 0:
    k = sayi % 10
    sayi_tersi = sayi_tersi * 10 + k 
    sayi //= 10 #kalansız bölme

print(sayi_tersi) 
"""

#Yukarıdaki örneği str dönüştürme yöntemi ile yazımı
"""
sayi = str(input("Lütfen sayı giriniz:"))
sayi = sayi[::-1]
print(int(sayi))
"""

#List özellikler hatırlatma
"""
dizi = [1, 2, 3, 4, 5]

print(dizi[-1])
print(dizi[:2])
print(dizi[:-2])
print(dizi[:])
print(dizi[::2]) #sonuna kadar 2'şer atlayarak git
print(dizi[::-1]) #tersten sona kadar
"""

#Fibonacci sayısı 0 1' den başlayarak son 2 rakam toplanarak diğer sayıyı oluşturur
#Fibonacci sayısının istenen terim sayısını yazdıran program
"""
terim = int(input("Fibonacci'nin kaç terimini görmek istersiniz:"))

a, b = 0, 1

k = 0

if terim < 0:
    print("Lütfen pozitif tam sayı giriniz")

else:
    while k < terim:
        print(a)
        v = a + b
        a = b
        b = v
        k +=1
"""


