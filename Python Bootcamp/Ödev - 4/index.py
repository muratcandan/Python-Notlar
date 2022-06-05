
# 1. soru
"""
def unique():
    a = ["a", "b", "a", "c"]
    benzersiz = []
    for i in a:
        if i not in benzersiz:
            benzersiz.append(i)
    print(benzersiz)


unique()
"""


# 2. soru
"""
def mailKontrol():
    mailAdresi = input("Lütfen mail giriniz:")
    mailAdresi = mailAdresi.lower()
    mailAdresi = mailAdresi.strip()
    b = mailAdresi.find("@")
    c = mailAdresi.find(".")
    d = mailAdresi.find(".edu.")
    e = mailAdresi.startswith("@")
    f = mailAdresi.endswith(".edu.")
    if b != -1 and c != -1 and d != -1 and b < d and e == False and f == False:
        print("Mail doğru")
    else:
        print("Mail yanlış")

mailKontrol()
"""
