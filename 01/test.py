import re
numbers = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9 
}

pattern = r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))'
s = "eighthree6"
matches = re.finditer(pattern, s)
results = [numbers[match.group(1)] for match in matches]

print(f'{results[0]}{results[-1]}')
      

