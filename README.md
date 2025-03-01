# Chatbot Médical avec Streamlit, LangChain et Google Cloud

**HealthGenie-Chatbot** est un chatbot médical avancé permettant de répondre à des questions médicales à partir d'un dataset spécialisé. Il est construit avec **Streamlit**, **LangChain**, et déployé sur **Google Cloud**.

## Fonctionnalités

- **Interface utilisateur intuitive** : Interface simple pour poser des questions et obtenir des réponses.
- **Recherche de similarité** : Utilisation de **FAISS** pour indexer et retrouver les documents pertinents.
- **Stockage des réponses** : Sauvegarde des questions, réponses, sources et scores de similarité dans **PostgreSQL (Google Cloud SQL)**.
- **Évaluation du chatbot** : Script d'évaluation pour tester la pertinence des réponses fournies.

---

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/Rodmigniha/Medical-Chatbot.git
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
Remplacez les valeurs par vos propres informations de connexion.

---

## Utilisation

### Lancer l'application Streamlit
Voici la section mise à jour de ton `README.md` avec l'ajout des instructions pour `embed_vstor.py` :  

---

## Utilisation  

### Première utilisation  

Avant de lancer l'application, il est nécessaire de générer et stocker l'index FAISS localement. Pour cela :  

1. Exécutez le script `embed_vstor.py` afin de générer l'index des embeddings :  
   ```bash
   python embed_vstor.py
   ```  
   
2. Un dossier `faiss_index` sera créé après l'exécution. Déplacez ce dossier dans le répertoire `app` :  
   ```bash
   mv faiss_index app/
   ```  

### Lancer l'application Streamlit  

1. Exécutez l'application Streamlit :  
   ```bash
   streamlit run app.py
   ```  

2. Ouvrez votre navigateur et accédez à l'URL affichée dans le terminal (généralement `http://localhost:8501`).  

3. Posez une question dans le champ de texte et appuyez sur Entrée pour obtenir une réponse.  

### Exemples

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1.PNG)

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture2.PNG)


### Évaluer le chatbot
1. Exécutez le script d'évaluation :
   ```bash
   python evaluation.py
   ```
2. Entrez vos questions (une par ligne). Tapez `fin` pour terminer.
3. Analyse automatique des réponses et calcul des métriques d'évaluation.

---

## Déploiement sur Google Cloud Run

### 1. Création du `Dockerfile`
```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
```

### 2. Construire et pousser l'image Docker
```bash
gcloud builds submit --tag gcr.io/votre_project_id/medical-chatbot
```

### 3. Déployer l'application sur Cloud Run
```bash
gcloud run deploy medical-chatbot --image gcr.io/votre_project_id/medical-chatbot --platform managed
```
Suivez les instructions pour configurer l'accès public et obtenir l'URL de déploiement.

---

## Structure du projet

```
Medical-Chatbot/
│-- app.py            # Application Streamlit
│-- db_utils.py       # Fonctions d'interaction avec PostgreSQL
│-- evaluation.py     # Script d'évaluation du chatbot
│-- requirements.txt  # Liste des dépendances
│-- README.md         # Documentation du projet
│-- Dockerfile        # Fichier pour déploiement sur Cloud Run
│-- .env.example      # Exemple de fichier d'environnement
```

---

## Métriques d'évaluation

Le chatbot est évalué selon les critères suivants :
- **Précision** : Proportion de réponses correctes parmi toutes les réponses générées.
- **Rappel** : Proportion de réponses correctes parmi toutes les questions posées.
- **F1-score** : Moyenne harmonique de la précision et du rappel.

---

## Auteurs

- **Lina THABET**
- **Rodrigue MIGNIHA**

📧 Contacts :
- linathabet101@gmail.com
- rodrigue.pro2020@gmail.com
- kidam.migniha@gmail.com

