res = list(map(int, input("Введите числа через пробел:\n").split()))
temp = set()
for i in res:
    print(f"{i} - YES") if i in temp else print(f"{i} - NO")
    temp.add(i)
        
        