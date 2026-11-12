
import unittest
from logic import Task, TaskManager


class TestTask(unittest.TestCase):

    def test_default_not_done(self):
        task = Task("Дело", "2026-11-13")
        self.assertFalse(task.done)

    def test_mark_done(self):
        task = Task("Дело", "2026-11-13")
        task.mark_done()
        self.assertTrue(task.done)

    def test_title_is_stripped(self):
        task = Task(" Хлеб ", "2026-11-13")
        self.assertEqual(task.title, "Хлеб")

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            Task("", "2026-11-13")

    def test_spaces_only_title_raises(self):
        with self.assertRaises(ValueError):
            Task("   ", "2026-11-13")


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task("Хлеб", "2026-11-13")
        self.manager.add_task("Цветы", "2026-11-14")

    def test_add_and_count(self):
        self.assertEqual(self.manager.count(), 2)

    def test_get_all_returns_copy(self):
        tasks = self.manager.get_all()
        tasks.pop()
        self.assertEqual(self.manager.count(), 2)

    def test_mark_done_and_get_pending(self):
        self.manager.mark_done_by_title("Хлеб")
        pending = self.manager.get_pending()
        self.assertEqual([t.title for t in pending], ["Цветы"])

    def test_remove_existing(self):
        self.manager.remove_task("Хлеб")
        self.assertEqual(self.manager.count(), 1)

    def test_remove_missing_raises(self):
        with self.assertRaises(ValueError):
            self.manager.remove_task("Нет такого")

    def test_mark_done_missing_raises(self):
        with self.assertRaises(ValueError):
            self.manager.mark_done_by_title("Нет такого")

    def test_get_sorted_by_deadline(self):
        result = self.manager.get_sorted_by_deadline()
        self.assertEqual(
            [t.title for t in result],
            ["Хлеб", "Цветы"]
        )


if __name__ == "__main__":
    unittest.main()
