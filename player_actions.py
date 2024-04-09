from random import randint


def menu_stats(player):
    print("Статистика игрока")
    print("*****************")
    print(player.stats())


def eat(player):
    number = int(input("Посадить продовольствие?\n"
          "1)Да\n"
          "2)Нет\n"))
    if number == 1:
        i = int(input('Какую часть территории вы собираетесь выделить?\n'))
        player.resources += randint(1, 5) * 5 * (i//10)
        player.territory -= (i//10)*10
    else:


def science(player):
    number = int(input(f'Использовать 25 ед ресурсов для развития науки на 1 единицу?\n'
                       f'1)Да\n'
                       f'2)Нет\n'))
    if number == 1:
        player.resources -= 25
        player.science_and_technology += 1
    else:

def military(player):
    number = int(input(f'Использовать 25 ед ресурсов для повышения военной мощности государства на 1 единицу?\n'
                       f'1)Да\n'
                       f'2)Нет\n'))
    if number == 1:
        player.resources -= 25
        player.military_power += 1


def territory(player):
    number = int(input(f'Отправить рабочих на освоение примыкающей к государству лесной местности?\n'
                       f'1)Да, введите количество:\n'
                       f'2)Нет\n'))
    if number != 2:
        player.population -= (randint(0,10)/10)*number
        player.territory += randint(5,15)*number
    else:


def

actions = {
    '0':menu_stats,
    '1':eat,
    '2':science,
    '3':military,
    '4':territory,
    '5':
    }