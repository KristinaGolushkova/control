import math

a = int(input("введите а: "))
b = int(input("введите b: "))
c = int(input("введите c: "))

D = b ** 2 - 4 * a * c
print("дискриминант равен", +int(D))

if D < 0:
    print("Корней нет")

elif D == 0:
    x = -b / 2 * a
    print(x)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1)
    print(x2)
