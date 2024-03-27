the_count = [1, 2, 3, 4, 5,]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#esse primeiro tipo de loop for percorre uma lista
for number in the_count:
    print(f"This is count {number}")

#mesma coisa que o codigo acima
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#também podemos percorrer listas mistas
#perceba que temos que usar um {} uma vez que não sabemos o que há nela 
for i in change:
    print(f"I got {i}")

#também podemos construir  listas, primeiro comece com uma vazia
elements = []

#então use a fução range para fazer a contagem de 0 a 5
for n in range(0, 6):
    print(f"Adding {n} to the list.")
    # append é uma função que as listas entendem
    elements.append(n)

#agora podemos imprimi-la também
for n in elements:
    print(f"Element was: {n}")