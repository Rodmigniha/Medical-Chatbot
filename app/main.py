import streamlit as st
from app import chatbot_mode
from evaluation import evaluation_mode

def main():
    """Fonction principale pour gérer les pages."""
    st.sidebar.title("HealthGenie Chatbot")
    st.sidebar.write("Choisissez un mode :")
    
    # Boutons de navigation
    mode = st.sidebar.radio("Mode", ("Accueil", "Chatbot", "Évaluation"))
    
    if mode == "Accueil":
        st.title("Bienvenue sur HealthGenie Chatbot")
        st.write("""
        **HealthGenie Chatbot** est une application conçue pour répondre à vos questions médicales en utilisant des technologies avancées d'IA.
        
        ### Fonctionnalités :
        - **Mode Assistance** : Posez des questions médicales et obtenez des réponses précises.
        - **Mode Évaluation** : Testez le chatbot en évaluant ses réponses.
        
        ### Comment utiliser :
        1. Sélectionnez un mode dans la barre latérale.
        2. Suivez les instructions à l'écran.
        """)
    
    elif mode == "Chatbot":
        chatbot_mode()
    
    elif mode == "Évaluation":
        evaluation_mode()

if __name__ == "__main__":
    main()