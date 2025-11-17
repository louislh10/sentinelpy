messages = ["Failed password for invalid user", "Failed password for root from", "Accepted password for user bob from"] 
ips = ["192.168.1.15", "10.0.0.42", "45.183.76.22", "203.0.113.55"]

import time
import random
from datetime import datetime
import ipaddress
import re

def is_private_ip(ip):
    return ipaddress.ip_address(ip).is_private


if __name__ == "__main__": 
    with open("test.log", "a") as f:
        while True :
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{timestamp} { (random.choice( messages) + "\n")}"

            ip = random.choice(ips)
            msg =random.choice(messages)
            line = f"{timestamp} {msg} {ip}\n"
            f.write(line)
            print(line)
            f.seek(0, 2) # se positionner à la fin du fichier pour lire les nouvelles lignes
            time.sleep(2)
    

#écriture dans test log en temps réel