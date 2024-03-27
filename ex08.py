formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Colocando",
    "Meu proprio texto",
    "Talvez um poema",
    "Nah, sou ruim de poema"
))