from random import randint


def edit_res(res, quantity):
    res += quantity
    if quantity > 0:
        if f'{res}' == 'player.population':
            print(f'Численность населения увеличина на{quantity}\n')
        elif f'{res}' == 'player.military_power':
            print(f'Военное преимущество усилено на{quantity}\n')
        elif f'{res}' == 'player.science_and_technology':
            print(f'Наука и технологии развиты на{quantity}\n')
        elif f'{res}' == 'player.resources':
            print(f'Запасы ресурсов пополнены на{quantity}\n')
        else:
            print(f'Территория расширена на{quantity}\n')
    elif quantity < 0:
        if f'{res}' == 'player.population':
            print(f'Было потеряно {quantity} населения\n')
        elif f'{res}' == 'player.military_power':
            print(f'Военное преимущество ослабло на {quantity}\n')
        elif f'{res}' == 'player.science_and_technology':
            print(f'Потери в развитии науки и технологи состовляют {quantity}\n')
        elif f'{res}' == 'player.resources':
            print(f'Потрачено {quantity} единиц ресурсов\n')
        else:
            print(f'Территория уменьшилась на {quantity}\n')
    else:
        print(f'Вам повезло, вы сохранили доступные ресурсы')


def burn_place(player):
    number = int(input(f'Ваше государство обнаруживает новое месторождение ценного ресурса. Решите, как лучше использовать эту находку: \n'
          f'1)На развитие науки и технологий\n'
          f'2)Увеличить военное преимущества\n'
          f'3)Сохранить для возможного использования в будущем\n'))
    if number == 1:
        i = randint(3, 8)
        edit_res(player.science_and_technology, i)
    elif number == 2:
        i = randint(1, 3)
        edit_res(player.military_power, i)
    elif number == 3:
        edit_res(player.resources, 100)
    else:
        print('Try again') and burn_place(player)


def nature_event(player):
    number = int(input(f'В вашем государстве происходит природная катастрофа. Необходимо быстро принять решение о том, как справиться с последствиями: \n'
          f'1)Отправить часть населения на пораженные зоны\n'
          f'2)Никак не реагировать\n'))
    if number == 1:
        i = randint(-45, -10)
        edit_res(player.population, i)
    elif number == 2:
        edit_res(player.territory, -30)
    else:
        print('Try again') and nature_event(player)


def conflict(player):
    number = int(input(f'На границе вашего государства возникает конфликт с соседями. Нужно решить, как реагировать: \n'
          f'1)Попытаться разрешить ситуацию мирным путем\n'
          f'2)Применить силу\n'))
    if number == 1:
        edit_res(player.population, 0)
    elif number == 2:
        i = randint(-20, 0)
        m = randint(0, 50)
        edit_res(player.population, i) and edit_res(player.territory, m)
    else:
        print('Try again') and conflict(player)


def reform(player):
    number = int(input(f'Один из ваших министров предлагает провести реформы, на их проведение затребуется 20 единиц ресурсов. Рассмотрите предложение и решите, стоит ли его принимать. \n'
          f'1)Рискуем\n'
          f'2)Они того не стоят\n'))
    if number == 1:
        print('Реформы оказались удачными:\n Коэфициент роста популяции увеличен')
        i = randint(1, 5)
        edit_res(player.science_and_technology, i) and edit_res(player.resources, -20)
    elif number == 2:
        edit_res(player.population, 0)
    else:
        print('Try again') and reform(player)


def science(player):
    print(f'В вашем государстве происходит научное открытие. \n')
    i = randint(1, 5)
    edit_res(player.science_and_technology, i)


def popul(player):
    number = int(input(f'Приток беженцев из соседнего государства в связи с военными действиями на его территории. Примите решение \n'
          f'1)Впускаем всех\n'
          f'2)Закрываем границы\n'))
    if number == 1:
        i = randint(-20, -10)
        edit_res(player.resourses, i) and edit_res(player.population, 50)
    elif number == 2:
        edit_res(player.population, 0)
    else:
        print('Try again') and popul(player)


def medicine(player):
    number = int(input(f' Ваше государство сталкивается с проблемой нехватки медикаментов. Решите, как действовать:\n'
          f'1)Ввести нормирование медикаментов\n'
          f'2)Начать разработку новой технологии производства\n'))
    if number == 1:
        i = randint(-40, -10)
        edit_res(player.population, i)
    elif number == 2:
        edit_res(player.science_and_technology, 2) and edit_res(player.resources, -10)
    else:
        print('Try again') and medicine(player)


def medicine(player):
    number = int(input(f' Ваше государство сталкивается с проблемой нехватки медикаментов. Решите, как действовать:\n'
          f'1)Ввести нормирование медикаментов\n'
          f'2)Начать разработку новой технологии производства\n'))
    if number == 1:
        i = randint(-40, -10)
        edit_res(player.population, i)
    elif number == 2:
        edit_res(player.science_and_technology, 2) and edit_res(player.resources, -10)
    else:
        print('Try again') and medicine(player)

events = {
        1: [burn_place],
        2: [nature_event],
        3: [conflict],
        4: [reform],
        5: [science],
        6: [popul],
        7: [medicine],
        8: [burn_place],
        9: [burn_place],
        10: [burn_place],
        11: [burn_place],
        12: [burn_place],
        13: [burn_place],
        14: [burn_place]
    }