i = 0
numbers = []

#while i < 6:
#    print(f"At the top i is {i}")
#    numbers.append(i)
#
#    i = i +1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")
def while_loop(start, end):
    numbers = []
    while start < end:
        start += 1
        numbers.append(start)
    return numbers

make_numbers = while_loop(0, 37)
print(f"The numbers: {make_numbers}")

#for num in numbers:
#    print(num)