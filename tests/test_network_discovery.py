import unittest
from modules.network_discovery import scan_network

class TestNetworkDiscovery(unittest.TestCase):

    def test_scan_network(self):
        result = scan_network("192.168.1.0/24")  # Replace with a valid IP range
        self.assertIsInstance(result, list)  # Check if the result is a list

if __name__ == '__main__':
    unittest.main()
