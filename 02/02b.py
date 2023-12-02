import re

sum_of_power = 0
with open('input.txt') as file:
    for game in file:
        game = re.sub(r'Game \d+: ', '', game).replace(';', ',').strip()
        min = { 'red': 0, 'green': 0, 'blue': 0}
        for cube in game.split(', '):
            n, color = cube.split()
            if min[color] < int(n):
                min[color] = int(n)
        
        sum_of_power += min['red'] * min['green'] * min['blue']

print(sum_of_power)

