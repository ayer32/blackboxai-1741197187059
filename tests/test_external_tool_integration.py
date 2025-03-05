import unittest
from modules.external_tool_integration import run_nmap_scan, run_wireshark

class TestExternalToolIntegration(unittest.TestCase):

    def test_run_nmap_scan(self):
        result = run_nmap_scan("127.0.0.1")
        self.assertIn("Nmap done:", result)  # Check if the result contains expected output

    def test_run_wireshark(self):
        result = run_wireshark()
        self.assertEqual(result, "Wireshark launched successfully.")  # Check if Wireshark launches correctly

if __name__ == '__main__':
    unittest.main()
