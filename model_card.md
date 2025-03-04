# HealthGenie Chatbot

## Description
Le **HealthGenie Chatbot** est conçu pour fournir des réponses médicales précises à partir d'un dataset spécifique. Utilisant les modèles avancés de **LangChain** et **Gemini**, il génère des réponses de haute qualité en se basant sur un ensemble de données questions-réponses provenant du [dataset Kaggle LayoutLM](https://www.kaggle.com/datasets/jpmiller/layoutlm/data). L'application est déployée sur **Google Cloud Run** pour un accès facile et une interaction fluide avec les utilisateurs.

## Données
- **Source des données** : Dataset [MedQuAD](https://www.kaggle.com/datasets/jpmiller/layoutlm/data) de Kaggle.
- **Colonnes utilisées** :
  - `question` : La question posée.
  - `answer` : La réponse attendue.
  - `source` : La source de la réponse.
  - `focus_area` : Le domaine médical concerné.
- **Prétraitement** : Les données sont nettoyées et transformées pour créer des embeddings via **FAISS**, facilitant ainsi la recherche de similarité.

## Architecture
- **Modèle de langage** : **Gemini 1.5 Pro** (Google Generative AI).
- **Embeddings** : Embeddings générés par **Google Generative AI** (`models/embedding-001`).
- **Base de données vectorielle** : **FAISS** pour l'indexation des embeddings et la recherche de similarité.
- **Stockage des réponses** : **PostgreSQL** sur **Google Cloud SQL** pour stocker les informations de réponse et les sources.

## Métriques
- **Précision** : 0.92
- **Rappel** : 0.89
- **F1-score** : 0.90
- **Temps de réponse moyen** : 2.5 secondes

## Limitations
- Performances dégradées pour des questions hors du domaine médical.
- Qualité des réponses dépendante des données d'entraînement.
- Pas de support pour les questions multimodales (images, vidéos).

## Utilisation
- **Interface utilisateur** : **Streamlit** pour une interface interactive facile d’utilisation.
- **Déploiement** : L'application est déployée sur **Google Cloud Run** pour une utilisation accessible à distance.
- **Étapes d'utilisation** :
  1. Entrez une question médicale dans l'interface Streamlit.
  2. Le chatbot génère une réponse en sélectionnant les documents les plus pertinents.
  3. Les sources et les scores de similarité sont affichés pour plus de transparence.

![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture1-assistant.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture2-evaluation.PNG)
![Dashboard boxplot](https://github.com/Rodmigniha/Medical-Chatbot/blob/main/data/Capture3-evaluation.PNG)

## Références
- [Documentation Gemini](https://ai.google.dev/)
- [Documentation LangChain](https://python.langchain.com/)
- [Dataset MedQuAD sur Kaggle](https://www.kaggle.com/datasets/jpmiller/layoutlm/data)
