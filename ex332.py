i = 0
numbers = []

def while_loop(start, end):
    numbers = []
    while start < end:
        start += 1
        numbers.append(start)
    return numbers

make_numbers = while_loop(1, 70)

print(make_numbers)    
