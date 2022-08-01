from prueba import Car
from prueba import Payment

car_1= Car("BMW","Serie 3","2022","Blanco")
pago = Payment("Credit")

print(car_1.make)
print(car_1.model)
print(car_1.color)
car_1.drive()
car_1.stop()

pago.decifrar()
