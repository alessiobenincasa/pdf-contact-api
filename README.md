# pdf-contact-api
API d'upload de PDF : Extraire le texte de la couche OCR et repérer automatiquement les infos de contact (Nom, Email, Téléphone, Adresse) grâce à un LLM. Les données sont sauvegardées dans une base et accessibles via un endpoint. Un projet simple, rapide et efficace démontrant mes compétences en IA &amp; backend. 

# PDF Uploader API

***Version : 0.1.0***

***

## Introduction

Cette API a pour objectif d'extraire le texte et les contacts d'un fichier PDF envoyé par l'utilisateur.  
Les contacts extraits sont ensuite stockés dans une base de données.

> **Note** : La configuration et la mise en place de la base de données restent à implémenter (TODO).

***

## Fonctionnalités

- **Upload de PDF** : Permet d'uploader un fichier PDF via l'endpoint `/upload/` pour en extraire le texte et les contacts.
- **Extraction de contacts** : Utilise la fonction `extract_contacts_with_hf` pour récupérer les contacts depuis le texte extrait.
- **Stockage en base de données** : Les contacts extraits sont enregistrés dans la base de données.  
  *(TODO : finaliser la configuration de la base de données)*
- **Vérification d'upload** : Endpoint `/check-upload/` pour vérifier que le fichier uploadé est bien un PDF.
- **Lecture des contacts** : Endpoint `/contacts/` pour récupérer les contacts stockés.

***

## Technologies utilisées

- [FastAPI](https://fastapi.tiangolo.com/) pour la construction de l'API.
- [Uvicorn](https://www.uvicorn.org/) comme serveur ASGI.
- [SQLAlchemy](https://www.sqlalchemy.org/) pour la gestion de la base de données *(configuration à compléter)*.
- [Python](https://www.python.org/) (version 3.8 ou supérieure).

***

## Installation

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/votre-username/pdf-uploader-api.git
   cd pdf-uploader-api
Créer et activer un environnement virtuel :

Sur Linux/Mac :

bash
Copier
Modifier
python -m venv venv
source venv/bin/activate
Sur Windows :

bash
Copier
Modifier
python -m venv venv
venv\Scripts\activate
Installer les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
Configuration de la base de données (TODO) :

Mettre en place votre base de données (ex : PostgreSQL, SQLite, MySQL, etc.).
Configurer les paramètres de connexion dans le fichier app/database.py.
Créer les tables nécessaires ou appliquer les migrations.
Démarrage de l'application
Pour démarrer l'API, utilisez Uvicorn :

bash
Copier
Modifier
uvicorn app.main:app --reload
L'application sera accessible à l'adresse : http://127.0.0.1:8000

Endpoints disponibles
1. Upload d'un fichier PDF
URL : /upload/

Méthode : POST

Description :
Permet d'uploader un fichier PDF. Le fichier est traité pour extraire le texte et les contacts, qui seront ensuite stockés en base de données.

Exemple de commande cURL :

bash
Copier
Modifier
curl -X 'POST' \
  'http://127.0.0.1:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@chemin/vers/votre-fichier.pdf;type=application/pdf'
2. Vérification de l'upload
URL : /check-upload/
Méthode : POST
Description :
Vérifie que le fichier uploadé est bien un PDF et retourne des informations sur le fichier (nom, type, taille).
3. Lecture des contacts
URL : /contacts/
Méthode : GET
Description :
Retourne la liste des contacts stockés dans la base de données.
Paramètres optionnels (Query Parameters) :
skip : Nombre de contacts à ignorer (pour la pagination).
limit : Nombre maximum de contacts à retourner.
Test de l'application
Utilisation de Swagger UI
FastAPI génère automatiquement une documentation interactive accessible via :

http://127.0.0.1:8000/docs

Vous pouvez tester tous les endpoints (upload, vérification, lecture des contacts) directement depuis cette interface en cliquant sur Try it out.

Test via cURL ou Postman
Upload d'un PDF :
Envoyez une requête POST sur l'URL /upload/ avec le fichier PDF en multipart/form-data.
Lecture des contacts :
Après avoir uploadé un PDF, envoyez une requête GET sur /contacts/ pour vérifier que les contacts ont été stockés correctement.
TODO
Mise en place de la base de données :
La configuration et le déploiement de la base de données (création des tables, migrations, etc.) restent à implémenter.
Tests unitaires :
Ajouter des tests unitaires pour valider l'extraction des contacts et leur stockage en base de données.
Amélioration de la validation :
Renforcer la validation des données extraites (par exemple, vérifier le format des emails, la présence de tous les champs requis, etc.).
Conclusion
Cette API permet d'extraire des contacts à partir de fichiers PDF et de les stocker pour une consultation ultérieure via une interface REST.
La prochaine étape sera de mettre en place et configurer correctement la base de données pour garantir la persistance des données.

N'hésitez pas à contribuer ou à signaler des problèmes !

lua
Copier
Modifier
    
