import matplotlib.pyplot as plt

def visualize_traffic(data):
    """Visualize network traffic data."""
    plt.figure(figsize=(10, 5))
    plt.plot(data['time'], data['traffic'], label='Traffic Over Time')
    plt.xlabel('Time')
    plt.ylabel('Traffic (bytes)')
    plt.title('Network Traffic Visualization')
    plt.legend()
    plt.grid()
    plt.show()

def visualize_scan_results(scan_results):
    """Visualize scan results."""
    ip_addresses = [result['ip'] for result in scan_results]
    states = [result['state'] for result in scan_results]

    plt.figure(figsize=(10, 5))
    plt.bar(ip_addresses, states)
    plt.xlabel('IP Address')
    plt.ylabel('State')
    plt.title('Scan Results Visualization')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    sample_traffic_data = {
        'time': [1, 2, 3, 4, 5],
        'traffic': [100, 200, 150, 300, 250]
    }
    visualize_traffic(sample_traffic_data)

    sample_scan_results = [
        {'ip': '192.168.1.1', 'state': 'Active'},
        {'ip': '192.168.1.2', 'state': 'Inactive'},
        {'ip': '192.168.1.3', 'state': 'Active'}
    ]
    visualize_scan_results(sample_scan_results)
