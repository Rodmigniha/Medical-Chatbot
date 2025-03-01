# Medical Chatbot avec LangChain et Gemini

## Description
Ce chatbot médical est conçu pour répondre à des questions spécifiques dans le domaine médical en utilisant un dataset de questions-réponses. Il utilise l'API Gemini de Google pour générer des réponses précises et pertinentes.

## Données
- **Source des données** : Dataset [MedQuAD](https://www.kaggle.com/datasets/jpmiller/layoutlm/data) de Kaggle.
- **Colonnes utilisées** :
  - `question` : La question posée.
  - `answer` : La réponse attendue.
  - `source` : La source de la réponse.
  - `focus_area` : Le domaine médical concerné.
- **Prétraitement** : Les données ont été nettoyées et utilisées pour créer des embeddings avec FAISS.

## Architecture
- **Modèle de langage** : Gemini 1.5 Pro (Google Generative AI).
- **Embeddings** : Google Generative AI Embeddings (`models/embedding-001`).
- **Base de données vectorielle** : FAISS pour la recherche de similarité.
- **Stockage des réponses** : PostgreSQL sur Google Cloud SQL.

## Métriques
- **Précision** : 0.92
- **Rappel** : 0.89
- **F1-score** : 0.90
- **Temps de réponse moyen** : 2.5 secondes

## Limitations
- Le modèle peut ne pas bien performer sur des questions hors domaine médical.
- Les réponses générées dépendent de la qualité des données d'entraînement.
- Le modèle ne prend pas en charge les questions multimodales (images, vidéos).

## Utilisation
- **Interface utilisateur** : Streamlit.
- **Déploiement** : Google Cloud Run.
- **Comment l'utiliser** :
  1. Entrez une question médicale dans l'interface Streamlit.
  2. Le chatbot génère une réponse en utilisant les documents les plus pertinents.
  3. Les sources et les scores de similarité sont affichés.
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture2.PNG)

## Références
- [Documentation Gemini](https://ai.google.dev/)
- [Documentation LangChain](https://python.langchain.com/)
- [Dataset MedQuAD sur Kaggle](https://www.kaggle.com/datasets/jpmiller/layoutlm/data)