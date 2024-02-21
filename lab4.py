from scapy.all import sniff, DNS, DNSQR, DNSRR

expected_dns_responses = {"ekantipur.com": "172.67.167.186"}

def dns_spoofing_detector(packet):
   print(packet)
   if DNS in packet and packet[DNS].qr:  # Check if it's a DNS response
       dns_question = packet[DNS].qd
       domain = dns_question.qname.decode()
      
       if domain in expected_dns_responses:
           print(domain)
           if packet.haslayer(DNSRR) and packet[DNSRR].rdata != expected_dns_responses[domain]:
               print(f"DNS Spoofing detected for {domain}! Expected: {expected_dns_responses[domain]}, Actual: {packet[DNSRR].rdata}")

sniff(prn=dns_spoofing_detector, filter="udp port 53", store=3, count=10)