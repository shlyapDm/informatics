import math

def task1():
    """Даны произвольные х, у, z. Нужно вычислить a и b по формулам:
    a= (ln|x-1| - y**(1/3)) / (x**(1/3) + |y|**(1/2) * ln(x+3))
    b= (1+x**2)**(1/5) + sin(z) * cos(x)"""

    while True:
        x=float(input("Введите x: "))
        if x+3<=0:
            print("Ошибка: логарифм х+3 должен быть больше 0")
            continue
        break

    y=float(input("Введите y: "))
    z=float(input("Введите z: "))

    a=(math.log(abs(x-1)) - y**(1./3)) / (x**(1./3) + math.sqrt(abs(y)) * math.log(x+3))
    b=(math.sqrt(1 + x**2))**1./5 + math.sin(z) * math.cos(x)
    
    print(f"Значение a в формате .4f: {a:.4f}")
    print(f"Значение b в формате .4f: {b:.4f}")
    

def task2():
    """Нужно вычислить значение функции ф(х) по форумле:
    f(x)= ((b*x + a)**2) / (c + x**3) + x**3
    где a= −1; b= 4; c= 3"""
    try:
        x=float(input("Введите x: "))
        a, b, c = -1, 4, 3

        f=((b*x + a)**2) / (c + x**3) + x**3

        print(f"Значение в формате .4f: f(x) = {f:.4f}")

    except Exception as e:
        print("Ошибка:", e)


def task3():
    """Нужно вычислить значение функции ф(х) по формуле:
    f(x) = ch**2*(sh(1 / x**2))"""
    try:
        x= float(input("Введите x: "))
        if x==0:
            raise ValueError("x не может быть равен 0")

        f=math.cosh(math.sinh(1 / x**2)) ** 2

        print(f"Значение в формате .4f: f(x) = {f:.4f}")

    except Exception as e:
        print("Ошибка:", e)


def task5():
    """Конькобежец массой M(кг), стоя на коньках на льду, бросает в горизонтальном направлении
    камень массой m(кг) со скоростью V(м/с) относительно льда, коэф. тренеия = mu
    Надо найти на какое рассотяние S откатьится при этом конькобежец"""
    while True:
        M= float(input("Введите массу конькобежца M(кг): "))
        if M<=0:
            print("Ошибка: масса должна быть больше 0")
            continue
        break

    while True:
        m= float(input("Введите массу камня m(кг): "))
        if m<=0:
            print("Ошибка: масса должна быть больше 0")
            continue
        break

    while True:
        V= float(input("Введите скорость броска V(м/с): "))
        if V<=0:
            print("Ошибка: скорость должна быть больше 0")
            continue
        break

    while True:
        mu= float(input("Введите коэффициент трения mu: "))
        if mu<=0:
            print("Ошибка: коэф. тренеия должна быть больше 0")
            continue
        break

    g= 9.81
    V= m*V / M
    S= V**2 / (2*mu*g)

    print(f"Расстояние отката в формате .4f: S = {S:.4f}(м)")


def task8():
    """Надо найти потенциальную энергию стрелы через время t(с), у которой масса m(г),
    выпущенна вертикально вверх со скоростью V(м/с)"""
    while True:
        m= float(input("Введите массу стрелы m(г): "))
        if m<=0:
            print("Ошибка: масса должна быть больше 0")
            continue
        break

    while True:
        V= float(input("Введите скорость V(м/с): "))
        if V<=0:
            print("Ошибка: скорость должна быть больше 0")
            continue
        break

    while True:
        t= float(input("Введите время(с): "))
        if t<=0:
            print("Ошибка: время должно быть больше 0")
            continue
        break

    g= 9.8066
    m_kg= m / 1000
    h=V*t - 0.5*(g*t**2)  #нахождение высоты
    Ep= m_kg*g*h
    print(f"Потенциальная энергия в формате .4f: Ep = {Ep:.4f} Дж")
