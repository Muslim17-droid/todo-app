
import unittest
from logic import Task, TaskManager


class FakeStorage:
    """Тестовое хранилище без записи в файл."""

    def load(self):
        return []

    def save(self, data):
        pass


class TestTask(unittest.TestCase):

    def test_mark_done(self):
        task = Task("Дело", "2026-11-11")

        self.assertFalse(task.done)

        task.mark_done()

        self.assertTrue(task.done)

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("   ", "2026-11-11")


class TestTaskManager(unittest.TestCase):

    def test_add_and_count(self):
        manager = TaskManager(FakeStorage())

        manager.add_task("Дело 1", "2026-11-11")
        manager.add_task("Дело 2", "2026-11-12")

        self.assertEqual(manager.count(), 2)

    def test_remove_missing_raises(self):
        manager = TaskManager(FakeStorage())

        with self.assertRaises(ValueError):
            manager.remove_task("Нет такого")


if __name__ == "__main__":
    unittest.main()
