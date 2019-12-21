# pyportal_bus_toulouse

Affiche les prochains bus à toulouse et environs sur un pyportal

# Pour commencer
    
1. Envoyer un mail à l'équipe qui gère les accès de l'api de tisséo pour avoir un token opendata@tisseo.fr
    * renseignez le token dans le fichier secrets.json du pyportal avec la clef tisseo_token
2. Récupérer la liste de arrets à l'url http://api.tisseo.fr/v1/stop_areas.json?key=<Votre token> à l'aide d'un navigateur 
3. Rechercher l'id de votre arrêt de départ, mettez le dans la variable stop_id dans le fichier code.py
4. la variable schedule_index permet de choisir le sens de la ligne (0/1) 
    * Attention, les tests ont été fait sur un arrêt avec une seule ligne

Transférez tout ça sur le pyportal & have fun

Enjoy & don't miss your bus

## liens 
https://www.adafruit.com/product/4116
https://fr.m.wikipedia.org/wiki/Fichier:Bus-logo.svg

