import nmap

def scan_network(ip_range):
    """Scan the specified IP range and return a list of active devices."""
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')  # -sn for ping scan
    devices = []
    
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            devices.append({
                'ip': host,
                'hostname': nm[host].hostname(),
                'state': nm[host].state()
            })
    
    return devices

# Example usage
if __name__ == "__main__":
    ip_range = "192.168.1.0/24"  # Example IP range
    active_devices = scan_network(ip_range)
    print(active_devices)
