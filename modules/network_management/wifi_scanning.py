import subprocess

def scan_wifi():
    """Scan for nearby wireless networks and return the results."""
    try:
        # Using airodump-ng to scan for wireless networks
        output = subprocess.check_output(['airodump-ng', '--band', 'bg', 'wlan0'], universal_newlines=True)
        networks = []
        
        # Process the output to extract relevant information
        for line in output.splitlines():
            if "ESSID" in line:
                parts = line.split()
                ssid = parts[parts.index("ESSID:") + 1].strip('"')
                bssid = parts[0]
                channel = parts[3]
                encryption = parts[4]
                signal_strength = parts[5]
                networks.append({
                    'SSID': ssid,
                    'BSSID': bssid,
                    'Channel': channel,
                    'Encryption': encryption,
                    'Signal Strength': signal_strength
                })
        
        return networks
    except Exception as e:
        return f"Error scanning WiFi networks: {e}"

# Example usage
if __name__ == "__main__":
    wifi_networks = scan_wifi()
    print(wifi_networks)
