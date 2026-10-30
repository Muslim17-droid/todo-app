def print_menu():
    print("=== Список дел ===")
    print("1. Добавить дело")
    print("2. Показать все дела")
    print("3. Отметить выполненным")
    print("4. Удалить дело")
    print("0. Выход")


def show_tasks(tasks):
    if not tasks:
        print("Список пуст.")
        return
    for i, t in enumerate(tasks, 1):
        status = "V" if t.done else "X"
        print(f"{i}. [{status}] {t.title} (срок: {t.deadline})")


def run(manager):
    while True:
        print_menu()
        choice = input("Выбор: ").strip()
        if choice == "1":
            title = input("Название: ")
            deadline = input("Срок: ")
            manager.add(title, deadline)
        elif choice == "2":
            show_tasks(manager.list_all())
        elif choice == "3":
            show_tasks(manager.list_all())
            idx = int(input("Номер дела: ")) - 1
            manager.mark_done(idx)
        elif choice == "4":
            show_tasks(manager.list_all())
            idx = int(input("Номер дела: ")) - 1
            manager.delete(idx)
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Неверный ввод.")