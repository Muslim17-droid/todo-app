
class Task:
    """Дело в списке дел."""

    def __init__(self, title: str, deadline: str, done: bool = False):
        if not title or not title.strip():
            raise ValueError("Название дела не может быть пустым")

        self.title = title.strip()
        self.deadline = deadline
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self) -> str:
        status = "выполнено" if self.done else "не выполнено"
        return f"{self.title} (до {self.deadline}) — {status}"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "deadline": self.deadline,
            "done": self.done
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["title"],
            data["deadline"],
            data.get("done", False)
        )


class TaskManager:
    """Управляет списком дел."""

    def __init__(self, storage=None):
        self.storage = storage
        self.tasks = []

    def load(self):
        if self.storage is not None:
            self.tasks = self.storage.load()

    def save(self):
        if self.storage is not None:
            self.storage.save(self.get_all())

    def add(self, title, deadline):
        self.add_task(title, deadline)

    def add_task(self, title: str, deadline: str) -> Task:
        task = Task(title, deadline)
        self.tasks.append(task)
        return task

    def list_all(self):
        return self.get_all()

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def remove_task(self, title: str) -> None:
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return
        raise ValueError(f"Дело «{title}» не найдено")

    def mark_done_by_title(self, title: str) -> None:
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return
        raise ValueError(f"Дело «{title}» не найдено")

    def get_all(self) -> list:
        return list(self.tasks)

    def get_pending(self) -> list:
        return [task for task in self.tasks if not task.done]

    def count(self) -> int:
        return len(self.tasks)

    def get_sorted_by_deadline(self) -> list:
        return sorted(self.tasks, key=lambda task: task.deadline)
