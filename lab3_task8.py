import os


def show_menu():
    """Выводит меню действий"""
    print("   МИНИ-ПРОЕКТ: Работа с файлами и папками")
    print("="*50)
    print("1. Создание файла")
    print("2. Удаление файла")
    print("3. Создание директории")
    print("4. Удаление директории")
    print("="*50)


def list_current_dir():
    """Показывает содержимое текущей директории"""
    print(f"\nТекущая директория: {os.getcwd()}")
    items = os.listdir()
    if not items:
        print("Папка пуста.")
        return
    for i, item in enumerate(items, 1):
        if os.path.isdir(item):
            print(f"{i:2}. [ПАПКА]  {item}")
        else:
            print(f"{i:2}. [ФАЙЛ]   {item}")


def create_file():
    """Создание файла"""
    filename = input("\nВведите имя нового файла: ").strip()
    if not filename:
        print("Ошибка: Имя файла не может быть пустым")
        return
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Файл {filename} создан.\n")
        print(f"Файл '{filename}' успешно создан")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")


def delete_file():
    """Удаление файла"""
    filename = input("\nВведите имя файла для удаления: ").strip()
    if not filename:
        print("Ошибка: Имя файла не может быть пустым")
        return
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не существует")
        return
    try:
        os.remove(filename)
        print(f"Файл '{filename}' успешно удалён")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")


def create_directory():
    """Создание директории"""
    dirname = input("\nВведите имя новой директории: ").strip()
    if not dirname:
        print("Ошибка: Имя директории не может быть пустым")
        return
    try:
        os.makedirs(dirname, exist_ok=True)
        print(f"Директория '{dirname}' успешно создана")
    except Exception as e:
        print(f"Ошибка при создании директории: {e}")


def delete_directory():
    """Удаление директории"""
    dirname = input("\nВведите имя директории для удаления(должна быть пустой): ").strip()
    if not dirname:
        print("Ошибка: Имя директории не может быть пустым")
        return
    if not os.path.exists(dirname):
        print(f"Директория '{dirname}' не существует")
        return
    try:
        # rmdir удаляет только пустые директории
        os.rmdir(dirname)
        print(f"Директория '{dirname}' успешно удалена")
    except OSError:
        print(f"Ошибка: Директория '{dirname}' не пуста")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")


def main():
    while True:
        show_menu()
        list_current_dir()  # показываем содержимое каждый раз
        
        choice = input("\nВыберите действие (0-4): ").strip()
        
        if choice == '1':
            create_file()
        elif choice == '2':
            delete_file()
        elif choice == '3':
            create_directory()
        elif choice == '4':
            delete_directory()
        else:
            print("Введите число от 0 до 4")


if __name__ == "__main__":
    main()
