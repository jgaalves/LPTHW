#crie um mapeamento entre estados e siglas
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California:': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#crie um conjunto básico de estados e algumas cidades deles
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

#adicione mais algumas cidades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#imprima algumas cidades
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#imprima alguns estados
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#faça isso usando o dic state e depois o cities
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#imprima todas as siglas dos estados
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#imprima cada cidade no estado
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#agora faça ambos ao mesmo tempo
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has cities {cities[abbrev]}")

print('-' * 10)
#com segurança, obtenha uma sigla de um estado que pode não estar ali
state = states.get('Texas')

if not state:
    print("Sorry, no  Texas")

#obtenha uma cidade com um valor padrão
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")