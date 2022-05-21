###Fonksiyonlar
"""
-var olan program akışımızı işlevsel hale getiren yapılardır
-tekrardan kurtarır
-kodu modüler küçük parçalara bölerek programın
kontrolünü sağlar
-programın bakımı kolaylaşır
"""

#fonksiyon kullanım örneği 
"""
def islem():
    print( 3 + 4 )
    print( "İşlem fonksiyonu" )

islem() #islem fonksiyonunu çağırdık
"""

#fonksiyon içerisinde fonksiyon da çağırabiliriz
"""
print( "A" )

def islem():
    print( "B" )

def yeap():
    islem()    
    print( "C" )

islem()
print("D")
yeap()
"""

#fonksiyon içerisinde parametre ile kullanma
"""
def islem( a , b ):
    print( a + b )

islem( 5 , 7 )
islem( 19 , 173)
"""

#fonksiyonlarda boş olarak gönderirsek
#default değer belirleyebiliyoruz
"""
def isim( a = "isim yok" ):
    print("İsminiz:" , a)

isim()
"""

#eğer değişken olarak ne kadar değişken
#gireceğimizi bilmiyorsak * ile istediğimiz kadar değer girebiliriz
"""
def isim(*isimler):
    print(isimler)
    for i in isimler:
        print(i)

isim("ali" , "ayse" , "veli")
"""

#dictionery olarak da değişkenleri fonksiyonda verebiliriz
"""
def isim(**isimler):
    print(isimler["a"])
    for k, v in isimler.items():

isim(a = "veli" , b = "ayse" , c = "ahmet") 
"""

#parametreli gönderdiğimizde sıra önemli değildir
"""
def yeap(a , b , c):
    print(a , b , c)

yeap(c = "ahmet" , a = "veli" , b = "ayse")
"""

#fonksiyonlarda dizileri de gönderebiliriz
"""
def diziToplam(dizi):
    toplam = 0
    for i in dizi:
        toplam += i
    print(toplam)

a = [12 , 23 , 34]
b = [1325 , 234 , 3124]
c = [1462 , 2623 , 3164]
d = [12246 , 2623 , 323]

diziToplam(a)
diziToplam(b)
diziToplam(c)
diziToplam(d)
"""

#biz fonskiyonlardan değer döndürmek isteriz
#return ile değer döndürebiliriz
"""
def toplam( a , b ):

    if a < 0 or b < 0:
        return -1
    else:
        return a + b

k = toplam( 5 , 6 )
p = toplam( -13 , 8 )

print(k)
print(p)
"""

#multiple return 
""""
def islem(a , b):
    return a + b , a - b , a * b , a / b

topla , cikar , carp , bol = islem( 10 , 5)
print( topla )
print( cikar )
print( carp )
print( bol )
"""

#docstring 
#fonksiyon hakkında açıklama yapmak istersek 
""""
def yeap():
    """ """"
    print("yeap fonksiyonu")

yeap()
print(yeap.__doc__) #fonksiyon hakkında yazdığın notu çağırır
"""
#iç içe fonksiyon yazma
""""
def yeap(a , b):
    def hop(k , v):
        return k + v
    return hop(a , b)

c = yeap(5 , 6)
print(c)
"""

###Recursive ==> Özyinelemeli
#fonksiyonun içinden kendisini tekrar çağırmak
#iteratif yapılar , faktöriyel
#+okuma kolaylaşır kod temiz görünür
#+karmaşık yapılar daha basit yazılır
#+kullanmak kolaylığı
#- mantığını anlamak zor
#-daha fazla bellek kullanımı
#-debug işlemi(hata ayıklama) daha zordur

#Recurcive kullanmadan
"""
a = 5
faktoriyel = 1

for i in range(1 , a+1):
    faktoriyel *= i

print(faktoriyel)
"""

#Recurcive kullanarak
"""
def faktoriyel(n):
    if n == 1:
        return 1
    else:
        return (n * faktoriyel(n - 1))
    # 5 * faktoriyel(4)
    # 4 * faktoriyel(3)
    # 3 * faktoriyel(2)
    # 2 * faktoriyel(1)
    #if kısmına çıktı n == 1 olduğundan 1 döndü
print(faktoriyel( 5 ))
"""

#Recurcive örneği
"""
def yeap(a):
    if a <= 0:
        print("hop")
    else:
        print(a)
        yeap(a - 1)

yeap( 7 )
"""

#bir fonksiyonu değişkene atama işlemi
#fonksiyon için esneklik sağlar 
"""
def yeap():
    print("yeap -->")

a = yeap

a()
"""

#fonksiyonu değişkene atama Örnek - 1
"""
def kupHesapla(a):
    return a ** 3 

def kareHesapla(a):
    return a ** 2

k = {"karesi" : kareHesapla, "kupu" : kupHesapla}
print(k["karesi"](4))

print(k["kupu"](5))
"""

#Fonksiyon kullanım örnek
"""
a = 0

if a:
    def yeap():
        print("ilk yeap")
else:
    def yeap():
        print("ikinci yeap")

yeap()
"""

#Lambda fonksiyolar
#isimsiz fonksiyonlar
#lambda <parametre>:<işlem>
"""
a = lambda k : k + 10

print(a(3))
"""

#lambda kullanmadan fonksiyon ile yazımı
"""
def kareHesapla( a ):
    return a ** 2

k = kareHesapla( 12 )
print( k )
"""

#lambda kullanarak yazımı
"""
kareHesapla = lambda a : a ** 2

print(kareHesapla( 5 ))
"""

#iki değerli lambda örneği 
#lambda ile
"""
topla = lambda a , b : a + b
print(topla(20 , 25))
"""

#fonksiyon ile
"""
def topla(a , b):
    return a + b

print(topla(10 ,15))
"""

#Lambda örnek - 1
#lambda ile
"""
a = (lambda k : 
    "tek" if k%2 
    else "çift")

print(a(2))
"""

#fonksiyon ile
"""
def a(k):
    if k%2:
        print("Tektir")
    else:
        print("Çifttir")

a(11)
"""
#Lambda örnek - 2
"""
a = lambda k, v, m : k * v * m

print( a(k = 2 , m = 3 , v = 10)) #sırasını farklı yzabiliriz
"""

#Lambda örnek - 3
#lambda fonksiyonunda default değerli parametreler
"""
a = lambda k, v = 10 : k + v # v değeri default 10

print( a(4) )
"""

#Lambda örnek - 4
#lambda ile * ile birden fazla değer kullanmak(tuple)
"""
a = lambda *k: sum(k) #sum(): toplama fonksiyonu

print( a(3,4,5) )
"""

#Lambda örnek - 5
##lambda ile ** dictionary yapısı kullanmak
"""
a = lambda *k: sum(k) 
print( a(3,4,5) )

b = lambda **m : sum(m.values())
print(b(g = 5 , y = 3))
"""

#Lambda örnek - 6
#fonksiyon içinde lambda kullanımı
"""
def yeap(a):
    return lambda k: k * a

m = yeap(3)

print( m(2) )
"""




