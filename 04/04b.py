import re

def winning_contains(num):
    for number in winning:
        if number == num:
            return True
    return False


with open('input.txt') as file:
    total_cards = sum(1 for line in file)

copies = {i: 1 for i in range(1, total_cards + 1)}

with open('input.txt') as file:
    for i, card in enumerate(file):
        parts = re.sub(r'Card\s+\d+:', '', card).strip().split('|')
        winning = [int(num) for num in re.findall(r'\d+', parts[0])]
        mine = [int(num) for num in re.findall(r'\d+', parts[1])]
        card_points = 0
        for num in mine:
            if winning_contains(num):
                card_points += 1

        # distribute points as copies of next cards
        # print(f"Card: {i + 1}, Points: {card_points}")
        for n in range(card_points):
            copies[i+n+2] += copies[i + 1]


total_cards = sum(copies.values())
print(total_cards)







