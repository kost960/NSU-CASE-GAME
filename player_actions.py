from random import randint
import ru_local as ru


def menu_stats(player):
    print("Статистика игрока")
    print("*****************")
    print(player.stats())


def eat(player):
    number = int(input(f"""{ru.EAT}
{ru.YES}
{ru.NO}
"""))
    if number == 1:
        i = int(input(f'{ru.EAT2}\n'))
        player.set_resources(player.resources + randint(1, 5) * 5 * (i//10))
        player.set_territory(player.territory - (i//10)*10)
        return True
    elif number == 2:
        return False
    else:
        print(f'Wrong, try again')
        return False


def science(player):
    number = int(input(f"""{ru.SCIENCE}
{ru.YES}
{ru.NO}
"""))
    if number == 1:
        if player.resources < 25:
            player.resources = 0
        else:
            player.resources -= 25
        player.science_and_technology += 1
        return True
    elif number == 2:
        return False
    else:
        print(f'Wrong, try again')
        return False


def military(player):
    number = int(input(f"""{ru.MILITARY}
{ru.YES}
{ru.NO}
"""))
    if number == 1:
        player.resources -= 25
        player.military_power += 1
        return True
    elif number == 2:
        return False
    else:
        print(f'Wrong, try again')
        return False


def territory(player):
    number = int(input(f"""{ru.TERRITORY}
{ru.YES}
{ru.NO}
"""))
    if number == 1:
        quantity = int(input(f'{ru.QUANTITY}'))
        player.population -= (randint(0,10)/10)*quantity
        player.territory += randint(5,15)*quantity
        return True
    elif number == 2:
        return False
    else:
        print(f'Wrong, try again')
        return False

def reform(player):
    number = int(input(f"""{ru.REFORM}
{ru.CARRY}
{ru.NOT_CARRY}
"""))
    if number == 1:
        if player.resources < 350 or player.territory < 101:
            print(f'{ru.NO_RESOURCES}')
            return False
        else:
            player.resources -= 350
            player.territory -= 100
            player.economy += 1
            return True
    elif number == 2:
        return False
    else:
        print(f'Wrong, try again')
        return False




actions = {
    '0':menu_stats,
    '1':eat,
    '2':science,
    '3':military,
    '4':territory,
    '5':reform
    }