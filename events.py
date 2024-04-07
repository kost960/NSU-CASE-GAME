from random import randint


def edit_res(resourse, quantity):
    resourse += quantity
    if quantity > 0:
        if resourse ==
def burn_place(player):
    number = int(input(f'Ваше государство обнаруживает новое месторождение ценного ресурса. Решите, как лучше использовать эту находку: \n'
          f'1)На развитие науки и технологий\n'
          f'2)Увеличить военное преимущества\n'
          f'3)Сохранить для возможного использования в будущем'))
    if number == 1:
        i = randint(3, 8)
        edit_res(player.science_and_technology, i)
    elif number == 2:
        i = randint(1, 3)
        edit_res(player.military_power, i)
    else:
        edit_res(player.military_power, 100)


def nature_event(player):
    number = int(input(f'В вашем государстве происходит природная катастрофа. Необходимо быстро принять решение о том, как справиться с последствиями: \n'
          f'1)Отправить часть населения на пораженные зоны\n'
          f'2)Никак не реагировать\n'))
    if number == 1:
        i = randint(-15, 0)
        edit_res(player.population, i)
    else:
        edit_res(player.territory, -30)



events = {
        1: ['я юсек', usec],
        2: ['я бир', bear]
    }