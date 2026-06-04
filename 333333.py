import math
import matplotlib.pyplot as plt
import numpy as np

# Задание 1
def task1():
    """Написать функцию, которая определяет, является ли число простым.
    +1 балл: пятизначный палиндром.
    +1 балл: программа в бесконечном цикле."""
    def is_prime(n):
        """Определяет, является ли число простым."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_five_digit_palindrome(n):
        """Определяет, является ли число пятизначным палиндромом."""
        s = str(n)
        return len(s) == 5 and s == s[::-1]

    print("Задание 1: Проверка чисел на простоту и палиндром.")
    while True:
        try:
            num_str = input("Введите целое число (или 'exit' для выхода): ")
            if num_str.lower() == 'exit':
                break
            num = int(num_str)
            print(f"Число {num}:")
            print(f"  Простое: {'Да' if is_prime(num) else 'Нет'}")
            print(f"  5-значный палиндром: {'Да' if is_five_digit_palindrome(num) else 'Нет'}")
        except ValueError:
            print("Ошибка: введите целое число.")

# Задание 2
def task2():
    """Вычисление f(x) и график."""
    def f(x):
        """f(x) = tan(x) + sin(x) если x >= π, иначе x² - π²"""
        if x >= math.pi:
            return math.tan(x) + math.sin(x)
        else:
            return x**2 - math.pi**2

    print("Задание 2: Вычисление функции f(x)")
    try:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        x = float(input("Введите x для расчета: "))
        print(f"f({x:.4f}) = {f(x):.4f}")
        
        # График
        x_vals = np.linspace(a, b, 400)
        y_vals = [f(xi) for xi in x_vals]
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, 'b-', label='f(x)')
        plt.axvline(math.pi, color='r', linestyle='--', label='π')
        plt.grid(True)
        plt.legend()
        plt.title('График функции f(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.show()
    except ValueError:
        print("Ошибка ввода.")

# Задание 3
def task3():
    """Преобразование чисел в разные системы счисления."""
    def decimal_in_binary_numeral_system(number):
        """Десятичная дробь в двоичную."""
        return decimal_in_new_numeral_system(number, 2)

    def decimal_in_new_numeral_system(number, base=2, input_base=10):
        """Перевод дроби из input_base в base."""
        if not (2 <= base <= 36 and 2 <= input_base <= 36):
            raise ValueError("Основание должно быть от 2 до 36")
        
        # Разделяем целую и дробную часть
        if isinstance(number, str):
            num_str = number
        else:
            num_str = str(number)
        
        if '.' in num_str:
            int_part, frac_part = num_str.split('.')
        else:
            int_part, frac_part = num_str, ''
        
        # Перевод целой части
        int_val = int(int_part, input_base) if int_part else 0
        int_bin = ''
        if int_val == 0:
            int_bin = '0'
        else:
            while int_val > 0:
                int_bin = str(int_val % base) + int_bin
                int_val //= base
        
        # Перевод дробной части
        frac_bin = ''
        frac_val = 0
        if frac_part:
            frac_val = int(frac_part, input_base) / (input_base ** len(frac_part))
            precision = 20  # точность
            for _ in range(precision):
                frac_val *= base
                digit = int(frac_val)
                frac_bin += str(digit)
                frac_val -= digit
                if frac_val < 1e-10:
                    break
        
        result = int_bin
        if frac_bin:
            result += '.' + frac_bin
        return result

    print("Задание 3: Перевод в системы счисления")
    try:
        num = input("Введите число (например 0.5 или 10.25): ")
        base = int(input("Введите основание (base): ") or "2")
        print(f"В base={base}: {decimal_in_new_numeral_system(num, base)}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Задание 4
def task4():
    """Проверка точки в фигурах."""
    def is_point_in_figure1(x, y):
        """Фигура 1 (левый полигон)"""
        # Предполагаемая фигура 1: многоугольник с вершинами примерно (-4,-4), (-2,4), (2,2), etc. 
        # Для точности используем ray casting или проверки
        # Простая реализация с ray casting для полигонов
        # Вершины фигуры 1 (примерно по описанию)
        poly1 = [(-4, -4), (-2, 3), (2, 2), (4, -2), (-1, -3)]  # приблизительно
        return point_in_polygon(x, y, poly1)

    def is_point_in_figure2(x, y):
        """Фигура 2 (правый полигон)"""
        poly2 = [(0, -4), (2, 2), (5, 1), (3, -3)]  # приблизительно
        return point_in_polygon(x, y, poly2)

    def point_in_polygon(x, y, poly):
        """Ray casting algorithm"""
        n = len(poly)
        inside = False
        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    print("Задание 4: Проверка точки в фигуре")
    try:
        x = float(input("x = "))
        y = float(input("y = "))
        in1 = is_point_in_figure1(x, y)
        in2 = is_point_in_figure2(x, y)
        print(f"В фигуре 1: {'Да' if in1 else 'Нет'}")
        print(f"В фигуре 2: {'Да' if in2 else 'Нет'}")
        
        # График
        plt.figure()
        # Plot polygons...
        plt.scatter([x], [y], color='green' if in1 or in2 else 'red')
        plt.grid(True)
        plt.show()
    except:
        print("Ошибка.")

# Задание 5
def task5():
    """Среди a,b,c найти среднее и удвоить."""
    print("Задание 5")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        nums = [a, b, c]
        nums.sort()
        middle = nums[1]
        doubled = middle * 2
        print(f"Удвоено среднее число {middle:.4f} -> {doubled:.4f}")
    except:
        print("Ошибка.")

# Задание 6
def task6():
    """Расчет месяцев для сдачи лабораторных."""
    print("Задание 6")
    try:
        labs = int(input("Осталось лабораторных: "))
        cons_per_month = int(input("Консультаций в месяц: "))
        attempts = int(input("Попыток на лабораторную: "))
        
        months = 0
        while labs > 0:
            months += 1
            submitted = min(cons_per_month, labs)
            labs -= submitted
            attempts = max(1, attempts - 1)
            print(f"Месяц {months}: сдано {submitted}, осталось {labs}")
        print(f"Всего месяцев: {months}")
    except:
        print("Ошибка.")

# Задание 7
def task7():
    """Время рабочего дня по температуре."""
    def working_time(temperature):
        """По таблице"""
        if temperature < 28.5:
            return "7ч"
        elif temperature < 29:
            return "6ч"
        elif temperature < 30:
            return "5ч"
        elif temperature < 30.5:
            return "4ч"
        elif temperature < 31:
            return "3ч"
        elif temperature < 31.5:
            return "2ч"
        elif temperature < 32:
            return "1ч"
        else:
            return "Работа приостановлена"
    
    print("Задание 7")
    try:
        temp = float(input("Температура: "))
        print(f"Время: {working_time(temp)}")
    except:
        print("Ошибка.")

# Задание 8
def task8():
    """Ряд S"""
    def series_sum(x, n):
        s = x
        for i in range(1, n):
            term = math.factorial(i) * (x ** (2*i + 1)) / math.factorial(2*i + 1)
            s += term
        return s

    print("Задание 8")
    try:
        x = float(input("x = "))
        n = int(input("n = ") or "5")
        eps = float(input("epsilon = ") or "1e-6")
        print(f"Сумма первых {n} членов: {series_sum(x, n):.4f}")
    except:
        print("Ошибка.")

# Задание 9
def task9():
    """Вычисления сумм и произведений"""
    print("Задание 9")
    # Первое
    s1 = sum(sum((math.cos(j) + math.sin(i))**2 for j in range(1, i+1)) for i in range(1, 9))
    print(f"Сумма1: {s1:.4f}")
    
    # Второе
    p2 = 1
    for i in range(1, 6):
        for j in range(1, i+1):
            p2 *= j ** (i + 1)
    print(f"Произведение2: {p2:.4f}")
    
    # Третье
    s3 = 0
    for i in range(1, 9):
        for j in range(i, 2*i):
            for k in range(i+j, 2*(i+j)+1):
                s3 += math.log(2*j - 3*(i - 0.5*k))
    print(f"Сумма3: {s3:.4f}")

# Задание 10
def task10():
    """Корень p-й степени"""
    def koren(y, x, p):
        """Итерация Ньютона"""
        return (1/p) * ((p-1)*y + x / (y**(p-1)))
    
    print("Задание 10")
    try:
        x = float(input("x = "))
        p = int(input("Степень p = "))
        eps = 1e-6
        y = x ** (1/p)  # начальное
        iter = 0
        while True:
            iter += 1
            y_new = koren(y, x, p)
            if abs(y_new - y) <= eps:
                break
            y = y_new
            if iter > 100:
                break
        print(f"Корень {p}-й степени: {y:.4f} (итераций: {iter})")
    except:
        print("Ошибка.")

# Задание 11
def task11():
    """Cos(x) ряд"""
    print("Задание 11")
    try:
        x = float(input("x = "))
        eps = 1e-6
        cos_approx = 1.0
        term = 1.0
        i = 1
        while abs(term) > eps:
            term = (-1)**i * (x**(2*i)) / math.factorial(2*i)
            cos_approx += term
            i += 1
        print(f"cos({x:.4f}) ≈ {cos_approx:.4f}")
    except:
        print("Ошибка.")

# Задание 12
def task12():
    """Площадь под кривой"""
    def f(x):
        return 8 * x**5 - math.sin(x)
    
    def ploshadPryamougolnika(x1, x2, f1):
        return (x2 - x1) * f1
    
    print("Задание 12")
    try:
        a = 1.0
        b = 2.0
        n = int(input("Количество разбиений n = ") or "100")
        h = (b - a) / n
        s = 0.0
        for i in range(n):
            x = a + i * h
            s += ploshadPryamougolnika(x, x + h, f(x))
        print(f"Площадь ≈ {s:.4f}")
        
        # График
        x_plot = np.linspace(a, b, 200)
        plt.plot(x_plot, [f(xi) for xi in x_plot])
        plt.fill_between(x_plot, [f(xi) for xi in x_plot], alpha=0.3)
        plt.grid(True)
        plt.show()
    except:
        print("Ошибка.")

if __name__ == "__main__":
    print("Лабораторная работа: Ветвящиеся алгоритмы. Циклы. Вариант 16")
    while True:
        print("\nВыберите задание:")
        print("1-12 - выполнить задание")
        print("0 - выход")
        choice = input("Ваш выбор: ")
        if choice == '0':
            break
        elif choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '10':
            task10()
        elif choice == '11':
            task11()
        elif choice == '12':
            task12()
        else:
            print("Неверный выбор.")
