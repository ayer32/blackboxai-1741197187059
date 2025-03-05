from scapy.all import *

def packet_callback(packet):
    """Callback function to process captured packets for intrusion detection."""
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Packet: {ip_src} -> {ip_dst}")
        # Here you can add logic to analyze the packet for suspicious activity

def start_monitoring(interface):
    """Start monitoring network traffic on the specified interface."""
    print("Starting intrusion detection...")
    sniff(iface=interface, prn=packet_callback, store=0)

# Example usage
if __name__ == "__main__":
    interface = "wlan0"  # Network interface
    start_monitoring(interface)
