import unittest
import logging
from src.task_manager import run_command
from tests.base_test_setup import BaseTestSetup

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Scenario
# Step 1: List tasks (initial state)
# Step 2: Add a new task
# Step 3: List tasks (to confirm the new task is added)
# Step 4: Delete the added task
# Step 5: List tasks (to confirm the task is deleted)

class TestIntegration(BaseTestSetup):
    TASK_DESCRIPTION = "Python Program"

    def test_add_and_delete_task(self):
        # Step 1: List tasks (initial state)
        logging.info("Running initial 'task list' command")
        result_list_initial = run_command("task", "list")
        self.assertEqual(result_list_initial.returncode, 1,
                         f"Initial 'task list' failed with return code {result_list_initial.returncode}: {result_list_initial.stderr}")

        # Step 2: Add a new task
        logging.info(f"Running 'task add {self.TASK_DESCRIPTION}' command")
        result_add = run_command("task", "add", self.TASK_DESCRIPTION)
        self.assertEqual(result_add.returncode, 0,
                         f"'task add {self.TASK_DESCRIPTION}' failed with return code {result_add.returncode}: {result_add.stderr}")

        # Step 3: List tasks (to confirm the new task is added)
        logging.info("Running 'task list' command after adding new task")
        result_list_after_add = run_command("task", "list")
        self.assertEqual(result_list_after_add.returncode, 0,
                         f"'task list' after adding new task failed with return code {result_list_after_add.returncode}: {result_list_after_add.stderr}")
        self.assertIn(self.TASK_DESCRIPTION, result_list_after_add.stdout,
                      f"New task '{self.TASK_DESCRIPTION}' was not found in the list")

        # Step 4: Delete the added task
        logging.info(f"Running 'task delete description /{self.TASK_DESCRIPTION}/' command")
        exitstatus_delete = run_command("task", "delete", "description", f"/{self.TASK_DESCRIPTION}/")
        self.assertEqual(exitstatus_delete, 1,
                         f"'task delete description /{self.TASK_DESCRIPTION}/' failed with exit status {exitstatus_delete}")

        # Step 5: List tasks (to confirm the task is deleted)
        logging.info("Running 'task list' command after deleting the task")
        result_list_after_delete = run_command("task", "list")
        self.assertEqual(result_list_after_delete.returncode, 1,
                         f"'task list' after deleting task failed with return code {result_list_after_delete.returncode}: {result_list_after_delete.stderr}")
        self.assertNotIn(self.TASK_DESCRIPTION, result_list_after_delete.stdout,
                         f"Deleted task '{self.TASK_DESCRIPTION}' was still found in the list")


if __name__ == '__main__':
    unittest.main(verbosity=2)
