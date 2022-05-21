#print başına f (format) koyarak isimlendirme
"""
name = input("İsim Giriniz:")
print(f"hello, {name}")
"""

#İlk kelimenin baş harfini büyük yapma fonksiyonu .capitalize()
"""
name = "murat candan"
name = name.capitalize()
print (name)
"""

#Tüm kelimelerin baş harfini büyük harfle yazar .title()
"""
name = "murat candan"
name = name.title()
print (name)
"""

#Tüm aradaki boşlukları temizler .strip()
"""
txt = "     banana     "
txt = txt.strip()
print("of all fruits", txt, "is my favorite")
"""

#İşlemi en yakın tam sayıya yuvarlar round()
"""
x = 3.1
y = 2.6
z = round(x + y)
print(z)
"""
#Eğer virgülden sonra 2 basamak yaz ve yuvarla gibi atama yapmak istersek
"""
x = 2
y = 3
z = round(x / y , 2)
print(z)
"""

#yukarıdaki örneğin farklı yazım şekli
"""
x = 2
y = 3
z = x / y
print(f"{z:.2f}")
"""

#Eğer sayıyı yazarken okunuş için virgül olmasını istersek
#Örnek 10000 yerine 10,000 gibi
"""
z = 100000000
print(f"{z:,}")
"""
 
 #fonksiyonları daha okunabilir tek satırda yazabiliriz

"""
 def is_even(n):
     return True if n % 2 == 0 else False

"""
#liste içinde çoklu dict yaratma ve for döngüsü ile içine ulaşma
"""
students = [
    {"name": "Hermione" , "house": "Gryffindor","patronus": "Otter"},
    {"name": "Harry" , "house": "Gryffindor","patronus": "Stag"},
    {"name": "Ron" , "house": "Gryffindor","patronus": "Terrier"},
    {"name": "Draco" , "house": "Slytherin","patronus": None },
]

for student in students:
    print(student["name"], student["house"],student["patronus"], sep=", ")
"""