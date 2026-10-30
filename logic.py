class Task:
    def __init__(self, title: str, deadline: str, done: bool = False):
        self.title = title
        self.deadline = deadline
        self.done = done

    def to_dict(self):
        return {"title": self.title, "deadline": self.deadline, "done": self.done}

    @staticmethod
    def from_dict(d):
        return Task(d["title"], d["deadline"], d.get("done", False))


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