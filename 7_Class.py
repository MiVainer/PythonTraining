
class Hero():
    """Описание персонажа для игры"""
    def __init__(self, name, level, race): # данный метод всегда стоит первым в классе
        """Инициализация персонажа"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Напечатать параметры персонажа"""
        discription = (self.name + "\nlevel is " + str(self.level) + "\nrace is " + self.race + "\nhealth is " + str(self.health) + '\n').title()
        print(discription)

    def level_up(self):
        """Повышение уровня персонажа"""
        self.level += 1

    def move(self):
        """Наинаем движение"""
        print("Hero " + self.name + " начал движение")

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """Класс, наследующий параметры из класса Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Инициализация класса"""
        super().__init__(name, level, race) #Перекидываем переменные из родительского класса
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        self.magic -= 10 #Понижение на 10 при каждом использовании

    def show_hero(self):
        """Напечатать параметры персонажа"""
        discription = (self.name + "\nlevel is " + str(self.level) + "\nrace is " + self.race + "\nhealth is " + str(self.health) + '\nMagic is ' + str(self.magic)).title()
        print(discription)

"""Создание объекта (персонажа)"""
myhero1 = Hero('Vurdalak ', 5, 'ork ')

myhero2 = Hero('Miha', 4, 'human ')

mysuperhero = SuperHero('Semen', 10, 'elf', 15)

myhero1.show_hero()
myhero2.show_hero()

myhero1.move()
myhero2.move()

myhero2.level_up()
myhero2.show_hero()

myhero1.set_health(50)
myhero1.show_hero()

mysuperhero.show_hero()
mysuperhero.makemagic()
mysuperhero.show_hero()