
def toplam(func):
    def wrapper(a):
        func(a)
        toplama = 0
        for i in range(1, a + 1):
            toplama += i
        print(a, "sayısına kadar toplam:", toplama)
    return wrapper


@toplam
def faktoriyel(a):
    fakt = 1
    for i in range(1, a + 1):
        fakt = fakt * i
    print(a, "sayısının faktoriyeli", fakt)


faktoriyel(20)
