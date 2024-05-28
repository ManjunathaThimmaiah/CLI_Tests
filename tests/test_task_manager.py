import unittest
import logging
from src.task_manager import run_command
from tests.base_test_setup import BaseTestSetup

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TestTaskManager(BaseTestSetup):

    def test_list(self):
        logging.info("Running 'task list' command")
        result = run_command("task", "list")
        self.assertEqual(result.returncode, 1,
                         f"Command 'task list' failed with return code {result.returncode}: {result.stderr}")

    def test_add(self):
        logging.info("Running 'task add Python Program' command")
        result = run_command("task", "add", "Python Program")
        self.assertEqual(result.returncode, 0,
                         f"Command 'task add Python Program' failed with return code {result.returncode}: {result.stderr}")

    def test_delete(self):
        logging.info("Running 'task delete description /Python Program/' command")
        result = run_command("task", "delete", "description", "/Python Program/")
        self.assertEqual(result, 1, f"Command 'task delete description /Python Program/' failed.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
