```markdown
# Medical Chatbot Project

## Description

Le **HealthGenie Chatbot** est une application interactive développée avec **Streamlit**, **FastAPI**, **LangChain**, et **Gemini** pour répondre à des questions spécifiques sur le domaine médical à partir de données issues du [dataset Kaggle LayoutLM](https://www.kaggle.com/datasets/jpmiller/layoutlm/data). Ce projet repose sur l'intégration de modèles avancés d'IA pour formuler des réponses précises et fournir des sources fiables.

### Objectifs

1. **Interface Chatbot avec Streamlit** : Développer une interface utilisateur intuitive permettant d'interagir avec un chatbot basé sur le modèle **LangChain** et les données médicales.
2. **Stockage des données dans Cloud SQL** : Créer une table dans **Cloud SQL** pour stocker les sources et autres informations pertinentes, telles que les zones de focus et les scores de similarité.
3. **Formulation des réponses** : Implémenter un mécanisme pour générer des réponses pertinentes à partir des questions posées, avec un score de similarité calculé à l'aide de **LangChain** et **Gemini**.
4. **Sources et Explication** : Fournir une liste des sources ayant permis de répondre à la question posée, incluant les éléments "source" et "focus_area".
5. **Déploiement sur Cloud Run** : Déployer l'application Streamlit sur **Google Cloud Run**, tout en respectant les bonnes pratiques de développement.
6. **Évaluation** : Implémenter un script `evaluation.py` pour tester l'efficacité du chatbot avec 10 exemples aléatoires du dataset.
7. **Originalité et Extension** : Bonus – Exploiter des fonctionnalités avancées comme LangGraph, LangFuse, ou le fine-tuning pour améliorer l'interaction et la pertinence des réponses.

### Technologies utilisées

- **Streamlit** : Pour la création de l'interface utilisateur interactive.
- **FastAPI** : Pour gérer l'API backend permettant l'interaction avec la base de données Cloud SQL.
- **LangChain** : Pour la gestion du flux de conversation et de l'intégration des modèles de langage afin de formuler des réponses appropriées.
- **Gemini** : Utilisé pour améliorer les capacités du chatbot en affinant les réponses et en utilisant des modèles IA avancés.
- **PostgreSQL (Cloud SQL)** : Pour stocker les données pertinentes comme les sources et les zones de focus utilisées pour répondre aux questions.
- **Docker & Docker Compose** : Pour gérer les services et le déploiement local, incluant la base de données et les services API.

### Déploiement sur Google Cloud Run

1. **Créez un compte Google Cloud** et activez les API nécessaires.
2. **Dockerisez l'application** en utilisant les fichiers `Dockerfile` pour Streamlit et FastAPI.
3. **Utilisez Cloud SQL** pour la gestion des données de la base PostgreSQL.
4. **Déployez sur Google Cloud Run** en utilisant les commandes appropriées.

### Structure du projet

- `Dockerfile`: Configuration pour déployer l'application Streamlit.
- `Dockerfile_api`: Configuration pour déployer l'API FastAPI.
- `docker-compose.yml`: Définition des services, y compris la base de données PostgreSQL, l'API FastAPI, et l'application Streamlit.
- `app/`: Contient l'ensemble du code source de l'application.
- `requirements.txt`: Liste des dépendances Python.
- `evaluation.py`: Script pour évaluer les performances du chatbot avec des exemples aléatoires.
- `.env`: Variables d'environnement pour la configuration (API keys, credentials).

### Évaluation du modèle

Le projet inclut une évaluation qui est exécutée via le script `evaluation.py`. Ce script teste le chatbot sur des exemples aléatoires et génère des métriques de performance.

### Instructions

1. **Clonez le repository**.

### 1. Cloner le dépôt
```bash
git clone https://github.com/Rodmigniha/Medical-Chatbot.git
cd Medical-Chatbot
```

2. a- **Installez les dépendances** 

```bash
pip install -r requirements.txt
```
2. b- Configurer les variables d'environnement
Créez un fichier `.env` à la racine du projet et ajoutez les informations suivantes :
```plaintext
GOOGLE_API_KEY=votre_google_api_key
DB_HOST=votre_host
DB_PORT=votre_port
DB_NAME=votre_db_name
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
```
Remplacez les valeurs par vos propres informations de connexion.

---

3. **Construisez les conteneurs Docker** avec `docker-compose build`.
4. **Exécutez les services localement** avec `docker-compose up`.
5. **Testez l'application Streamlit** en accédant à `http://localhost:8501`.

5. a- Ouvrez votre navigateur et accédez à l'URL affichée dans le terminal (généralement `http://localhost:8501`).  

5. b- Page d'accueil : Découvrez les fonctionnalités du chatbot et choisissez un mode dans la barre latérale.

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1.PNG)

5. c- Mode Assistance médicale : Posez une question dans le champ de texte et appuyez sur Entrée pour obtenir une réponse.

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1-assistant.PNG)

5. d- Mode Évaluation : Entrez plusieurs questions, évaluez les réponses générées, et consultez les métriques de performance (précision, rappel, F1-score).

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture2-evaluation.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture3-evaluation.PNG)

### Déploiement sur Cloud Run

Pour déployer sur Google Cloud Run, suivez ces étapes :
1. **Créez un projet Google Cloud** et activez les API Cloud Run et Cloud SQL.
2. **Déployez l'application** avec la commande `gcloud run deploy` après avoir configuré les variables d'environnement.
3. **Assurez-vous que l'application fonctionne correctement sur Cloud Run**.


## Auteurs

- **Lina THABET**
- **Rodrigue MIGNIHA**

📧 Contacts :
- linathabet101@gmail.com
- rodrigue.pro2020@gmail.com  - kidam.migniha@gmail.com