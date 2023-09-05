import os
import time
import json
from pynput import keyboard
from field import Field
from clouds import Clouds
from helicopter import Helicopter

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 200
CLOUDS_UPDATE = 150 

FIELD_WIDTH, FIELD_HEIGHT = 20, 10

clouds = Clouds(FIELD_WIDTH, FIELD_HEIGHT)
helicopter = Helicopter(FIELD_WIDTH, FIELD_HEIGHT)
field = Field(FIELD_WIDTH, FIELD_HEIGHT, clouds, helicopter)
tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def process_key(key):
    global tick, field, clouds, helicopter
    c = key.char.lower()
    # Обработка движений вертолета
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helicopter.move(dx, dy)
    # Сохранение игры
    elif c == 'f':
        data = {"helicopter": helicopter.export_data(), 
                "clouds": clouds.export_data(), 
                "field": field.export_data(),
                "tick": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    # Восстановление игры
    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helicopter.import_data(data["helicopter"])
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])
            
        
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()

while True:
    os.system("cls")
    field.process_helicoplter()
    helicopter.print_stats()
    field.print_cost()
    field.print_field()
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()