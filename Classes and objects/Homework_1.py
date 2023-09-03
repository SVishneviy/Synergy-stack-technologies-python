class Cashbox:
    
    def __init__(self, cash):
        self.cash = cash
    
    def top_up(self, x):
        self.cash += x
        
    def count_1000(self):
        print(self.cash // 1000)
    
    def take_away(self, x):
        if x < self.cash:
            self.cash -= x
        else:
            print("Не достаточно денег")
            
cashbox = Cashbox(500)

print("--- Команды ---")
print("1. Пополнить")
print("2. Целые тысячи")
print("3. Забрать деньги")
print("4. Остаток в кассе")
print("5. Выход")
print("---------------")

while True:
    command = int(input("Введите № команды: "))
    match abs(command):
        case 1:
            x = int(input("Введите на сколько пополнить: "))
            cashbox.top_up(abs(x))
        case 2:
            cashbox.count_1000()
        case 3:
            x = int(input("Введите сколько забрать:"))
            cashbox.take_away(abs(x))
        case 4:
            print(f"Остаток: {cashbox.cash}")
        case 5:
            break
        case _:
            print("Команда не найдена")