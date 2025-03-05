from scapy.all import sniff
import logging

def packet_callback(packet):
    """Callback function to process captured packets."""
    logging.info(f"Packet captured: {packet.summary()}")
    # Here you can add logic to analyze the packet for suspicious activity

def start_traffic_monitoring(interface=None):
    """Start capturing network traffic on the specified interface."""
    print("Starting traffic monitoring...")
    sniff(iface=interface, prn=packet_callback, store=0)

# Example usage
if __name__ == "__main__":
    start_traffic_monitoring()  # Capture on the default interface
