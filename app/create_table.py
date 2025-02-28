from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Configuration de la connexion à Cloud SQL
DATABASE_URI = 'mysql+pymysql://user:password@ip_address/db_name'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

# Définition de la table
questions_table = Table(
    'questions', metadata,
    Column('id', Integer, primary_key=True),
    Column('question', String(255)),
    Column('answer', String(255)),
    Column('source', String(255)),
    Column('focus_area', String(255))
)

# Création de la table
metadata.create_all(engine)