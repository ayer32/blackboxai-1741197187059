import unittest
from modules.api_integration import authenticate, start_scan, get_scan_results

class TestAPIIntegration(unittest.TestCase):

    def test_authenticate(self):
        token = authenticate()
        self.assertIsNotNone(token)  # Check if token is returned

    def test_start_scan_valid(self):
        result = start_scan(1)  # Replace with a valid scan ID
        self.assertIn("Scan started", result)  # Check if scan starts successfully

    def test_start_scan_invalid(self):
        result = start_scan(9999)  # Replace with an invalid scan ID
        self.assertIn("Error", result)  # Check if an error is returned

    def test_get_scan_results_valid(self):
        results = get_scan_results(1)  # Replace with a valid scan ID
        self.assertIsInstance(results, dict)  # Check if results are returned as a dictionary

    def test_get_scan_results_invalid(self):
        results = get_scan_results(9999)  # Replace with an invalid scan ID
        self.assertIn("Error", results)  # Check if an error is returned

if __name__ == '__main__':
    unittest.main()
