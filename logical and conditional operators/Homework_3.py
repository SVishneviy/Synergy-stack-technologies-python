print("Введите сумму инвестиций")
investSum = int(input())
print("Введите сумму денег у Майка:")
cashMike = int(input())
print("Введите сумму денег у Ивана:")
cashIvan = int(input())

if (cashMike >= investSum) and (cashIvan < investSum):
    print("Mike")
elif (cashIvan >= investSum) and (cashMike < investSum):
    print("Ivan")
elif (cashMike >= investSum) and (cashIvan >= investSum):
    print(2)
elif (cashMike < investSum and cashIvan < investSum) and (cashMike + cashIvan >= investSum):
    print(1)
else:
    print(0)