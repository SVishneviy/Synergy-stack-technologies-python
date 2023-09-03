import random

class Turtle:
    
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        
    def go_up(self):
        self.y += self.s
        
    def go_down(self): 
        self.y -= self.s
        
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
        
    def evolve(self):
        self.s += 1
        
    def degrade(self):
        self.s -= 1
        if self.s <= 0:
            raise ValueError
        
    def count_moves(self, x2, y2):        
        count = 0
        first_x = True
        first_y = True
        while(self.x != x2 or self.y != y2):
            
            # Сначала идем по оси Y, если за один ход дойдем до Y2
            if (self.y - self.s == y2) or (self.y + self.s == y2):
                first_x = False
            # Сначала идем по оси X, если за один ход дойдем до X2
            elif (self.x - self.s == x2) or (self.x + self.s == x2):
                first_y = False
            # Уменьшаем шаг, если сможем сделать ход по оси Y
            # (Например, для случаев, когда X = 1, Y = 4, S = 4, а X2 = 10, Y2 = 1)
            if (((y2 - (self.y - (self.s - 1)) == 0) or (abs(y2 - (self.y + (self.s - 1)) == 0))) 
                and (self.s > 1) and first_y):
                first_x = False
                self.degrade()
            # Уменьшаем шаг, если сможем сделать ход по оси X
            # (Например, для случаев, когда X = 4, Y = 6, S = 4, а X2 = 1, Y2 = 1)
            elif ((((x2 - (self.x - (self.s - 1)) == 0)) or (abs(x2 - (self.x + (self.s - 1)) == 0))) 
                  and (self.s > 1) and first_x):
                first_y = False
                self.degrade()
            # Делаем ход, если можем сходить по оси Y
            elif ((self.y + self.s <= y2) or abs(self.y - self.s >= y2)) and (self.y != y2) and first_y:
                self.__action_y(y2)
                first_x = True
            # Делаем ход, если можем сходить по оси X
            elif ((self.x + self.s <= x2) or abs(self.x - self.s >= x2)) and (self.x != x2) and first_x:
                self.__action_x(x2)
                first_y = True
            # Иначе, уменьшаем шаг
            else:
                self.degrade()
            count += 1
            field[self.y-1][self.x-1] = f" {count}"          
        return count
        
    def __action_x(self, x2):
        # Прибавляем к шагу, если сможем сделать ход
        if (abs(x2 - (self.x + (self.s + 1))) % (self.s + 1)) == 0:
            self.evolve()
        else:
            if (self.x < x2):
                self.go_right()
            else:
                self.go_left()
          
    def __action_y(self, y2):
        # Прибавляем к шагу, если сможем сделать ход
        if (abs(y2 - (self.y + (self.s + 1))) % (self.s + 1)) == 0:
            self.evolve()
        else:
            if (self.y < y2):
                self.go_up()
            else:
                self.go_down()
                     
def random_cell(m, n):
    rx = random.randint(1, m)
    ry = random.randint(1, n)
    return (rx, ry)

def print_field():
    print("  ", end=" ")
    print(*range(1, m + 1), sep=" ")
    t = 0
    for row in field:
        t += 1
        print("{:2d}".format(t), end="")
        for cell in row:
            if cell == 0:
                print(simb[0], end= "")
            elif cell == "t":
                print(simb[1], end= "")
            else:
                print(cell, end= "")            
        print()
simb = ("🟨", "🐢")

m, n = map(int, input("Введите размер карты N x M: ").split())

field = [[0 for i in range(m)] for i in range(n)]

# Для тестирования
# rx, ry = map(int, input("Введите координаты X x Y: ").split())

rx, ry = random_cell(m, n)
s = abs(int(input("Введите S - начальный шаг за ход: ")))

turtle = Turtle(rx, ry, s)

field[ry-1][rx-1] = "t"
print_field()

x2, y2 = map(int, input("Введите координаты X2 x Y2: ").split()) 
count_moves = turtle.count_moves(x2, y2)

print_field()
print(f"Минимальное количество действий: {count_moves}")