class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        self.title = title
        self.deadline = deadline
        self.done = done


    def mark_done(self):
        self.done = True

    def __str__(self) -> str:
        status = "выполнено" if self.done else "не выполнено"
        return f"{self.title} (до {self.deadline}) — {status}"

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = [Task.from_dict(d) for d in storage.load()]

    def add(self, title, deadline):
        self.tasks.append(Task(title, deadline))
        self._save()

    def list_all(self):
        return self.tasks

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            self._save()

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self._save()

    def _save(self):
        self.storage.save([t.to_dict() for t in self.tasks])