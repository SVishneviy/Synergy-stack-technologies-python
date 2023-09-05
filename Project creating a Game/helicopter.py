import os
from utils import randcell

class Helicopter:
    def __init__(self, width, height):
        rc = randcell(width, height)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.width = width
        self.height = height
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lifes = 20
    
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.height and ny < self.width):
            self.x, self.y = nx, ny
            
    def print_stats(self):
        print(f"🪣  {self.tank}/{self.mxtank}", sep="", end=" | ")
        print(f"🏆 {self.score}", end=" | ")
        print(f"❤️  {self.lifes}")
        
    def game_over(self):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("                                        ")
        print(f"       GAME OVER, YOUR SCORE IS {self.score}")
        print("                                        ")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)
        
    def export_data(self):
        return {"score": self.score,
                "lifes": self.lifes,
                "x": self.x, "y": self.y,
                "tank": self.tank,
                "mxtank": self.mxtank}
    
    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lifes = data["lifes"] or 20
        self.score = data["score"] or 0