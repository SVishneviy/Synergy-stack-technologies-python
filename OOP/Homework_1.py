class Transport:
   
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def print_attr(self):
        print(f"Название автомобиля: {self.name} " 
              f"Скорость: {self.max_speed} "
              f"Пробег: {self.mileage}")
        
autobus = Transport("Renault Logan", 180, 12)
autobus.print_attr()