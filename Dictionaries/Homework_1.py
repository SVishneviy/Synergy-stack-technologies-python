def declination(n):
    if pet['age'] % 10 == 1 and pet['age'] % 100 != 11:
        return "год"
    elif pet['age'] in [2, 3, 4] and not (pet['age'] in [12, 13, 14]):
        return "года"
    else:
        return "лет"

pets = dict()
n = int(input("Сколько животных добавить: "))
for i in range(n): 
    name = input("Введите кличку: ")
    animal = input("Введите вид животного: ")
    age = min(int(input("Введите возвраст: ")), 100)
    owner = input("Введите имя владельца: ")
    pets[name] = {'animal': animal, 'age': abs(age), 'owner': owner}
for k in pets.keys():
    pet = pets.get(k)
    print(f"Это {pet['animal']} по кличке \"{k}\". "
          f"Возраст животного: {pet['age']} {declination(pet['age'])}. "
          f"Имя владельца: {pet['owner']}")
