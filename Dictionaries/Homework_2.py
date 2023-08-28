start, end = map(int, (input("Введите начальный и конечный элементы через пробел: ").split()))
res = []
if start < end:
    res = list(int(x) for x in range(start, end+1))
else:
    res = list(int(x) for x in range(end, start+1))
    res.reverse()
temp = dict()
for i in res:
    temp[i] = i ** i
    print(f"{i} : {temp[i]}")