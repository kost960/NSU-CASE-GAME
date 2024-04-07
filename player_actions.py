from random import randint
def menu_stats(player):
    print("Статистика игрока")
    print("*****************")
    print(player.stats())
def eat(player):
    print("Посадить зерно")
    player.resources += randint(1, 5) * 5
    player.territory -= 10

actions = {
    '0':menu_stats,
    '1':eat,
    }