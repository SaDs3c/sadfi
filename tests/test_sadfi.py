import unittest
from unittest.mock import patch, MagicMock
from sadfi.main import scan_wifi_networks, header

class TestSadFi(unittest.TestCase):

    @patch('subprocess.check_output')
    def test_scan_wifi_networks_success(self, mock_check_output):
        # Mocking subprocess.check_output to return a sample JSON string
        mock_check_output.return_value = b'{"networks": [{"ssid": "TestSSID", "bssid": "00:11:22:33:44:55", "frequency_mhz": 2412, "rssi": -55}]}'

        result = scan_wifi_networks()

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["ssid"], "TestSSID")

    @patch('subprocess.check_output', side_effect=Exception("Mocked Exception"))
    def test_scan_wifi_networks_failure(self, mock_check_output):
        result = scan_wifi_networks()

        self.assertIsNone(result)

    def test_header(self):
        # Redirect stdout to capture print output
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
            header()

        result = mock_stdout.getvalue().strip()
        self.assertTrue(result.startswith('-'))
        self.assertIn("This SadSec tool allows access to all last wifi scan information.", result)

if __name__ == '__main__':
    unittest.main()
