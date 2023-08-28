class Transport:
   
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def print_attr(self):
        print(f"Название автомобиля: {self.name} " 
              f"Скорость: {self.max_speed} "
              f"Пробег: {self.mileage}")
        
class Autobus(Transport):
    pass

auto = Autobus("Renault Logan", 180, 12)
auto.print_attr()