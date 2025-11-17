# système de détections d'intrusions 
from datetime import datetime
import time
from generator_log import is_private_ip
import re
fails_log = {}




with open("test.log", "r") as f:
    f.seek(0, 2)
    while True: # surveillance constante du fichier terminal/test log
        line=f.readline()
        if not line : 
            print("en attente de nouvelles lignes...")
            time.sleep(1)
        
            continue
        if "Accepted password" in line :
                continue 
        
        match = re.search(r'(\d{1,3}\.){3}\d{1,3}', line)
        if match :
             ip = match.group()
        else:
              continue  # aucune IP on passe à la ligne suivante
            
        if "Failed password" in line or "Invalid user" in line :
            if not is_private_ip(ip): 
                fails_log[ip] = fails_log.get(ip, 0) + 1
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
                print(timestamp, f"[!] Tentative ratée depuis {ip} (compteur = {fails_log[ip]})")
                if fails_log[ip] >= 3:
                    with open("alerts.log", "a") as alert_file :
                        alert_msg = f" {timestamp} [ALERTE] Adresse IP publique suspecte detectee : {ip} avec {fails_log[ip]} tentatives echouees.\n"
                        alert_file.write(alert_msg)
                    print("Adresse IP suspecte : ", ip)

                

        


       
