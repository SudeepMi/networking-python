from scapy.all import sniff, IP

def packet_handler(packet):
   if IP in packet:
       print(f"Source IP: {packet[IP].src}, Destination IP: {packet[IP].dst}")


sniff(prn=packet_handler, count=10)  # Sniff 10 packets

# The sniff() function returns information about all the packets that has been sniffed.
capture = sniff(count=5)
print(capture.summary())

# The following command will capture only TCP packets:
print(sniff(filter="tcp", count=5))
