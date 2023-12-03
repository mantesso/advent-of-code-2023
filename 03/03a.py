arr = []

with open('input.txt') as file:
    for line in file:
        arr.append(list(line.strip()))

rows = len(arr)
cols = len(arr[0])

def check_adjacent(x1, y1, x2, y2):
    for y in range(y1 - 1, y2 + 2):
        if 0 <= y < rows:  # Check for out-of-bounds
            if x1 - 1 >= 0:  # Left edge
                if arr[y][x1 - 1] != '.':
                    return True
            if x2 + 1 < cols:  # Right edge
                if arr[y][x2 + 1] != '.':
                    return True

    for x in range(x1, x2 + 1):
        if y1 - 1 >= 0:  # Top edge
            if arr[y1 - 1][x] != '.':
                return True
        if y2 + 1 < rows:  # Bottom edge
            if arr[y2 + 1][x] != '.':
                return True
    return False

total_sum = 0
for y in range(rows):
    x1 = None
    x2 = None
    for x in range(cols):
        if arr[y][x].isnumeric():
            if x1 is None:
                x1 = x
            x2 = x 
        elif x1 is not None:
            # Process the number as soon as a non-numeric character is encountered
            if check_adjacent(x1, y, x2, y):
                number = ""
                for n in range(x1, x2 + 1):
                    number += arr[y][n]
                total_sum += int(number)
            x1 = None
            x2 = None

    # Check if the last character in a row is a part of a number
    if x1 is not None and check_adjacent(x1, y, x2, y):
        number = ""
        for n in range(x1, x2 + 1):
            number += arr[y][n]
        total_sum += int(number)

print(total_sum)

