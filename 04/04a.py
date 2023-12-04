import re

total_points = 0

def winning_contains(num):
    for number in winning:
        if number == num:
            return True
    return False

with open('input.txt') as file:
    for card in file:
        parts = re.sub(r'Card\s+\d+:', '', card).strip().split('|')
        winning = [int(num) for num in re.findall(r'\d+', parts[0])]
        mine = [int(num) for num in re.findall(r'\d+', parts[1])]
        card_points = 0
        for num in mine:
            if winning_contains(num) and card_points == 0:
                card_points = 1
            elif winning_contains(num):
                card_points *= 2
        total_points += card_points


print(total_points)



