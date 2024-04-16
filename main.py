# Case-study Game
# Developers: Maltsev A., Kolchik K.
#

from random import randint
from events import events
from player_actions import actions
import ru_local as ru


def grow_population(players):
    '''
    Function responsible for population growth.
    '''
    for player_number, player in players.items():
        print(f'{ru.DEF_GROW_POPULATION1} {player_number} {ru.DEF_GROW_POPULATION2}')
        player.set_population(player.population * player.grow_population)

def players():
    '''
    Function responsible for move transition.
    '''
    players_count = int(input(f'{ru.PLAYER_NUMBER}'))
    players = {}
    winner = 0
    for i in range(players_count):
        p = Player()
        players[i + 1] = p

    player_number = 1
    while len(players) > 1:
        player = players.get(player_number, 'not found')
        if player == 'not found':
            player_number += 1
            if player_number > players_count:
                player_number = 1
            continue

        if player.territory == 0 or player.population == 0:
            players.pop(player_number)
            players_count -= 1
            player_number += 1

            if player_number > players_count:
                player_number = 1
            continue

        if player_number == 1:
            grow_population(players)

        print(f'{ru.PLAYERS_MOVE}{player_number}')
        menu(player)
        player_number += 1

        if player.economy >= 3:
            winner = player_number
            print(f'{ru.WINNER} {winner}')
            print(f'{ru.ECONOMY_WINNER}')
            break

    if len(players) == 1:
        print(f'{ru.WINNER} {list(players.keys())[0]}')

class Player:
    population = 100
    military_power = 1  # max 15
    science_and_technology = 1  # max 30
    resources = 50
    territory = 100
    economy = (population / 1000) + (territory / 1000) + (science_and_technology / 30)
    grow_population = 1.3

    def stats(self):
        return (f"""
{ru.YOUR_POPULATION}{self.population}
{ru.YOUR_ECONOMY}{self.economy}
{ru.YOUR_MILITARY_POWER}{self.military_power}
{ru.YOUR_SCIENCE}{self.science_and_technology}
{ru.YOUR_RESOURCES}{self.resources}
{ru.YOUR_TERRITORY}{self.territory}""")

    '''
    Below are the methods responsible for checking and reflecting changes in characteristics.
    '''

    def set_population(self, new_population):
        past_population = self.population
        self.population = new_population
        if new_population < 0:
            self.population = 0

        difference = new_population - past_population
        if difference > 0:
            print(f'{ru.GROW_POPULATION} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_POPULATION} {abs(difference)}\n')

    def set_military_power(self, new_military_power):
        past_military_power = self.military_power
        self.military_power = new_military_power
        if new_military_power < 0:
            self.military_power = 0

        difference = new_military_power - past_military_power
        if difference > 0:
            print(f'{ru.GROW_MILITARY} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_MILITARY} {abs(difference)}\n')

    def set_science_and_technology(self, new_science_and_technology):
        past_science_and_technology = self.science_and_technology
        self.science_and_technology = new_science_and_technology
        if new_science_and_technology < 0:
            self.science_and_technology = 0

        difference = new_science_and_technology - past_science_and_technology
        if difference > 0:
            print(f'{ru.GROW_SCIENCE} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_SCIENCE} {abs(difference)}\n')

    def set_resources(self, new_resources):
        past_resources = self.resources
        self.resources = new_resources
        if new_resources < 0:
            self.resources = 0

        difference = new_resources - past_resources
        if difference > 0:
            print(f'{ru.GROW_RESOURCES} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_RESOURCES} {abs(difference)}\n')

    def set_territory(self, new_territory):
        past_territory = self.territory
        self.territory = new_territory
        if new_territory < 0:
            self.territory = 0

        difference = new_territory - past_territory
        if difference > 0:
            print(f'{ru.GROW_TERRITORY} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_TERRITORY} {abs(difference)}\n')

    def set_economy(self, new_economy):
        past_economy = self.economy
        self.economy = new_economy
        if new_economy < 0:
            self.territory = 0

        difference = new_economy - past_economy
        if difference > 0:
            print(f'{ru.GROW_ECONOMY} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_ECONOMY} {abs(difference)}\n')

    def set_grow_population(self, new_grow_population):
        past_grow_population = self.grow_population
        self.grow_population = new_grow_population

        difference = new_grow_population - past_grow_population
        if difference > 0:
            print(f'{ru.GROW_SET_POPULATION} {difference}\n')
        elif difference < 0:
            print(f'{ru.DECLINE_SET_POPULATION} {abs(difference)}\n')


def get_player_choice():
    '''
    Function responsible for selecting a player in the menu.
    '''
    print(f'{ru.MENU}')
    n = input(f"{ru.NUMBER}")
    return n


def menu(player):
    '''
    The function responsible for choosing an action and choosing a solution in a random event.
    '''
    chosen = False
    while not chosen:
        n = get_player_choice()
        while actions.get(n, 'not found') == 'not found':
            print(f'{ru.TRY_AGAIN}')
            n = get_player_choice()

        while n == '0':
            action = actions.get(n, 'not found')
            action(player)
            n = get_player_choice()

        action = actions.get(n, 'not found')
        chosen = action(player)

    event_number = randint(0, len(events))
    if event_number == 0:
        print(f'{ru.NO_EVENTS}')
        player.population = player.population * player.grow_population
        return
    event = events.get(event_number)
    event(player)


players()
