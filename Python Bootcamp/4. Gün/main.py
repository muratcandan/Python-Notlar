#kontrol yapıları boolean çıktı verir
"""
age = 30
print(age == 30)
print(age > 30)
print(age < 30)
print(age != 30)
print(age <= 30)
"""

#Akış Kontrol Mekıanizmaları
#Döngüler

###if yapısı
""""
age = int( input( "Lütfen Yaşınızı Giriniz:" ) )

if age >= 18:
    print( "Yaş 18'den büyüktür." )
    
elif age < 18:
    print( "Yaş 18'den küçüktür )

else:
    print( "Yaş 18'e eşittir." )

print( "Program akışı devam ediyor" )
"""

#and if ile örnek
"""
a = 13
b = 15

if a == 12 and b == 27:
    print( "Koşullar Sağlanıyor." )

else:
    print( "Koşullar sağlanmıyor." )
"""

#or if ile örnek
"""
a = 13
b = 15

if a == 12 or b == 27:
    print( "Koşullardan biri sağlanıyor." )

else:
    print( "Koşulların hiç biri sağlanmıyor." )
"""

#boolean if örnek
"""
a = True

if a:
    print("a True")
else:
    print("a False")
"""

#iç içe if örnek
"""
a , b , c = 7 , 4 , 2

if a > b:
    print("a, b'den büyüktür")
    if a > c :
        print("a, hem b'den hem c'den büyüktür.")
"""

#tekrarlı işlemlerde döngüler kullanılır
#for döngüsü

#dizinin elemanlarının toplamını bulmak
"""
a = [12 , 34 , 54 , 65]
print(a[0] + a[1] + a[2] + a[3])
"""

#for döngüsü ile kolay dizi elamanları toplama yöntemi
""""
a = [12 , 34 , 54 , 65]
toplam = 0

for i in a:
    toplam += i 

print("Toplam:" , toplam)
"""

#range metodu
""""
print(range(10))
print( list( range(10) ) ) # tek değer varsa 0'dan başla birer artır
print( list( range(3 , 8) ) ) #iki değer için ilk değer başlangıç ikinci bitiş
print( list( range(2 , 14 , 3) ) ) #üç değer için üçüncü değer artış miktarı
"""

#range örnek kullanım - 1
"""
a = [12 , 34 , 54 , 65 , 56 , 76 , 78 , 98 , 23]

for i in range( len(a) ):
    print(a[i])
"""

#for'da else yapısı vardır
#istediğimiz durumlar gerçekleştirmezse diğer durumlar için kullanılır
"""
a = [5 , 2 , 4]

for i in a:
    if i ==8:
        print("8 dizide vardır")
        break
else:
    print("Aranılan sayı dizide yoktur")
"""

###while döngüsü
"""
a = 1

while a < 10:
    print(a)
    a += 1
"""

#for ile aynı döngünün yazımı
"""
for i in range(1,10):
    print(i)
"""

#while koşul sağlanmazsa çalışmaz
"""
a = 15

while a < 10:
    print(a)
    a += 1
"""

#while'da da else ifadesi yazılabilir
"""
a = 0

while a < 5:
    print(a)
    a += 1
else:
    print("yeap")
"""

#sonsuz döngü
"""
while True :
    print("yeap")
"""

#iç içe for döngüsü örneği
"""
for i in range(3):
    for j in range(3):     
        print("i:", i , "j:" ,j)
"""

###break ifadesi 
#bulunduğu döngüyü kırar
"""
for i in range(3):
    for j in range(3):   
        if j == 1:
            break  
        print("i:", i , "j:" ,j)
"""

#while ile break örneği
""""
a =0

while a < 5:
    
    if a == 3:
        break
    a += 1
    print(a)
"""

#continue ifadesi
#kendinden sonra gelen tüm kodları yok sayar
# ifadeleri işletmez ve döngü başa döner
"""
for i in range(6):
    if i == 4:
        continue
    print(i)
"""

# while ile continue örneği
""""
a = 0

while a < 5:
    a += 1
    if a == 4:
        continue
    print(a)
"""

#yukardaki ile benzer ancak sonsuz döngü verir 
#yerleşime dikkat
"""
a = 0

while a < 5:
    print(a)
     4:
        continue
    a += 1
    if a ==
"""

# pass eğer o an kod yazmayacaksak hata almamak için kullanılır
"""
a = [23 , 45 , 65 , 7]

for i in a:
    pass

print("Hello")
"""

# Aşağıdaki yazım şekilleri ile de karşılaşabiliriz
""""
a , b = 7 , 5

if a > b: print("a, b den büyüktür") 
if a > b : print("a, b den büyüktür") ; print("küçüktür") ; print("a ve b eşit değil")
"""

# "Döngü örneği - 1"
"""
a = ["ali" , "veli" , "ayse"]
name = input("İsim giriniz:")

if name in a:
    print(name , "listede vardır.")
else:
    print (name ,  "listede yoktur")    
"""

# "Döngü örneği - 2" sanki sonsuz döngü gibi görünür 
#ancak 0 ve "" False olduğundan 0'da sonlanır
"""
a = 5

while a:
    print(a)
    a -= 1
"""

# "Döngü örneği - 3" 
"""
a = "python"

while a:
    print(a)
    a = a[1:]
"""

# "Döngü örneği - 4"
"""
a = 9

while a:
    print(a)
    a -= 1
    if a == 5:
        break
"""

# "Döngü örneği - 4" 
#koşulu sağladığı anda döngüden çıkan input örneği
"""
while True:
    a = int( input("Sayı giriniz:") )
    if a == -1 : break
"""

# "Döngü örneği - 5" 
"""
for i in range(5):
    while i:
        i -= 1
        if i % 2 == 0:
            continue
        print(i)
"""

# "Döngü örneği - 6" 
#liste içinde liste'nin tüm elemanlarına ulaşmak
"""
a = [ [5 , 3 , 2] , [12 , 34 , 54]]

for i in a:
    for k in i:
        print(k)
"""
