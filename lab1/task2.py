from math import cos, log, sin, e, sqrt

x=float(input("Введите значение переменной х: "))
y=float(input("Введите значение переменной y: "))
z=float(input("Введите значение переменной z: "))

a=sqrt(x**3/2) - sin(y)
b=(e**2/3) - cos(y) + z + log(y)

print(f"Получено значение функции a={a}")
print(f"Получено значение функции b={b}")
