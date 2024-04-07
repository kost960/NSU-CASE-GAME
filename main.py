from random import randint
from events import events
from player_actions import actions

def grow_population(players):
    for player_number, player in players:
        player.set_population(player.population * player.grow_population)

def players():
    players_count = int(input('Введите количество игроков: '))
    players = {}
    for i in range(players_count):
        p = Player()
        players[i + 1] = p

    player_number = 1
    while len(players) > 1:
        player = players.get(player_number, 'не найдено')
        if player == 'не найдено':
            player_number += 1
            if player_number > players_count:
                player_number = 1
            continue

        if player.territory <= 0 or player.population <= 0:
            players.pop(player_number)
            players_count -= 1
            player_number += 1

            if player_number > players_count:
                player_number = 1
            continue

        if player_number == 1:
            grow_population(players)

        print(f'Ход игрока с номером {player_number}')
        menu(player)
        player_number += 1


class Player:
    population = 100
    military_power = 1 #max 15
    science_and_technology = 1 #max 30
    resources = 50
    territory = 100
    economy = (population / 1000) + (territory / 1000) + (science_and_technology / 30)
    grow_population = 1.3
    def stats(self):
        return (f"""Население вашего государства: {self.population}
Ваша экономика: {self.economy}
Военная мощь государства: {self.military_power}
Наука и технологии: {self.science_and_technology}
Ваши ресурсы: {self.resources}
Ваши территории: {self.territory}""")
    def set_population(self, new_population):
        past_population = self.population
        self.population = new_population
        if new_population < 0:
            self.population = 0

        difference = past_population - new_population
        if difference > 0:
            print(f'Численность населения увеличина на {difference}\n')
        elif difference < 0:
            print(f'Численность населения уменьшена на {abs(difference)}\n')
        else:
            print(f'Численность населения не изменилось\n')
def get_player_choice():
    print(f"""
            Меню:
            0) Статистика
            1) Посадить зерно
            """)
    n = input("Введите число: ")
    return n


def menu(player):
    n = get_player_choice()
    while actions.get(n, 'не найдено') == 'не найдено':
        print('Вы ввели неправильно, попробуйте ещё раз')
        n = get_player_choice()

    while n == '0':
        action = actions.get(n, 'не найдено')
        action(player)
        n = get_player_choice()

    action = actions.get(n, 'не найдено')
    action(player)

    event_number = randint(0, len(events))
    if event_number == 0:
        print('Никаких событий не произошло')
        player.population = player.population*player.grow_population
        return
    event = events.get(event_number)
    event(player)

players()
