import unittest
import os
from logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        """Sets up the Logger instance and log file for testing."""
        self.log_file = 'test_log.txt'
        self.logger = Logger(self.log_file)

    def tearDown(self):
        """Cleans up by removing the log file after each test."""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_metadata(self):
        """Tests the write_metadata method of the Logger class."""
        self.logger.write_metadata(1000, 0.05, "Sniffles", 0.12, 0.5, 50)
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, 'r') as file:
            content = file.read()
        self.assertIn("Population size: 1000", content)
        self.assertIn("Initial number of infected people: 50", content)

if __name__ == "__main__":
    unittest.main()