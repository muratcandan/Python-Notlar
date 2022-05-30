import time


def kare():
    kare_uzunluk = float(
        input("Lütfen karenin kenar uzunluğunu giriniz:"))
    kare_cevre = (4 * kare_uzunluk)
    print("Çemberin çevresi:", kare_cevre)
    time.sleep(5)
    sorgu()


def cember():
    pi = 3.14
    cember_yaricap = float(
        input("Lütfen çemberin yarıçap uzunluğunu giriniz:"))
    cember_cevre = (2 * pi * cember_yaricap)
    print("Çemberin çevresi:", cember_cevre)
    time.sleep(5)
    sorgu()


def dikdortgen():
    dikdortgen_kenar_1 = float(
        input("Lütfen dikdörtgenin birinci kenar uzunluğunu giriniz:"))
    dikdortgen_kenar_2 = float(
        input("Lütfen dikdörtgenin ikinci kenar uzunluğunu giriniz:"))
    dikdortgen_cevre = ((2 * dikdortgen_kenar_1) + (2 * dikdortgen_kenar_2))
    print("Dikdörtgen çevresi:", dikdortgen_cevre)
    time.sleep(5)
    sorgu()


def paralelkenar():
    paralelk_1 = float(
        input("Lütfen paralelkenarın birinci kenar uzunluğunu giriniz:"))
    paralelk_2 = float(
        input("Lütfen paralelkenarın ikinci kenar uzunluğunu giriniz:"))
    paralelk_cevre = ((2 * paralelk_1) + (2 * paralelk_2))
    print("Paralelkenarın çevresi:", paralelk_cevre)
    time.sleep(5)
    sorgu()


def sorgu():
    kullanici_sorgu = int(
        input("""Çevre Hesaplama:
    Karenin çevresini hesaplamak için 1’e basınız.
    Çemberin çevresini hesaplamak için 2’e basınız.
    Dikdörtgenin çevresini hesaplamak için 3’e basınız.
    Paralelkenarın çevresini hesaplamak için 4’e basınız.
    Programdan çıkmak için -1’ e basınız.
    
    Seçiminizi Yapınız :""")
    )

    if kullanici_sorgu == 1:
        kare()
    elif kullanici_sorgu == 2:
        cember()

    elif kullanici_sorgu == 3:
        dikdortgen()

    elif kullanici_sorgu == 4:
        paralelkenar()

    elif kullanici_sorgu == -1:
        pass

    else:
        print("istenilen değerlerden herhangi birini seçmediniz")
        time.sleep(3)
        sorgu()


sorgu()
