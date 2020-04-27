#Declaracion de variables
#Variable carros
cars = 4
#Variable en el carro
space_in_a_car = 4
#Conductores
drivers = 30
#Pasajeros
passengers = 90
#Variable carros que no se manejan
cars_not_driven = cars - drivers
#Variable carros que se manejan
cars_driven = drivers
#Varible de capacidad compartidas
carpool_capacity = cars_driven * space_in_a_car
#Personas en el carro
average_passengers_per_car = passengers / cars_driven

print ("there are", cars, "cars avaible")
print ("There are only", drivers , "drivers avaible")
print ("There will be ", cars_not_driven , "empty cars today")
print ("we can transpor " , carpool_capacity , "people today")
print ("we have", passengers, "to carpool today")
print ("we need to put about" , average_passengers_per_car , "in each car.")
