cars = 100 #define a quantidade de carros
space_in_a_car = 4 #define quanto de espaço tem em cada carro
drivers = 30 #informa o numero de motoristas
passengers = 90 #informa o numero de passageiros
cars_not_driven = cars - drivers #calcula qual a quantidade de carros sem motoristas
cars_driven = drivers #informa que a quantidade de carros dirigidos é a mesma de motoristas
carpool_capacity = cars_driven * space_in_a_car # informa a capacidade de carona em cada carro
average_passengers_per_car = passengers / cars_driven #informa a média de passageiros por carro


print("There are" , cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have ", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")