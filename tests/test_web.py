import unittest
from flask import json
from modules.web import app

class TestWebIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_nmap_scan(self):
        response = self.app.post('/nmap', json={'target': '127.0.0.1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.get_json())

    def test_nessus_start_scan(self):
        response = self.app.post('/nessus/start', json={'scan_id': 1})  # Replace with a valid scan ID
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.get_json())

    def test_nessus_get_results(self):
        response = self.app.get('/nessus/results/1')  # Replace with a valid scan ID
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.get_json())

    def test_get_incidents(self):
        response = self.app.get('/incidents')
        self.assertEqual(response.status_code, 200)
        self.assertIn('incidents', response.get_json())

    def test_get_scans(self):
        response = self.app.get('/scans')
        self.assertEqual(response.status_code, 200)
        self.assertIn('scans', response.get_json())

if __name__ == '__main__':
    unittest.main()
