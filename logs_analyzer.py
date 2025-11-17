# système de détections d'intrusions 

import time


with open("test.log", "r") as f:
    f.seek(0, 2)
    while True: # surveillance constante du fichier
        line = f.readline()
        if "Failed password" in line:
            print(line)
        else :
            time.sleep(0.1)
            continue
        

         
