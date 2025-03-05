import nmap

def scan_ports(target_ip):
    """Scan the specified target IP for open ports."""
    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-p 1-65535')  # Scan all ports
    open_ports = []
    
    for port in nm[target_ip]['tcp']:
        if nm[target_ip]['tcp'][port]['state'] == 'open':
            open_ports.append(port)
    
    return open_ports

# Example usage
if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Example target IP
    open_ports = scan_ports(target_ip)
    print(f"Open ports on {target_ip}: {open_ports}")
