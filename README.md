# 🚀 TP MLOps : Déploiement et Conteneurisation d'un Modèle

Bienvenue dans ce TP d'introduction au MLOps ! L'objectif de cette session est de vous apprendre à franchir le pont entre la création d'un modèle de Machine Learning et sa mise en production. Vous allez transformer un modèle d'IA (Analyse de sentiment Allociné) en un véritable service web, autonome et robuste.

---

## 🛠️ Étape Préalable : Préparation de l'Environnement

Avant de vous lancer dans les missions, vous devez préparer votre espace de travail.

**Installation des dépendances :** > ⚠️ **IMPORTANT :** N'oubliez pas d'installer les bibliothèques Python nécessaires dans votre environnement virtuel (`venv` ou `.env`) avant de lancer les tests ou le script de téléchargement.

---

## 🎯 Les Missions
### Mission 1 : Le Récupérateur (Dockerfile & build_model.py)
* **Objectif :** Isoler le téléchargement du modèle dans un conteneur dédié.
* **Description :** Pour éviter de retélécharger le modèle à chaque démarrage de l'API, vous allez utiliser le script `build_model.py`. Votre mission est de créer un premier `Dockerfile` qui exécute ce script afin de télécharger et stocker le modèle `tf-allocine` de Hugging Face.

### Mission 2 : Le Serveur en Salle (FastAPI)
* **Objectif :** Créer et tester votre API RESTful en local.
* **Description :** Tel un serveur de restaurant, votre application va jouer les intermédiaires. Développez votre API avec FastAPI pour qu'elle reçoive des critiques de films (au format JSON), utilise le modèle pour prédire s'il s'agit d'un avis positif ou négatif, et renvoie la réponse. Testez-la d'abord sur votre machine !

### Mission 3 : La Mise en Boîte (Dockerfile & main.py)
* **Objectif :** Conteneuriser votre application FastAPI.
* **Description :** "Ça marche sur ma machine !" – Pour éviter cette fameuse phrase, rédigez un second `Dockerfile` dédié à votre fichier `main.py`. C'est la recette qui indique à Docker comment construire l'environnement de votre API de A à Z (OS de base, dépendances, code source).

### Mission 4 : Le Multivers (Docker Compose & Volumes)
* **Objectif :** Orchestrer l'ensemble de votre infrastructure.
* **Description :** Les applications modernes sont un assemblage de plusieurs services. Utilisez un fichier `docker-compose.yml` pour lancer vos conteneurs ensemble.
Vous devrez impérativement utiliser les Volumes Docker pour que le modèle téléchargé par la Mission 1 soit partagé et accessible par l'API de la Mission 3 !


---

## 📚 Vos ressources de survie (À lire en cas de blocage)

### 🧠 Le Modèle & IA
* **Modèle TF-Allociné :** Documentation du modèle utilisé pour l'analyse de sentiments.
  👉 [Fiche Hugging Face - tf-allocine](https://huggingface.co/tblard/tf-allocine)
* **Hugging Face (`pipeline`) :** Comment charger facilement le modèle ?
  👉 [Doc officielle de la fonction pipeline](https://huggingface.co/docs/transformers/main_classes/pipelines)

### ⚡ FastAPI
* **Body & Pydantic :** Comment valider les données entrantes (JSON) ?
  👉 [Tutoriel FastAPI - Body (Pydantic)](https://fastapi.tiangolo.com/tutorial/body/)

### 🐳 Docker & Docker Compose
* **Dockerfile Reference :** Pour trouver chaque instruction (`FROM`, `COPY`, `RUN`...).
  👉 [Docker Builder Documentation](https://docs.docker.com/engine/reference/builder/)
* **Docker Volumes :** Comprendre comment partager des fichiers entre l'hôte et le conteneur.
  👉 [Documentation Docker Volumes](https://docs.docker.com/storage/volumes/)
* **Docker Compose (`depends_on`) :** Gérer l'ordre de démarrage des services.
  👉 [Doc Docker Compose - depends_on](https://docs.docker.com/compose/compose-file/05-services/#depends_on)

### 📖 Support de cours
* **Cours MLOps :** Les bases du MLOps.
  👉 [Support MLOps](https://fromsmash.com/Formation-ESEO-MLOps1)
* **Cours DevOps :** Les bases du DevOps.
  👉 [Support DevOps](https://fromsmash.com/Formation-ESEO-DevOps1)

---
*Bon code et bonne chance pour ce déploiement !* 👩‍💻👨‍💻
