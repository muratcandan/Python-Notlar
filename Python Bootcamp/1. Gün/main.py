#Ekrana çıktı almak için print fonksiyonu kullanılır
print( "Hello world!" )

#Python'da tek satır yorum yazmak # simgesi ile yapılır
"""""
çoklu 
satırda
yorum yazmak için üç tırnak arasına yazılır
"""
#değişken atama yöntemi
a = 5
b = "ali"
c = 3.14

#tam sayı (integer) çoklu atama yöntemi
a, b, c=10,15,20
print(a,b,c)

#metinsel(string) ifadeleri atama yöntemi
a = "murat"
print( a )

#ondalık sayı (float) atama yöntemi
d = 3.5
print( type(d) )

#doğru-yanlış(boolean) ifadeleri atama yöntemi
c = True

#verinin tipini öğrenmek için type komutu kullanılır
type( c )

#geçici değişken yöntemi ile değerleri takas etme
a = 10
b = 5
tmp = a
a=b
b = tmp
print("a değeri" , a , "b değeri" , b)

#değişkenleri geçici değişken oluşturmadan python'da takaslayabiliyoruz
a = 10
b = 60
a , b = b , a
print("a değeri" , a , "b değeri" , b)

