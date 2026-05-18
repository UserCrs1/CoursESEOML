# 💻 Cheat Sheet : L'arsenal du MLOps

Ce document regroupe toutes les commandes utiles pour survivre à ce TP. Gardez-le sous le coude !

---

## 🐧 WSL (Windows Subsystem for Linux)
> **Ce que c'est :** Un outil qui permet d'exécuter un véritable environnement Linux (comme Ubuntu) directement dans Windows, sans machine virtuelle lourde.

⚠️ **Règle d'or avec Docker sur Windows :** Travaillez toujours dans le système de fichiers Linux (allez dans votre dossier personnel avec `cd ~`) pour des performances optimales, et évitez les dossiers montés comme `/mnt/c/`.

* **Configurer Ubuntu par défaut** (si vous avez plusieurs distributions) :
    `wsl --set-default Ubuntu`
* **Lancer WSL** (ouvre votre distribution par défaut) :
    `wsl`
* **Lancer une distribution spécifique** :
    `wsl -d Debian`
* **Ouvrir l'explorateur Windows dans le dossier Linux actuel** :
    `explorer.exe .`

---

## 🐍 Venv (Environnement Virtuel Python)
> **Ce que c'est :** Une "bulle" isolée sur votre machine pour installer les bibliothèques Python de votre projet sans casser le reste de votre système.

* **Installer l'outil venv** (si ce n'est pas déjà fait sur votre Linux) :
    `sudo apt update`
    `sudo apt install python3-venv`
* **Créer l'environnement virtuel** (nommé .venv) :
    `python3 -m venv .venv`
* **Activer** (se connecter à) **l'environnement virtuel** :
    `source .venv/bin/activate`

---

## ⚡ API (FastAPI & Uvicorn)
> **Ce que c'est :** FastAPI est le code qui crée vos routes web. Uvicorn est le serveur web local qui fait tourner ce code et écoute les requêtes.

* **Installer les paquets nécessaires** (si absents du requirements.txt) :
    `pip install fastapi uvicorn`
* **Lancer le serveur API en local** :
    `uvicorn test:app --reload`
    (Explication : test est le nom de votre fichier test.py, app est l'objet FastAPI dans votre code. Le flag --reload redémarre le serveur à chaque fois que vous sauvegardez votre code).

* **Tester l'API** : Une fois lancé, ouvrez votre navigateur et allez sur :
    👉 http://localhost:8000/docs (Interface interactive générée automatiquement !).

---

## 🐳 Docker
> **Ce que c'est :** Un outil pour "empaqueter" votre application et ses dépendances afin qu'elle fonctionne partout de la même manière.

> **La métaphore** : L'image est un "gâteau congelé" (la recette figée). Le conteneur est le gâteau que l'on "décongèle" et qu'on consomme.

1. Manipuler le Modèle (Mission 1)
* **Créer l'image** (Préparer le gâteau congelé) :
    `docker build -t allocine-modele .`
    (-t allocine-modele = le nom que je donne à mon image).

* **Lancer le conteneur** (Décongeler le gâteau) :
    `docker run --rm -v "$(pwd)/../shared_model:/shared_model" allocine-modele`
    (Explications : --rm supprime le conteneur dès qu'il a fini son travail, très pratique pour un script de téléchargement. -v crée un Volume pour lier un dossier de votre PC au conteneur).

2. Manipuler l'API (Mission 3)
* **Créer l'image de l'API** :
    `docker build -t allocine-api .`
* **Lancer le conteneur de l'API** :
    `docker run -p 8000:8000 -v "$(pwd)/../shared_model:/shared_model" allocine-api`
    (Explications : -p 8000:8000 relie le port 8000 de votre PC au port 8000 du conteneur. Sans ça, l'API est injoignable).
3. Commandes Utiles
* **Voir toutes les images sur votre PC** :
    `docker images`
* **Voir les conteneurs en cours d'exécution** :
    `docker ps`

---

## 🎼 Docker Compose
> **Ce que c'est :** Le chef d'orchestre ! Il permet de lancer plusieurs conteneurs (ex: le récupérateur de modèle ET l'API) ensemble via un seul fichier de configuration.

* **Lancer toute l'infrastructure** (à exécuter dans le dossier contenant le docker-compose.yml) :
    `docker-compose up --build`
    (Le flag --build force Docker à recréer les images si vous avez modifié votre code).

---

## 🐙 Git
> **Ce que c'est :** L'outil de versioning par excellence pour sauvegarder, annuler et collaborer sur du code.

* **Récupérer le projet initial** :
    `git clone [https://github.com/UserCrs1/CoursESEOML.git](https://github.com/UserCrs1/CoursESEOML.git)`
* **Changer la destination** (repo) **pour pointer vers votre propre dépôt GitHub** :
    `git remote set-url origin <URL_DE_VOTRE_NOUVEAU_REPO>`
* **Mettre vos modifications dans "la boîte"** :
    `git add .`
* **Fermer la boîte et mettre une étiquette descriptive** :
    `git commit -m "Ajout des libs dans requirements.txt"`
* **Sauvegarder sur le cloud** (GitHub) :
    `git push`

---

## 🧹 Nettoyage (Faire place nette)
> Pour éviter que votre disque dur ne sature, voici comment tout supprimer.

### Docker (L'ordre compte : Supprimez les conteneurs AVANT les images)
* **Voir TOUS les conteneurs** (même ceux arrêtés) :
    `docker ps -a`
* **Supprimer un conteneur précis** :
    `docker rm <NOM_OU_ID_DU_CONTENEUR>`
* **Voir toutes les images** :
    `docker images`
* **Supprimer une image précise** :
    `docker rmi <NOM_OU_ID_DE_L_IMAGE>`

### WSL (Suppression radicale)
⚠️ Attention : Cela supprime la distribution Linux et TOUTES les données qu'elle contient. Aucune trace ne survivra.
* **Voir les distributions installées** :
    `wsl -l -v`
* **Supprimer** (désenregistrer) **une distribution** :
    `wsl --unregister Ubuntu`