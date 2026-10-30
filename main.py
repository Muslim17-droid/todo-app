import storage
import ui
from logic import TaskManager


def main():
    manager = TaskManager(storage)
    ui.run(manager)


if __name__ == "__main__":
    main()