import os

DB_PORT = "5432"
DB_NAME = "gen_ai_db"
DB_USER = "students"

if "CLOUD_RUN" in os.environ:
    # Connexion sur Cloud Run via Cloud SQL Auth Proxy
    DB_HOST = "/cloudsql/dauphine-437611:europe-west1:gen-ai-instance"
else:
    # Connexion en local
    DB_HOST = "127.0.0.1"
    #DB_HOST=db


