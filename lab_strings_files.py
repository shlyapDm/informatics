import random  # task2() task4()
import os      # task7() task3() task5() task6()


# ==== ЗАДАНИЕ 1 =====
def print_char_list(array):
    """Выводит одномерный массив символов"""
    for char in array:
        print(char, end=' ')
    print()

def task1():
    n = int(input("Введите количество элементов массива: "))
    array = []
    for i in range(n):
        element = input(f"Введите {i+1} символ: ")
        array.append(element)

    print("Исходный массив:")
    print_char_list(array)

    for i in range(len(array)):
        if array[i].isdigit():
            array[i] = '*'

    print("Модифицированный массив:")
    print_char_list(array)



# ==== ЗАДАНИЕ 3 =====
def task3():
    file_capitals = "../data/capitals.txt"
    file_lowers = "../data/lowers.txt"

    # Очистка файлов
    with open(file_capitals, 'w', encoding='utf-8') as f:
        pass
    with open(file_lowers, 'w', encoding='utf-8') as f:
        pass

    print("Начинаем сортировку строк (нужно ввести 5 раз)")

    for i in range(5):
        text = input("Введите текст: ")
        if len(text) > 0 and text[0].isupper():
            with open(file_capitals, 'a', encoding='utf-8') as f:
                f.write(text + '\n')
        else:
            with open(file_lowers, 'a', encoding='utf-8') as f:
                f.write(text + '\n')

    print("Текст успешно распределен по файлам")



# ==== ЗАДАНИЕ 4 =====
def print_string_list(array):
    """Выводит список строк"""
    for item in array:
        print(item)


def random_choice(array):
    """Возвращает случайный элемент массива"""
    return random.choice(array)


def task4():
    apps = ["Instagram", "TikTok", "YouTube", "Telegram", "WhatsApp",
        "VKontakte", "Discord", "Twitter", "Facebook", "Snapchat",
        "Pinterest", "Reddit", "LinkedIn", "Twitch", "Steam"]

    print("Список:")
    print_string_list(apps)
    print()

    print("Для получения случайного элемента массива нажмите Enter")
    print("(для выхода введите 'q')\n")

    while True:
        user_input = input()
        if user_input.strip().lower() == 'q':
            print("Выход из режима случайного выбора.")
            break

        random_app = random_choice(apps)
        print(f"Случайный элемент: {random_app}")
        print("Нажмите Enter для нового элемента (или q для выхода)")



# ==== ЗАДАНИЕ 5 =====
def task5():
    print("Введите текст:")
    text = input()

    file_path = "../data/task1.out"

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"\nТекст успешно записан в файл: {file_path}")
        print("Содержимое файла:")
        print("-" * 40)
        print(text)
        print("-" * 40)
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")



# ==== ЗАДАНИЕ 7 =====
def task7():
    print("Введите имя новой директории:")
    dir_name = input().strip()

    dir_path = os.path.join("../data", dir_name)

    try:
        os.makedirs(dir_path, exist_ok=True)
        print(f"Директория '{dir_name}' успешно создана по пути: {dir_path}")
    except Exception as e:
        print(f"Ошибка при создании директории: {e}")
        return

    print("Введите имя нового файла:")

    file_name = input().strip()
    file_path = os.path.join(dir_path, file_name)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"файл {file_name}\nСоздан в директории {dir_name}\n")

        print(f"Файл '{file_name}' успешно создан в директории '{dir_name}'")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
