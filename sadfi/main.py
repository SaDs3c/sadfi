import subprocess
import json
import logging
from tabulate import tabulate

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scan_wifi_networks():
    try:
        result = subprocess.check_output(["termux-wifi-scaninfo"])
        networks = json.loads(result)
        return networks
    except Exception as e:
        logger.error(f"Error during Wi-Fi scan: {e}")
        return None

def header():
    print('-'*60)
    print('This SadSec tool allows access to all last wifi scan information.\n')
    return None

def main():
    wifi_data = scan_wifi_networks()
    if wifi_data:
        table_headers = ["SSID", "BSSID", "Frequency", "RSSI"]

        # Check for the existence of keys before accessing them
        table_data = [
            [
                network.get("ssid", ""),
                network.get("bssid", ""),
                network.get("frequency_mhz", ""),
                network.get("rssi", "")
            ]
            for network in wifi_data
        ]

        header()
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    else:
        print("Could not scan for networks or no networks found.")

if __name__ == "__main__":
    main()
