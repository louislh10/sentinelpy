# système de détections d'intrusions 

import time
from generator_log import is_private_ip
import re



with open("test.log", "r") as f:
    f.seek(0, 2)
    while True: # surveillance constante du fichier test log
        line=f.readline()
        if not line : 
            print("en attente de nouvelles lignes...")
            time.sleep(2)
        
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
                print("Adresse IP suspecte : ", ip)
                

        


       
