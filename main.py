
from logic import TaskManager
from storage import Storage
import ui


def main():
    storage = Storage("tasks.json")
    manager = TaskManager(storage)

    try:
        manager.load()
    except ValueError as e:
        print(f"Предупреждение: {e}")
        print("Начинаем с пустого списка дел")

    ui.run(manager)

    manager.save()
    print("Данные сохранены")


if __name__ == "__main__":
    main()
