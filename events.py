from random import randint
import ru_local as ru


def burn_place(player):
    number = int(input(f'{ru.BURN_PLACE}'))
    if number == 1:
        i = randint(3, 8)
        player.set_science_and_technology(player.science_and_technology + i)
    elif number == 2:
        i = randint(1, 3)
        player.set_military_power(player.military_power + i)
    elif number == 3:
        player.set_resources(player.resources + 100)
    else:
        print('Try again') and burn_place(player)


def nature_event(player):
    number = int(input(f'{ru.NATURE_EVENT}'))
    if number == 1:
        i = randint(-45, -10)
        player.set_population(player.population + i)
    elif number == 2:
        player.set_territory(player.territory - 30)
    else:
        print('Try again') and nature_event(player)


def conflict(player):
    number = int(input(f'{ru.CONFLICT}'))
    if number == 1:
        player.set_population(player.population + 0)
    elif number == 2:
        i = randint(-20, 0)
        m = randint(0, 50)
        player.set_population(player.population + i) and player.set_territory(player.territory + m)
    else:
        print('Try again') and conflict(player)


def reform(player):
    number = int(input(f'{ru.SECOND_REFORM}'))
    if number == 1:
        print(f'{ru.SUCCESS}')
        if player.resources < 20:
            print(f'{ru.NO_RESOURCES2}') and reform(player)
        player.set_grow_population(player.grow_population + 0.3) and player.set_resources(player.resources - 20)
    elif number == 2:
        player.set_population(player.population + 0)
    else:
        print('Try again') and reform(player)


def science(player):
    print(f'{ru.OPEN_SCIENCE}')
    i = randint(1, 5)
    player.set_science_and_technology(player.science_and_technology + i)


def popul(player):
    number = int(input(f'{ru.POPUL}'))
    if number == 1:
        i = randint(-20, -10)
        if player.resourses < abs(i):
            print(f'{ru.NO_RESOURCES2}') and popul(player)
        else:
            player.set_resourses(player.resourses + i) and player.set_population(player.population + 50)
    elif number == 2:
        player.set_population(player.population + 0)
    else:
        print('Try again') and popul(player)


def medicine(player):
    number = int(input(f'{ru.MEDICINE}'))
    if number == 1:
        i = randint(-40, -10)
        player.set_population(player.population + i)
    elif number == 2:
        if player.resources < 10:
            print(f'{ru.NO_RESOURCES}') and medicine(player)
        else:
            player.set_science_and_technology(player.science_and_technology + 2) and player.set_resources(
                player.resources - 10)
    else:
        print('Try again') and medicine(player)


def military_up(player):
    number = int(input(f"""{ru.MILITARY_UP}
                       {ru.APPLY}
                       {ru.DECLINE}"""))
    if number == 1:
        player.set_military_power(player.military_power + 3) and player.set_resources(player.resources + -15)
    elif number == 2:
        player.set_science_and_technology(player.science_and_technology + 1)
    else:
        print('Try again') and medicine(player)


def attack(player):
    number = int(input(f'{ru.ATTACK}'))
    while number != 1 or number != 2:
        print(f'{ru.TRY_AGAIN}')
        number = int(input(f'{ru.ATTACK}'))
    if number == 1:
        if player.military_power < 5:
            print(f'{ru.UNLUCKY_ATTACK}')
            player.set_population(player.population + -30) and player.set_resources(
                player.resources + -15) and player.set_territory(player.territory + -10)
        else:
            print(f'{ru.SUCCESS_ATTACK}')
            player.set_population(player.population + 50) and player.set_resources(
                player.resources + 25) and player.set_territory(player.territory + 80)
    elif number == 2:
        i = randint(1, 2)
        if i == 1:
            print(f'{ru.DIPLOMACY}')
        else:
            print(f'{ru.NO_DIPLOMACY}')
            if player.military_power < 5:
                print(f'{ru.UNLUCKY_ATTACK}')
                player.set_population(player.population + -30) and player.set_resources(
                    player.resources + -15) and player.set_territory(player.territory + -10)
            else:
                print(f'{ru.SUCCESS_ATTACK}')
                player.set_population(player.population + 50) and player.set_resources(
                    player.resources + 25) and player.set_territory(player.territory + 80)


def peace(player):
    number = int(input(f'{ru.PEACE}'))
    if number == 1:
        player.set_military_power(player.military_power + 2) and player.set_resources(player.resources + 10)
    elif number == 2:
        if player.military_power < 3:
            print(f'{ru.VERY_UNLUCKY_ATTACK}')
            player.set_population(player.population + -30) and player.set_resources(
                player.resources + -10) and player.set_territory(player.territory + -10)
        else:
            print(f'{ru.VERY_SUCCESS_ATTACK}')
            player.set_population(player.population + 30) and player.set_resources(
                player.resources + 20) and player.set_territory(player.territory + 40)
    else:
        print('Try again') and peace(player)


events = {
    1: burn_place,
    2: nature_event,
    3: conflict,
    4: reform,
    5: science,
    6: popul,
    7: medicine,
    8: military_up,
    9: attack,
    10: peace,
    11: burn_place,
    12: burn_place,
    13: burn_place,
    14: burn_place
}
