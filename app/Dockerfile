FROM python:3.11-slim

WORKDIR /app

# Copier d'abord les fichiers nécessaires à l'installation des dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste de l'application
COPY . .

# Exposer le port 8080 pour Cloud Run
EXPOSE 8080

# Lancer Streamlit en le forçant à écouter sur 0.0.0.0 et le port 8080
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
