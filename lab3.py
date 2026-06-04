import sys
import matplotlib.pyplot as plt
import math

def input_data(msg: str, wanted_type: object = float):

    """-> Вспомогательная функция. Проверка на нужный формат
    msg - значение которое мы получаем от пользователя, тип строка
    wanted_type - тип, которая ожидает программа

    При вводе верного значения, возращает уже объект ожидаемого класса
    Если же перевести нельзя, поднимается исключение ValueError и выводиться сообщение
    Ctrl-C заканчивает программу полностью"""
    
    while True:
        try:
            return wanted_type(input(msg))
        except ValueError:
            print(f'Ошибка. Введите валидное значение, ожидается {wanted_type}')
        except KeyboardInterrupt:
            print("\nЗаканчиваю работу!")
            sys.exit(-1)

def integer_to_base(num: int, base) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # проверка
    if base > 35: raise Exception("Максимальная система счисления равна 35")
    if base > num: return str(num)
    itog = ""
    while num > 0:
        itog += digits[num%base]
        num //= base 
    return itog[::-1]

def fract_to_base(fract: int, base) -> str:
    # https://studfile.net/preview/8991849/page:4
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # проверка
    if base > 35: raise Exception("Максимальная система счисления равна 35")
    if base > fract: return str(fract)
    if fract == 0: return 0
    fract = float('0.'+str(fract))
    fract_ls = []
    for i in range(10):
        if fract>1: fract=fract-int(fract)
        fract*=base
        fract_ls.append(digits[int(fract)])
    fract = "".join(fract_ls)
    return fract


# на 3 балла
def task1():
    def check_prime(num) :
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
    # Проверяем нечетные делители от 3 до корня из n
    # Шаг 2 позволяет пропускать четные числа (3, 5, 7...)
        limit = int(num**0.5) + 1
        for i in range(3, limit, 2):
            if num % i == 0:
                return False
        return True
    def check_palindrom(num):
        return (str(num) == str(num)[::-1]) and len(str(num))==5
    while True:
        num = input_data("Введите число: ", int)
        print(f'Число простое? {"Да" if check_prime(num) else "Нет"}')
        print(f'Число пятизначный палиндром? {"Да" if check_palindrom(num) else "Нет"}')

# 2 балла        
def task2():
    def func_y(x):
        if x>=math.pi:
            return math.tan(x)+math.sin(x)
        else: 
            return x**2-math.pi**2

    x_num = input_data("x = ")
    print(f"f(x) = {func_y(x_num)}")
    
    print("Введите диапазон [a, b]")
    a = input_data("a = ", int)
    b = input_data("b = ", int)
    x_ls = [i for i in range(a, b, 1)]
    y_ls = [func_y(i) for i in x_ls]
    plt.plot(x_ls, y_ls)
    plt.grid(True)
    plt.show()


# 1 балл
def task5():
    a = input_data("Введите a: ", int)
    b = input_data("Введите b: ", int)
    c = input_data("Введите c: ", int)

    if (a > b and a < c) or (a > c and a < b):
        avg = a
    elif (b > a and b < c) or (b > c and b < a):
        avg = b
    else:
        avg = c

    print(f"Удвоено число: {avg}")
    print(f"Результат: {avg * 2}")
