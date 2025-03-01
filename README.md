### **Fichier `README.md`**

```markdown
# Chatbot Médical avec Streamlit, LangChain et Google Cloud

HealthGenie-Chatbot est un chatbot médical qui répond à des questions spécifiques en utilisant un dataset médical. Il est construit avec Streamlit, LangChain, et déployé sur Google Cloud.

## Fonctionnalités

- **Interface utilisateur** : Une interface simple et intuitive pour poser des questions et obtenir des réponses.
- **Recherche de similarité** : Utilisation de FAISS pour trouver les documents les plus pertinents.
- **Stockage des réponses** : Enregistrement des questions, réponses, sources, et scores de similarité dans une base de données PostgreSQL sur Google Cloud SQL.
- **Évaluation du chatbot** : Un script d'évaluation pour tester le chatbot sur des questions spécifiques.

## Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/Rodmigniha/Medical-Chatbot.git
   cd Medical-Chatbot
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez les variables d'environnement dans un fichier `.env` :
   ```plaintext
   GOOGLE_API_KEY=votre_google_api_key
   DB_HOST=votre_host
   DB_PORT=votre_port
   DB_NAME=votre_db_name
   DB_USER=votre_utilisateur
   DB_PASSWORD=votre_mot_de_passe
   ```

   Remplacez les valeurs par vos propres informations de connexion.

## Utilisation

### Lancer l'application Streamlit

1. Exécutez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```

2. Ouvrez votre navigateur et accédez à l'URL affichée dans le terminal (généralement `http://localhost:8501`).

3. Posez une question dans le champ de texte et appuyez sur Entrée pour obtenir une réponse.

### Évaluer le chatbot

1. Exécutez le script d'évaluation :
   ```bash
   python evaluation.py
   ```

2. Entrez vos questions (une par ligne). Tapez `fin` pour terminer.

3. Le script génère des réponses et vous demande d'évaluer leur exactitude.

4. Les métriques (précision, rappel, F1-score) sont affichées à la fin.

## Déploiement sur Google Cloud Run

1. Créez un fichier `Dockerfile` pour conteneuriser l'application :
   ```dockerfile
   FROM python:3.8-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
   ```

2. Construisez et poussez l'image Docker :
   ```bash
   gcloud builds submit --tag gcr.io/votre_project_id/medical-chatbot
   ```

3. Déployez sur Cloud Run :
   ```bash
   gcloud run deploy medical-chatbot --image gcr.io/votre_project_id/medical-chatbot --platform managed
   ```

4. Suivez les instructions pour configurer l'accès public et obtenir l'URL de déploiement.

## Structure du projet

- **`app.py`** : L'application Streamlit principale.
- **`db_utils.py`** : Les fonctions pour interagir avec la base de données PostgreSQL.
- **`evaluation.py`** : Le script d'évaluation du chatbot.
- **`requirements.txt`** : Les dépendances du projet.
- **`README.md`** : La documentation du projet.
- **`Dockerfile`** : Pour le déploiement sur Cloud Run.

## Métriques d'évaluation

Le chatbot est évalué sur les métriques suivantes :
- **Précision** : Proportion de réponses correctes parmi toutes les réponses générées.
- **Rappel** : Proportion de réponses correctes parmi toutes les questions posées.
- **F1-score** : Moyenne harmonique de la précision et du rappel.


## Auteur

- Lina THABET
- Rodrigue MIGNIHA
- Contact : linathabet101@gmail.com - rodrigue.pro2020@gmail.com - kidam.migniha@gmail.com



