from random import randint


def menu_stats(player):
    print("Статистика игрока")
    print("*****************")
    print(player.stats())


def eat(player):
    print("Посадить продовольствие")
    i = int(input('Какую часть территории вы собираетесь выделить?\n'))
    player.resources += randint(1, 5) * 5 * (i//10)
    player.territory -= (i//10)*10


actions = {
    '0':menu_stats,
    '1':eat,
    }