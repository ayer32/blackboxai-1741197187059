import nmap

def get_device_info(ip_range):
    """Retrieve and return details about connected devices in the specified IP range."""
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sP')  # -sP for ping scan
    devices = []
    
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            devices.append({
                'ip': host,
                'hostname': nm[host].hostname(),
                'mac': nm[host]['addresses'].get('mac', 'N/A'),
                'os': nm[host]['osmatch'][0]['name'] if nm[host]['osmatch'] else 'N/A',
                'open_ports': nm[host]['tcp'].keys() if 'tcp' in nm[host] else []
            })
    
    return devices

def fingerprint_device(ip):
    """Perform device fingerprinting on the specified IP address."""
    nm = nmap.PortScanner()
    nm.scan(ip)
    if nm[ip].state() == 'up':
        os_info = nm[ip]['osmatch'][0]['name'] if nm[ip]['osmatch'] else 'N/A'
        services = nm[ip]['tcp'].keys() if 'tcp' in nm[ip] else []
        return {
            'ip': ip,
            'os': os_info,
            'services': list(services)
        }
    return None

# Example usage
if __name__ == "__main__":
    ip_range = "192.168.1.0/24"  # Example IP range
    device_info = get_device_info(ip_range)
    print(device_info)

    # Example fingerprinting
    fingerprint = fingerprint_device("192.168.1.1")  # Example IP
    print(fingerprint)
