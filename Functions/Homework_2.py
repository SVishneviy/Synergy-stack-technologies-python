import collections

def create():
    last = 0
    if len(pets) > 0:
        last = collections.deque(pets, maxlen=1)[0]
    name = input("Введите кличку: ")
    animal = input("Введите вид животного: ")
    age = min(int(input("Введите возвраст: ")), 100)
    owner = input("Введите имя владельца: ")
    pets[last+1] = {name: {'animal': animal, 'age': abs(age), 'owner': owner}}
    
def read():
    id = int(input("Введите id питомца: "))
    pet_name = get_pet(abs(id))
    if pet_name:
        pet_v = pets[id].get(pet_name)
        print(f"Это {pet_v['animal']} по кличке \"{pet_name}\". "
            f"Возраст животного: {pet_v['age']} {get_declination(pet_v['age'])}. "
            f"Имя владельца: {pet_v['owner']}")
    else:
        print(f"Питомца с id - {id} не найдено")

def update():
    id = int(input("Введите id питомца: "))
    pet_name = get_pet(abs(id))
    if pet_name:
        print("--- Редактирование ---")
        print("1. name")
        print("2. age")
        print("3. owner")
        print("4. stop")
        print("-----------------------")
        while True:
            pet_v = pets[id].get(pet_name)
            cmd = input("Введите команду: ").lower()
            if cmd == "name":
                name_new = input("Введите новое имя: ")
                pet = pets.get(id)
                pet[name_new] = pet.pop(pet_name)
                pet_name = name_new
            elif cmd == "age":
                pet_v['age'] = abs(int(input("Введите новый возраст: ")))
            elif cmd == "owner":
                pet_v['owner'] = input("Введите новый владельца: ")
            elif cmd == "stop":
                break
            else:
                print("Команда введена некорректно")                
    else:
        print(f"Питомца с id - {id} не найдено")
        
def delete():
    id = int(input("Введите id питомца: "))
    if id in pets.keys():
        pets.pop(id)
        print(pets)
    else:
        print(f"Питомца с id - {id} не найдено")
    
def get_pet(id):
    if id in pets.keys():
        for k in pets.get(id):
            return k
    return False

def print_list():
    for id, info in pets.items():
        for k in info:
            print(k, info[k])

def get_declination(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age in [2, 3, 4] and not (age in [12, 13, 14]):
        return "года"
    else:
        return "лет"
    
pets = dict()
print("--- Команды ---")
print("1. create")
print("2. read")
print("3. update")
print("4. delete")
print("5. print")
print("6. stop")
print("---------------")
while True:
    cmd = input("Введтите команду: ").lower()
    if cmd == "create":
        create()
    elif cmd == "read":
        read()
    elif cmd == "update":
        update()
    elif cmd == "delete":
        delete()
    elif cmd == "print":
        print_list()
    elif cmd == "stop":
        break
    else:
        print("Команда введена некорректно")
    