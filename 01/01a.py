total = 0

with open('input.txt') as file:
    for word in file:
        first, last = None, None
        for char in word.strip():
            if char.isnumeric() and first is None:
                first = char
            elif char.isnumeric() and first != None:
                last = char
        
        if (last == None):
            total += int(first + first)
        else:
            total += int(first + last)
        
        
print(total)