Coupe_du_monde_API
Objectif :

Cette API représente les équipes et les matches de la coupe du monde 2022
Via cette API, nous allons pouvoir effectuer les actions suivantes
MATCHES
Récupérer les matches, avec la possibilité de filtrer par :
Date
Équipe
Status
Stade
Créer un match
Modifier un match
Récupérer un match
ÉQUIPE
Récupérer les informations d’une équipe
Créer une équipe
Modifier une équipe
Récupérer les équipes participantes avec la possibiliter de filter sur
Group
----Sur Windows----

Pré-requis : Python : -Installer Python -Pour vérifier si Python est correctement installé vous pouvez exécuter cette commande à partir de votre terminal : *python --version

Environnement virtuel : -Créer un dossier pour le projet *mkdir CMD *cd CMD

-Créer l'environnement virtuel lié au projet *python -m venv env

-Pour l'activer *env\Scripts\activate

-Pour le désactiver *deactivate

-Installation de Django *pip install django

*pip install djangorestframework

-Installation de git project

git clone https://github.com/BENACHOUR14/Coupe_du_monde_API.git
-Migration *python manage.py makemigrations *python manage.py migrate
