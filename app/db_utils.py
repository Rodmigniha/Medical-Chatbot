import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql


# Charger les variables d'environnement
load_dotenv()

# Configuration de la base de données
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_to_db():
    """Établir une connexion à la base de données PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None

def insert_into_rm_med_table(question, answer, source, focus_area, similarity_score, similarity_type):
    """Insérer un document dans la table 'rm_med_table'."""
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            query = sql.SQL("""
                INSERT INTO rm_med_table (question, answer, source, focus_area, similarity_score, similarity_type)
                VALUES (%s, %s, %s, %s, %s, %s)
            """)
            # Convertir numpy.float32 en float
            similarity_score_float = float(similarity_score)
            print(f"Tentative d'insertion : {question}, {answer}, {source}, {focus_area}, {similarity_score_float}, {similarity_type}")
            cur.execute(query, (question, answer, source, focus_area, similarity_score_float, similarity_type))
            conn.commit()
            print("Données enregistrées avec succès dans la base de données.")
        except Exception as e:
            print(f"Erreur lors de l'insertion des données : {e}")
        finally:
            cur.close()
            conn.close()

def fetch_from_rm_med_table():
    """Récupérer tous les enregistrements de la table 'rm_med_table'."""
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM rm_med_table")
            results = cur.fetchall()
            return results
        except Exception as e:
            print(f"Erreur lors de la récupération des données : {e}")
            return []
        finally:
            cur.close()
            conn.close()

