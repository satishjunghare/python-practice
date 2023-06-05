import config
import configChild
from classObject import Car

print(config.name)

car = Car("Nissan Magniet", "Nissan")
car.start()
car.stop()
print(car.getDetails())