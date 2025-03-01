import streamlit as st
from db_utils import insert_into_rm_med_table
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Charger le vectorstore FAISS
def load_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.load_local("faiss_index", embeddings, 
                                   allow_dangerous_deserialization=True)
    return vectorstore

# Initialiser le modèle Gemini
def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

# Définir le prompt
def create_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "Tu es un assistant pour les tâches de questions-réponses. Utilise les\
            éléments de contexte sur les documents pour répondre à la question. Sois concis. Pour répondre, \
            tu vas fournir l'exact réponse 'answer' correspondant à la question, et en plus, \
            tu vas afficher les sources ayant permis de répondre à la question. \
            Pour chaque source : Les éléments 'source' et 'focus_area' doivent être présents."),
        ("human", "Question: {question}"),
        ("human", "Context: {context}"),
        ("ai", "Answer:"),
    ])

def answer_quest(question, enable_insert=True):
    """Répond à une question en utilisant le modèle Gemini et retourne la réponse, les documents et les scores.
    
    Args:
        question (str): La question à poser.
        enable_insert (bool): Si True, les résultats sont enregistrés dans la base de données. Par défaut, True.
    
    Returns:
        tuple: (reponse, docs, scores) ou (None, None, None) en cas d'erreur.
    """
    # Charger le vectorstore et le modèle Gemini
    vectorstore = load_vectorstore()
    llm = load_llm()
    prompt = create_prompt()
    
    # Rechercher les documents les plus similaires avec leurs scores
    docs_with_scores = vectorstore.similarity_search_with_score(question, k=3)  # k=3 pour les 3 meilleurs résultats
    
    # Extraire les documents et les scores
    docs = [doc for doc, score in docs_with_scores]
    scores = [score for doc, score in docs_with_scores]
    
    # Concaténer le contexte des documents
    context = "\n".join([doc.page_content for doc in docs]) 
    
    # Formater le prompt avec la question et le contexte
    formatted_prompt = prompt.format_messages(question=question, context=context)
    
    # Interroger Gemini via LangChain pour obtenir une réponse
    ai_msg = llm.invoke(formatted_prompt)
    
    # Vérifier si le message renvoyé par Gemini contient la réponse
    if hasattr(ai_msg, 'content'):
        reponse = ai_msg.content
        st.write("Réponse:", reponse)
        
        # Afficher les sources, focus_area et les scores de similarité
        st.write("Sources ayant permis de répondre :")
        for i, doc in enumerate(docs):
            st.write(f"- Source: {doc.metadata['source']}, Focus Area: {doc.metadata['focus_area']}")
            st.write(f"  Score de similarité: {scores[i]:.4f}, Type de similarité: cosine")
            
        # Enregistrer dans la table rm_med_table si enable_insert est True
        if enable_insert:
            for i, doc in enumerate(docs):
                insert_into_rm_med_table(
                    question=question,
                    answer=reponse,
                    source=doc.metadata['source'],
                    focus_area=doc.metadata['focus_area'],
                    similarity_score=scores[i],
                    similarity_type="cosine"
                )
        
        return reponse, docs, scores
    else:
        st.write("Erreur : la réponse générée ne contient pas de texte valide.")
        return None, None, None

def chatbot_mode():
    """Mode chatbot : assistance médicale."""
    st.title("HealthGenie Chatbot - Mode Assistance")
    
    # Interface utilisateur
    question = st.text_input("Posez votre question:")
    
    if question:
        answer_quest(question)  # enable_insert est True par défaut