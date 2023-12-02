import re

MAX_VALUES = {'red': 12, 'green': 13, 'blue': 14}
sum_of_ids = 0

def valid_draw(draw):
    for cube in draw.split(','):
        n, color = cube.split()
        if int(n) > MAX_VALUES[color]:
            return False
    return True

with open('input.txt') as file:
    for id, game in enumerate(file):
        game = re.sub(r'Game \d+: ', '', game).strip()
        draws = game.split('; ')
        if all(valid_draw(draw) for draw in draws):
            sum_of_ids += (id + 1)

print(sum_of_ids)