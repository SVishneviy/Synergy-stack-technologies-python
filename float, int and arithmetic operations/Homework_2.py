print("Введите число:")
num = int(input())
calc = ((((num % 100) // 10) ** (num % 10)) * ((num % 1000) // 100)) / (((num % 100000) // 10000) - ((num % 10000) // 1000)) 
print(calc)