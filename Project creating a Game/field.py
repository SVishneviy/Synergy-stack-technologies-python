from utils import randbool
from utils import randcell
from utils import randcell2

CELL_TYPES = "🟩🌲🟦🏥🏨🔥"
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 1000
class Field:
    
    def __init__(self, width, height, clouds, helicopter):
        self.width = width
        self.height = height
        self.clouds = clouds
        self.helicopter = helicopter
        self.cells = [[0 for i in range(width)] for j in range(height)]
        self.generate_forest(5, 10)
        rivers = width // 10
        while (rivers > 0):
            self.generate_river(height)
            rivers -= 1
        self.generate_upgrade_shop()
        self.generate_hospital()
        
    def update_fires(self):
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        list_fires = []
        for ri in range(self.height):
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    list_fires.append((ri, ci))
                    if(self.helicopter.score != 0):
                        self.helicopter.score -= TREE_BONUS
        for i in range(len(list_fires)):
            for j in range(len(moves)):
                ry2, rx2 = list_fires[i][0] + moves[j][0], list_fires[i][1] + moves[j][1]
                if(self.check_bounds(ry2, rx2) and self.cells[ry2][rx2] == 1):
                    self.cells[ry2][rx2] = 5
                    break
        for i in range(self.height // 2):
            self.add_fire()                
        
    def add_fire(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 1):
            self.cells[cx][cy] = 5
        
    def generate_river(self, l):
        rc = randcell(self.width, self.height)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
        
    def generate_forest(self, r, mxr):
        for ri in range(self.height):
            for ci in range(self.width):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
                    
    def generate_tree(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
    
    def generate_upgrade_shop(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4
        
    def generate_hospital(self):
        c = randcell(self.width, self.height)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()
        
    def print_field(self):
        print("⬛" * (self.width + 2))
        for ri in range(self.height):
            print("⬛", end="")
            for ci in range(self.width):
                cell = self.cells[ri][ci]
                if (self.clouds.cells[ri][ci] == 1):
                    print("☁️ ", end="")
                elif (self.clouds.cells[ri][ci] == 2):
                    print("🌩️ ", end="")                    
                elif (self.helicopter.x == ri and self.helicopter.y == ci):
                    print("🚁", end="")
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.width + 2))
    
    def print_cost(self):
        print(f"🪣  {UPGRADE_COST}💲", sep="", end=" | ")
        print(f"❤️  {LIFE_COST}💲")
              
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.height or y >= self.width):
            return False
        return True
    
    def process_helicoplter(self):
        helicopter = self.helicopter
        cell = self.cells[helicopter.x][helicopter.y]
        if (cell == 2):
            helicopter.tank = helicopter.mxtank
        if (cell == 5 and helicopter.tank > 0):
            helicopter.tank -= 1
            helicopter.score += TREE_BONUS
            self.cells[helicopter.x][helicopter.y] = 1
        if (cell == 4 and helicopter.score >= UPGRADE_COST):
            helicopter.mxtank += 1
            helicopter.score -= UPGRADE_COST
        if (cell == 3 and helicopter.score >= LIFE_COST):
            helicopter.lifes += 10
            helicopter.score -= LIFE_COST
        if (self.clouds.cells[helicopter.x][helicopter.y] == 2):
            helicopter.lifes -= 1
            if (helicopter.lifes == 0):
                helicopter.game_over()
                
    def export_data(self):
        return {"cells": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.width)] for j in range(self.height)]