SentinelPy est un petit système de détection d’intrusion écrit en Python.
Il surveille en temps réel un fichier de logs SSH, détecte les tentatives de connexion suspectes et génère des alertes dès qu’une adresse IP publique échoue plusieurs fois.

Fonctionnalités :

Surveillance en temps réel d’un fichier test.log
Extraction automatique des adresses IP via expressions régulières
Filtrage des adresses privées pour n’analyser que les IP externes
Détection des tentatives échouées (Failed password, Invalid user)
Compteur de tentatives par adresse IP
Alerte écrite dans alerts.log après 3 échecs
Génération automatique de logs d’activité (via generator_log.py)
Code simple, robuste et facilement extensible

Lancer le générateur de logs :
python generator_log.py

Lancer l’analyseur :
python logs_analyzer.py

Le système surveille alors le fichier en continu.

Le programme lit les nouvelles lignes du fichier test.log

Si une ligne contient :
Failed password
Invalid user

Et si l’IP est publique
→ Le compteur d’échecs augmente
À partir de 3 tentatives, l’adresse IP est considérée suspecte.

J'aimerai développer y ajouter un système d'alertes par mail dès lors que alertes_logs est alimenté
