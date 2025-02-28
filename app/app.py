import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS


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

def main():
    st.title("Chatbot IA GENE & GCP")
    
    # Charger le vectorstore et le modèle Gemini
    vectorstore = load_vectorstore()
    llm = load_llm()
    prompt = create_prompt()
    
    # Interface utilisateur
    question = st.text_input("Posez votre question:")
    
    if question:
        # Rechercher les documents les plus similaires
        docs = vectorstore.similarity_search(question, k=3)  
        context = "\n".join([doc.page_content for doc in docs]) 
        
        # Formater le prompt avec la question et le contexte
        formatted_prompt = prompt.format_messages(question=question,
                                                  context=context)
        
        # Interroger Gemini via LangChain pour obtenir une réponse
        ai_msg = llm.invoke(formatted_prompt)
        
        # Vérifier si le message renvoyé par Gemini contient la réponse
        if hasattr(ai_msg, 'content'):
            reponse = ai_msg.content
            st.write("Réponse:", reponse)
            
            # Afficher les sources et focus_area
            st.write("Sources ayant permis de répondre :")
            for doc in docs:
                st.write(f"- Source: {doc.metadata['source']}, Focus Area: {doc.metadata['focus_area']}")
        else:
            st.write("Erreur : la réponse générée ne contient pas de texte valide.")

if __name__ == "__main__":
    main()

