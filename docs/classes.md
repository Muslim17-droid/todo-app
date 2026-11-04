# Классы системы «Список дел»

## Task
- Атрибуты: title (str), deadline (str), done (bool)
- Методы: mark_done(), __str__()
- Назначение: модель одного дела.

## TaskManager
- Атрибуты: tasks (list)
- Методы: add_task(), remove_task(), get_all(), find_by_title()
- Назначение: управление коллекцией дел.

## TaskStorage
- Атрибуты: filename (str)
- Методы: load(), save()
- Назначение: персистентность (файл).

## ConsoleUI
- Атрибуты: manager (TaskManager)
- Методы: run(), print_menu(), print_tasks()
- Назначение: консольный интерфейс.

## Связи
- ConsoleUI → TaskManager: ассоциация (UI владеет менеджером).
- TaskManager → Task: агрегация (менеджер содержит список дел).
- TaskManager → TaskStorage: зависимость (используется при сохранении).
- TaskStorage не связана с ConsoleUI — зависимость идёт только «вниз».