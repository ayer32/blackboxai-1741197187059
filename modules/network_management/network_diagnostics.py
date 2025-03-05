import subprocess

def ping(host):
    """Ping a host and return the result."""
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error pinging {host}: {e}"

def traceroute(host):
    """Perform a traceroute to a host and return the result."""
    try:
        output = subprocess.check_output(['traceroute', host], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error performing traceroute to {host}: {e}"

# Example usage
if __name__ == "__main__":
    print(ping("8.8.8.8"))  # Example ping
    print(traceroute("8.8.8.8"))  # Example traceroute
