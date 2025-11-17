messages = ["Failed password for invalid user", "Failed password for root from", "Accepted password for user bob from"] 

import time
import random

with open("test.log", "w") as f:
    while True :
        line = (random.choice(messages) + "\n")
        f.write(line)
        print(line)
        f.seek(0, 2) # se positionner à la fin du fichier pour lire les nouvelles lignes
        time.sleep(5)

#écriture dans test log en temps réel