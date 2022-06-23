import numpy as np

# Listeden numpy Array(dizi)'i oluşturma(matrix olarak)
"""
matrix_listesi = [[35, 42, 49], [56, 63, 70], [12, 24, 36]]
print(np.array(matrix_listesi))
"""

# numpy dizisi oluşturma(ilk-son-atlama miktarı)
"""
print(np.arange(0, 20, 2))
"""
# zeros sıfırlardan oluşan dizi oluşturur
"""
print(np.zeros(2))
print(np.zeros((5, 5)))  # kaça kaçlık matris istersek oluşturabiliriz
"""

# ones bu sefer 1'lerden oluşan dizi,matris oluşturur
"""
print(np.ones((7, 7)))
"""

# aralık arasını kaç elemanlı dizi isteniyorsa eşit olarak bölerek veren komut
"""
print(np.linspace(0, 20, 6))
print(np.linspace(0, 10, 20))  # float olarak eşit böler
"""

# eye komutu soldan sağa 1 olan diğer elemanları 0 olan matris verir
# genelde matrisin tersini alma gibi durumlarda kullanılır
"""
print(np.eye(5))
"""

# numpy içindeki random kütüphanesi
# randn rastgele dizi veya matris oluşturur
"""
print(np.random.randn(4))
print(np.random.randn(5, 5))
"""

# belli aralık arasında(son değeri döndürmez) tek bir tam sayı değer döndürmek için rand int
"""
print(np.random.randint(0, 10))
print(np.random.randint(1, 300, 5))  # 1'den 300'e kadar 5 tane tam sayı döndür
"""

# numpy metodlarından elde edilen sayıları bir değişkene eşitleme
"""
benimDİzim = np.random.randint(1, 10)
print(benimDİzim)
"""

# reshape elimizdeki diziyi istenen matris kaça kaçlıksa ona çevirir
# not: yeterli eleman olması gerekir (örnek:30 elaman varsa 6*5 yada 3*10 gibi)
"""
dizim = np.random.randint(0, 100, 30)
print(dizim)
dizim = dizim.reshape(5, 6)
print(dizim)

print(dizim.max())  # dizideki maksimum verir
print(dizim.min())  # dizideki minimum değeri verir
print(dizim.argmax())  # dizideki maksimum değerin index değerini verir
print(dizim.argmin())  # dizideki minimum değerin index değerini verir
"""

# numpy dizileri de listedeki özellikleri taşıyor
"""
benim_dizim = np.arange(0, 15)

print(benim_dizim[5])
print(benim_dizim[2:10])
"""

# ancak listelerden farklı özelliklere de sahipler
# dizideki belli bir bölümün değerini belirleyebiliriz
"""
benim_dizim = np.arange(0, 15)

benim_dizim[2:8] = -5
print(benim_dizim)
"""

# numpy'da başka bir diziden oluşturulan dizi değiştirilirse orjinal diziyi de etkiler
# bunu istemediğimiz durumlarda copy olarak başka bir dizi olduğunu belirtmemiz gerekir
"""
birinci_dizi = np.arange(0, 24)
ikinci_dizi = birinci_dizi[5:12]
print(birinci_dizi)
print(ikinci_dizi)

ikinci_dizi[:] = 700
print(ikinci_dizi)
print(birinci_dizi)  # şu an bu dizi de değişti

# bu durumu yok etmek için kopyasını oluşturuyoruz
# böylece kopyası ancak farklı dizi oluşturuyoruz
# biri diğerini etkilememiş oluyor
birinci_dizi_kopya = birinci_dizi.copy()

birinci_dizi_kopya[:] = 900
print(birinci_dizi_kopya)
print(birinci_dizi)
"""

# Matrix Ornekler - 1
"""
benim_listem = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                [214, 1120, 11531, 1512], [5219, 15210, 11251, 152]]

benim_listem = np.array(benim_listem)
print(benim_listem)

print(benim_listem[0])

print(benim_listem[0][2])
# yukarıdaki yazım ile aynı değeri veirir
print(benim_listem[0, 2])

# 1. indexten başlayıp devamını getir ve onların 2. indexini getir
print(benim_listem[1:, 2])
print(benim_listem[1:, 2:])

# 0,2 ve 4. indexleri al ve liste şeklinde getir
print(benim_listem[[4, 2, 4]])
"""

# Numpy'da Operasyonlar
"""
yenibir_dizi = np.random.randint(1, 100, 20)

print(yenibir_dizi)

# büyüktür küçüktür ile false true şeklinde döndürebiliriz
kontrol_dizisi = yenibir_dizi > 24
print(kontrol_dizisi)
# sadece 24'den büyük rakamları görmek istersek
print(yenibir_dizi[kontrol_dizisi])

# dizilerde matematiksel işlemler de yapabiliriz

print(yenibir_dizi + yenibir_dizi)
print(np.sqrt(yenibir_dizi)) #karekök alma
"""
