import unittest
import logging
from src.task_manager import run_command

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BaseTestSetup(unittest.TestCase):

    def setUp(self):
        logging.info("Setting up test environment")
        result_delete_all = run_command("task", "delete", "all")
        if isinstance(result_delete_all, int):
            self.assertEqual(result_delete_all, 1, f"Setup 'task delete all' failed with exit status {result_delete_all}")
        else:
            self.assertIn("No matches.", result_delete_all, "Unexpected output during setup 'task delete all'")

    def tearDown(self):
        logging.info("Tearing down test environment")
        result = run_command("task", "delete", "description", "/Python Program/")
        if isinstance(result, int):
            self.assertEqual(result, 1, f"Teardown 'task delete description /Python Program/' failed with exit status {result}")
        else:
            self.assertIn("No matches.", result, "Unexpected output during teardown 'task delete description /Python Program/'")
