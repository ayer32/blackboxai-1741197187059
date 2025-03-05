import subprocess

def run_nmap_scan(target):
    """Run an Nmap scan on the specified target."""
    try:
        result = subprocess.run(['nmap', target], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running Nmap scan: {str(e)}"

def run_wireshark():
    """Run Wireshark."""
    try:
        subprocess.Popen(['wireshark'])
        return "Wireshark launched successfully."
    except Exception as e:
        return f"Error launching Wireshark: {str(e)}"

# Example usage
if __name__ == "__main__":
    print(run_nmap_scan("192.168.1.1"))
    print(run_wireshark())
