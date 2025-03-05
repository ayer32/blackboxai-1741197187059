import unittest
from utils.logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_log_info(self):
        with self.assertLogs('NetManEthics', level='INFO') as log:
            self.logger.log_info("This is an info message.")
            self.assertIn("This is an info message.", log.output[0])

    def test_log_error(self):
        with self.assertLogs('NetManEthics', level='ERROR') as log:
            self.logger.log_error("This is an error message.")
            self.assertIn("This is an error message.", log.output[0])

if __name__ == "__main__":
    unittest.main()
