from random import randint


def players():
    players_count = int(input('Введите количество игроков: '))
    players = {}
    for i in range(players_count):
        p = Player()
        players[i + 1] = p


class Player:
    population = 100
    economy = 100
    military_power = 100
    science_and_technology = 100
    resources = 100
    territory = 100

    def stats(self):
        return (f"""Население вашего государства: {self.population}
Ваша экономика: {self.economy}
Военная мощь государства: {self.military_power}
Наука и технологии: {self.science_and_technology}
Ваши ресурсы: {self.resources}
Ваши территории: {self.territory}""")


p = Player()


class Enemy:
    hp = randint(70, 130)
    damage = randint(6, 13)


def menu(p):
    while True:
        print(f"""
Меню:
1) Сражаться
2) Статистика
3) Посадить зерно""")
        n = input("Введите число: ")

        if int(n) == 1:
            menu_fight(p)
        elif int(n) == 2:
            menu_stats(p)
        elif int(n) == 3:
            eat(p)
        else:
            print("Чего ждем?")


def menu_stats(p):
    print("Статистика игрока")
    print("*****************")
    print(p.stats())


def eat(p):
    print("Посадить зерно")
    p.resources += randint(1, 5) * randint(1, 5)
    p.territory -= 10


def menu_fight(p):
    p.hp = 100
    e = Enemy()

    print(f"Вы hp: {p.population} damage: {p.military_power}")
    print(f"Враг hp: {e.hp} damage: {e.damage}")
    print("**********************")
    while e.hp > 0:
        print("1)Ударить")
        print("2)Хил 0-5")
        n = input("Введите число: ")
        if int(n) == 1:

            e.hp -= p.military_power
            print(f"Вы ударили противника, у него осталось {e.hp} hp")
            p.population -= e.damage
            print(f"Противник ударил вас, у вас осталось {p.population} hp")

            print("*********************")

        elif int(n) == 2:

            p.population += randint(0, 5)
            if p.population > 100:
                p.population = 100

            print(f"Ваши хп {p.population}")

        else:
            print("Чего ждем?")
        if p.population < 0:
            print("Вы проиграли")
            break
        if e.hp < 0:
            print("Вы победили")
            break


menu(p)
