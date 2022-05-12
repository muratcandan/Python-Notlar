
# \ ile satır inerek aynı satırda olmadan koda devam edebiliyoruz 
"""""
a= 5 and b=7 and \
    c=14
"""""

#karmaşık sayılar(complex) yazma yöntemi
d= 10 + 7j
print( type( d ) )

#python'da tür dönüşümü yapma
a="10"
b=int( a )
print( type( b ) )

#Python'da 0 ve "" False olarak döner, diğer tüm değerler True'dur
a = ""
b = 0
print( bool(a) , bool(b))

#Değişken ismi kuralları
"""     1-  sayı ile başlamaz 
        2- _ ile başlayabilir
        3 - keyworldler ile başlamaz (list,set gibi)
        4 - değişkenler arasına boşluk koyulmaz
"""
#Python Değişken Yazım Şekilleri: camelCase - PascalCase - snake_case
camelCase = 1
PascalCase = 2
snake_case = 3

#print fonsiyonunda tırnaklar farklı oldukça python onu algılar
print( 'Selam benim adım "Murat" ' )

#print fonsiyonunun varsayılan özelliklerini üstüne mouse imleci ile gelerek görebiliriz(VSCode)
# varsayılan özelliği değiştirebiliriz
a="ahmet"
b="mehmet"
print(a , b)
print(a , b , sep="++") #sep ayrımdan sonra aralarına ne geleceğini değiştirir
print(a , b , sep="\n") #alt satırda yazmak için \n kullanılır

#format fonksiyonu kullanımı ve farklı yöntemleri
print( "a değişkeni {} ve b değişkeni {}'dir" .format(a,b) )
print( "a değişkeni " , a , "ve b değişkeni " , b ,"'dir" )
print( "a değişkeni " , str(7) , "ve b değişkeni " , str(10),"'dur" )

#print yaparken önüne * işareti konarsa sep değerini harf harf aralarına konulacak ifadeyi belirleyebiliriz
print(*"Murat" , sep="+")

#Kaçış karakterleri \n: alt satıra geçirir \:string ifadesinin devam ettiğini belirtir devamındaki
#karakteri yok sayar
#mesela tırnak karışıklığının yaşanmaması için kullanılabilir
print('İstanbul\'un merkezi')

#\a önceki yazılanı yok sayar
print("Ahmet Mehmet\a Kamil Hakkı")
#başlangıca r koyarsak kaçır karakterlerinin hepsini yok sayar
#bu durum klasör konumu belirtirken işe yarar
print(r"ahmet\mehmet\c.txt")

#formatı dışardan atmak istersek yöntem
a = "Benim adım {}"
a = a.format( "Murat" )
print( a )

#Matematiksel operatörler
#üs alma ** ile sağlanır 
print(5**2)

#mod alma % ile yapılır kalanı verir
print(12%5)

#taban bölme işlemi // ile yapılır kalansız tam sayı olarak böler
print(5//2)

# + - / * diğer matematiksel operatörlerdir

#atama operatörleri 
e = 10
e += 10 # e = e + 10
e *= 5 # e = e * 5
print( e )

# ==: eşittir !=: eşit değildir
a = 5
b = 10
a==b
print( a != b )

#koşul ifadeleri and && , or || , not !

#and durumu, her durumun doğru olması gereklidir yoksa False çıkartır
a = 5
b = 10
print( a == 5 and b == 10 )
print( a == 10 and b == 3 )
print( a == 5 and b == 7 ) 

#or durumu, sadece bir durumun doğru olduğunda True çıkartır
a = 5
b = 10
print( a == 5 or b == 10 )
print( a == 10 or b == 3 )
print( a == 5 or b == 7 )

#not durumu, durumun tam tersini çıktı verir
a = 5
b = 10
print( a != 5 )
print( a != 10 )
print( a != 5 )

#id ile bellekteki yer kapladığı konum bulunur
print( id ( 5 ) )
print( id ( 10 ) )

# is komutu ile aynı bellekte olup olmadığı konmtrol edilir
c = 10
d = 20
print( id ( c) )
print(id ( d ))
print( c is d )

#in ve not in operatörü içerisinde var mı yok mu konmtrolü sağlanabilir
a="Ahmet Mehmet"
print("b" in a)
print("q" not in a)

#constant değerler sabitlerdir değiştirilemeyen değerlerdir. Python'da yoktur. Diğer dillerde karşımıza çıkabilir
#geleneksel olarak constant değerler büyük harfle yazılır
FILE_SIZE = 1234114

