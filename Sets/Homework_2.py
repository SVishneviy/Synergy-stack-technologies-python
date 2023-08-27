res1 = list(map(int, input("Введите числа через пробел:\n").split()))[:100000]
res2 = list(map(int, input("Введите числа через пробел:\n").split()))[:100000]
print(f"res1 = {res1}\nres2 = {res2}")
print(len(set(res1).union(res2)))