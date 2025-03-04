import streamlit as st
import requests

# URL de l'API FastAPI
API_URL = "https://rm-api-medical-1021317796643.europe-west1.run.app/ask" # decommenter après deploiement de FastAPI

def ask_question_via_api(question):
    """
    Envoie une question à l'API FastAPI et retourne la réponse.
    """
    try:
        # Envoyer une requête POST à l'API
        #response = requests.post(f"http://fastapi-container:8080/ask", json={"question": question}) # Commenter après deploiement de FastAPI
        response = requests.post(API_URL, json={"question": question}) # decommenter après deploiement de FastAPI
        if response.status_code == 200:
            return response.json()  # Retourner la réponse JSON
        else:
            st.error(f"Erreur de l'API : {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {e}")
        return None

def chatbot_mode():
    """
    Mode chatbot : assistance médicale.
    """
    st.title("HealthGenie Chatbot - Mode Assistance")
    
    # Interface utilisateur
    question = st.text_input("Posez votre question:")
    
    if question:
        # Envoyer la question à l'API et obtenir la réponse
        result = ask_question_via_api(question)
        if result:
            st.write("Réponse:", result["response"])
            st.write("Sources ayant permis de répondre :")
            for i, source in enumerate(result["sources"]):
                st.write(f"- Source: {source['source']}, Focus Area: {source['focus_area']}")
                st.write(f"  Score de similarité: {result['scores'][i]:.4f}, Type de similarité: cosine")


if __name__ == "__main__":
    chatbot_mode()