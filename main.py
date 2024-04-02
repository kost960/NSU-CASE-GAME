from random import randint


class Player:
    population = 100
    economy = 10
    military_power = 0
    science_and_technology = 0
    resources = 0
    territory = 0

p = Player()


class Enemy:
    hp = randint(70, 130)
    damage = randint(6, 13)


def menu(p):
    while True:
        print("""1) Сражаться
2) Статистика
3) Посадить зерно""")
        try:
            n = input("Введите число: ")

            if int(n) == 1:
                menu_fight(p)
            elif int(n) == 2:
                menu_stats(p)
            elif int(n) == 3:
                eat(p)
            else:
                print("Чего ждем?")

        except NameError:
            ...
        except SyntaxError:
            ...
        except ValueError:
            ...


def menu_stats(p):
    print("Статистика игрока")
    print("*****************")
    print(f"""
Население вашего государства: {p.population}
Ваша экономика: {p.economy}
Военная мощь государства: {p.military_power}
Наука и технологии: {p.science_and_technology}
Ваши ресурсы: {p.political_stability}
Ваши территории: {p.territory}
""")

def eat(p):
    print("Посадить зерно")
    p.resources += randint(1, 5) * randint(1, 5)
    p.territory -= 10

def menu_fight(p):
    p.hp = 100
    e = Enemy()

    print(f"Вы hp: {p.hp} damage: {p.damage}")
    print(f"Враг hp: {e.hp} damage: {e.damage}")
    print("**********************")
    while e.hp > 0:
        print("1)Ударить")
        print("2)Хил 0-5")
        n = input("Введите число: ")
        if int(n) == 1:

            e.hp -= p.damage
            print(f"Вы ударили противника, у него осталось {e.hp} hp")
            p.hp -= e.damage
            print(f"Противник ударил вас, у вас осталось {p.hp} hp")

            print("*********************")

        elif int(n) == 2:

            p.hp += randint(0, 5)
            if p.hp > 100:
                p.hp = 100

            print(f"Ваши хп {p.hp}")

        else:
            print("Чего ждем?")
        if p.hp < 0:
            print("Вы проиграли")
            p.fol += 1
            break
        if e.hp < 0:
            print("Вы победили")
            p.wins += 1
            break


menu(p)
