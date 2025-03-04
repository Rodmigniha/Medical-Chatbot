# Medical Chatbot Project

## Description

Le **HealthGenie Chatbot** est une application interactive d'assistance médicale développée avec **Streamlit**, **FastAPI**, **LangChain**, et **Gemini**. Il permet de répondre à des questions médicales spécifiques à partir des données issues du [dataset Kaggle LayoutLM](https://www.kaggle.com/datasets/jpmiller/layoutlm/data). Ce projet repose sur l'intégration de modèles avancés d'IA afin de formuler des réponses précises et fournir des sources fiables.

## Objectifs

1. **Interface Chatbot avec Streamlit** : Développer une interface utilisateur intuitive pour interagir avec un chatbot médical basé sur **LangChain** et les données médicales.
2. **Stockage des données dans Cloud SQL** : Utiliser **Cloud SQL** pour stocker les sources et autres informations pertinentes, telles que les zones de focus et les scores de similarité.
3. **Formulation des réponses** : Générer des réponses pertinentes avec **LangChain** et **Gemini**, tout en calculant un score de similarité.
4. **Affichage des sources** : Présenter les sources ayant contribué aux réponses, incluant les éléments "source" et "focus_area".
5. **Déploiement sur Cloud Run** : Déployer l'application Streamlit sur **Google Cloud Run**, en respectant les bonnes pratiques de développement.
6. **Évaluation** : Implémenter `evaluation.py` pour tester l'efficacité du chatbot avec des exemples aléatoires du dataset.
7. **Optimisation et Extension** : Bonus – Ajouter des fonctionnalités avancées comme **LangGraph, LangFuse**, ou un **fine-tuning** du modèle pour améliorer la pertinence des réponses.

## Technologies utilisées

- **Streamlit** : Interface utilisateur interactive.
- **FastAPI** : API backend pour l'interaction avec la base de données Cloud SQL.
- **LangChain** : Gestion du flux de conversation et formulation des réponses.
- **Gemini** : Modèle IA avancé pour améliorer la pertinence des réponses.
- **PostgreSQL (Cloud SQL)** : Base de données pour stocker les sources et métadonnées des réponses.
- **Google Cloud Run** : Déploiement de l'application.
- **Docker & Docker Compose** : Gestion des services et déploiement local.

## Structure du projet

- `app/` : Code source de l'application.
- `Dockerfile` : Configuration pour déployer Streamlit.
- `Dockerfile_api` : Configuration pour FastAPI.
- `docker-compose.yml` : Services incluant PostgreSQL, FastAPI et Streamlit.
- `requirements.txt` : Liste des dépendances Python.
- `evaluation.py` : Script d'évaluation du chatbot.
- `.env` : Variables d'environnement (API keys, credentials).
- `embed_vstor.py` : Script pour générer l'index FAISS à partir des données médicales.

## Instructions d'installation et d'utilisation

### 1. Cloner le dépôt

```bash
git clone --branch version-fastapi https://github.com/Rodmigniha/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet et ajoutez les informations suivantes :

```plaintext
GOOGLE_API_KEY=votre_google_api_key
DB_HOST=votre_host
DB_PORT=votre_port
DB_NAME=votre_db_name
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
```

### 4. Première utilisation : Génération de l'index FAISS

Avant de lancer l'application, exécutez `embed_vstor.py` pour générer l'index FAISS localement :

```bash
python app/embed_vstor.py
```

Le fichier **faiss_index** généré doit être placé dans le répertoire `app/` pour assurer son bon fonctionnement.

### 5. Construire et exécuter les conteneurs Docker

```bash
docker-compose build
docker-compose up
```

### 6. Accéder à l'application

Ouvrez votre navigateur et rendez-vous sur `http://localhost:8501`.

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1-assistant.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture2-evaluation.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture3-evaluation.PNG)

## Déploiement sur Google Cloud Run

1. **Créer un projet Google Cloud** et activer les API Cloud Run et Cloud SQL.
2. **Déployer l'application** avec `gcloud run deploy` après avoir configuré les variables d'environnement.
3. **Vérifier le bon fonctionnement** de l'application sur Cloud Run.

## Évaluation du modèle

Le projet inclut un script `evaluation.py` pour tester les performances du chatbot en générant des métriques de précision et de pertinence.

## Auteurs

- **Lina THABET**
- **Rodrigue MIGNIHA**

📧 Contacts :
- linathabet101@gmail.com
- rodrigue.pro2020@gmail.com | kidam.migniha@gmail.com

