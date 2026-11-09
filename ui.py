
def print_menu():
    print("\n=== Список дел ===")
    print("1. Добавить дело")
    print("2. Показать все дела")
    print("3. Отметить выполненным")
    print("4. Удалить дело")
    print("5. Показать невыполненные дела")
    print("0. Выход")


def show_tasks(tasks):
    if not tasks:
        print("Список пуст.")
        return

    for i, task in enumerate(tasks, 1):
        status = "V" if task.done else "X"
        print(f"{i}. [{status}] {task.title} (срок: {task.deadline})")


def run(manager):
    while True:
        print_menu()
        choice = input("Выбор: ").strip()

        if choice == "1":
            title = input("Название: ").strip()
            deadline = input("Срок: ").strip()

            try:
                manager.add_task(title, deadline)
                print("Дело успешно добавлено!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            show_tasks(manager.get_all())

        elif choice == "3":
            show_tasks(manager.get_all())

            try:
                title = input("Введите название дела: ").strip()
                manager.mark_done_by_title(title)
                print("Дело отмечено выполненным!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            show_tasks(manager.get_all())

            try:
                title = input("Введите название дела: ").strip()
                manager.remove_task(title)
                print("Дело удалено!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            show_tasks(manager.get_pending())

        elif choice == "0":
            print("Пока!")
            break

        else:
            print("Неверный ввод.")
1