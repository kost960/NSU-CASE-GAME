from random import randint

def usec(player):
    player.resources += randint(1, 5) * randint(1, 5)
    player.territory -= 100

def bear(player):
    player.resources += randint(1, 5) * randint(1, 5)
    player.territory += 100

events = {
        1: ['я юсек', usec],
        2: ['я бир', bear]
    }