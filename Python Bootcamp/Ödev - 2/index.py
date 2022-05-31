
class Animal:
    def __init__(self, age, gender):
        self.age = int(age)
        self.gender = str(gender)

    def isMammal():
        pass

    def mate():
        pass


class Duck(Animal):
    def __init__(self, beakColor="yellow"):
        self.beakColor = str(beakColor)

    def swim():
        pass

    def quack():
        pass


class Fish(Animal):
    def __init__(self, sizeInFt, canEat):
        self.__sizeInFt = int(sizeInFt)
        self.__canEat = bool(canEat)

    def __swim():
        pass


class Zebra(Animal):
    def __init__(self, is_wild):
        self.is_wild = bool(is_wild)

    def run():
        pass
