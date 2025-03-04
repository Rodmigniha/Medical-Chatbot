FROM python:3.11-slim

WORKDIR /app

# Copier d'abord les fichiers nécessaires à l'installation des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste de l'application
COPY . .

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Lancer Streamlit avec les paramètres nécessaires
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
