import math
a = float(input("A "))
b = float(input("B "))
c = float(input("C "))
D = b * b - 4 * a * c
if D < 0:
    print("Корней нет")
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print(x1, x2)
if D == 0:
    x = (-b + math.sqrt(D))/(2*a)
    print(x)
