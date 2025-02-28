import os
from dotenv import load_dotenv
import pandas as pd
from langchain.docstore.document import Document
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# Load the Google API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

FILE_PATH = 'E:/Projet_IA_GENE/medical_chatbot/data/medquad.csv'      
df = pd.read_csv(FILE_PATH, sep=",")
df = df.dropna(subset=['question'])
df = df.fillna('')
"""    Preparation des objets Document pour LangChain
"""
docs = [
    Document(page_content=row['question'], 
             metadata={"answer": row['answer'], "source": row['source'],
                       "focus_area": row['focus_area']})
    for index, row in df.iterrows()
]

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(docs, embeddings)
""" sauvegarder l'index en local pour une utilisation ultérieure.
"""
vectorstore.save_local("faiss_index")
 