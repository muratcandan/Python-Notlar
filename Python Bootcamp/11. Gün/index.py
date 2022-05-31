# comprehension olmadan örnek - 1
"""
a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 6]
c = []

for i in a:
    if i not in b:
        c.append(i**3)

print(c)
"""

# comprehension ile örnek - 1
"""
a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 6]

d = [i ** 3 for i in a if i not in b]
print(d)
"""

# Iteratorler
# tekrarlı yinelenen verileri kullanılma halidir
# tekrarlanabilen objelerdir
# bir objenin iterator olması için 1. __iter__() , 2. __next__() objesi olmalıdır
# iterable objeler: list, tuple, string, range
# iterable yapılar kaynak tüketimi açısından daha verimlidir
# iterable yapılar sonlu bellekte teorik olarak sonsuz bellek yaratır

# Iterator yazım örneği
"""
sayilar = [23, 34, 54, 76]

a = iter(sayilar)  # a içinde iteratör oluşturma
print(next(a))  # her next bir sonraki elemana konumlanıyor
print(a.__next__())  # aynı şekilde böyle de çağırabiliyor
print(next(a))
print(next(a))
print(next(a))  # StopIteration hatası veriyoruz çünkü menzil dışına çıktık
"""

# For döngüsü aslında alttaki gibi elemanlara while ile ulaşır
"""
sayilar = [23, 34, 54, 76]
a = iter(sayilar)

while True:
    try:
        k = next(a)
        print(k)
    except StopIteration:
        break
"""

# custom iteratorler
"""
class Ornek:
    def __init__(self, son=0):
        self.son = son

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.son:
            k = 2 ** self.n
            self.n += 1
            return k
        else:
            raise StopIteration


a = Ornek(5)

i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))  # StopIteration hatası alırız

for i in Ornek(3):
    print(i)
"""

# Iterator örneği
"""
class Sonsuz:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

a = iter(Sonsuz())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
"""

# Generatorler
# iteratorlerin daha kolay oluşturulabilen yöntemidir
# tek tek çağırdığı için bellekte yer kaplamazlar
# yield anahtar sözcüğü ile kullanılır

# generatorler kullanım şekli
"""
def a():
    n = 1
    yield n  # n'i return etmiş olduk


print(a())  # <generator object a at 0x000002D4F4699A10>

print(next(a()))
print(next(a()))
print(next(a()))
print(next(a()))
print(next(a()))

for i in a():
    print(i)
"""

# generator örneği - 1

"""
def gen():
    n = 1
    print("ilk")
    yield n
    n = 2
    print("iki")
    yield n
    n = 3
    print("üç")
    yield n
for k in gen():
    print(k)

a = gen()
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # StopIteration hatası alırız
"""

# generator örneği - 2
"""
def sayilar(max):
    for i in range(max):
        yield i


a = sayilar(20000000000)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
"""

# generator oluşturmadan - 3
# bellekte yer kaplar
"""
def kup():
    a = []
    for i in range(1, 30):
        a.append(i ** 3)
    return


print(kup())
"""

# generator ile - 3
"""
def kup():
    for i in range(1, 30):
        yield i ** 3


i = kup()
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
"""

# Dipnot:
# yukrıdaki örnekte iter oluşturmadan yaptığımız için yeniden
# fonksiyon oluşturursak 0'^dan başlar ancak iter yapısı tek seferde kullanılır
# ikinci iter oluşsa bile kaldığı yerden devam eder

"""
def kup():
    for i in range(1, 5):
        yield i ** 3


gen = kup()

i1 = iter(gen)
print(next(i1))
print(next(i1))
print("-----")

# yeni iter yapsak bile nerde kaldıysa devam eder
i2 = iter(gen)
print(next(i2))
"""

# list comprehension'u generator'e çevirme
"""
sayilar = [i * 5 for i in range(3)]
print(sayilar)

# generator'e çevirirken tuple gibi dönüştürürüz
gen = (i * 5 for i in range(1, 4))

print(gen)

i = iter(gen)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
"""

# Anahtar kelimeler: flex,django, request-response

# Flask framework'üne geçtik konu anlatımı diğer klasörde
