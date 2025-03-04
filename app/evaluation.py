import streamlit as st
from sklearn.metrics import precision_score, recall_score, f1_score
import requests

# URL de l'API FastAPI
API_URL = "https://rm-api-medical-1021317796643.europe-west1.run.app/ask" # decommenter après deploiement de FastAPI

def ask_question_via_api(question):
    """Envoie une question à l'API FastAPI et retourne la réponse."""
    try:
        #response = requests.post(f"http://fastapi-container:8080/ask", json={"question": question}) # Commenter après deploiement de FastAPI
        response = requests.post(API_URL, json={"question": question}) # decommenter après deploiement de FastAPI
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Erreur de l'API : {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {e}")
        return None

def evaluation_mode():
    """Mode évaluation : testez le chatbot en évaluant ses réponses."""
    st.title("HealthGenie Chatbot - Mode Évaluation")

    st.write("### Mode Évaluation")
    st.write("Entrez vos questions ci-dessous pour évaluer les réponses du chatbot.")

    # Initialisation de l'état de session
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'responses' not in st.session_state:
        st.session_state.responses = []
    if 'evaluations' not in st.session_state:
        st.session_state.evaluations = []
    if 'show_metrics' not in st.session_state:
        st.session_state.show_metrics = False

    # Saisie des questions par l'utilisateur
    questions_input = st.text_area("Entrez vos questions (une par ligne) :")

    # Bouton pour générer les réponses
    if st.button("Générer les réponses"):
        st.session_state.questions = [q.strip() for q in questions_input.split('\n') if q.strip()]
        st.session_state.responses = []
        st.session_state.show_metrics = False

        for question in st.session_state.questions:
            result = ask_question_via_api(question)
            if result:
                st.session_state.responses.append({
                    "question": question,
                    "reponse": result["response"],
                    "sources": result["sources"],
                    "scores": result["scores"]
                })
            else:
                st.session_state.responses.append({
                    "question": question,
                    "reponse": None,
                    "sources": [],
                    "scores": []
                })

        # Ne pas réinitialiser `evaluations` mais l'ajuster
        while len(st.session_state.evaluations) < len(st.session_state.responses):
            st.session_state.evaluations.append(None)

    # Affichage des réponses et évaluations
    if st.session_state.responses:
        st.write("### Réponses générées")

        for i, response in enumerate(st.session_state.responses):
            st.write(f"**Question :** {response['question']}")
            if response['reponse']:
                st.write(f"**Réponse générée :** {response['reponse']}")
                st.write("**Sources ayant permis de répondre :**")

                for j, source in enumerate(response["sources"]):  # `j` au lieu de `i`
                    st.write(f"- Source: {source['source']}, Focus Area: {source['focus_area']}")
                    st.write(f"  Score de similarité: {response['scores'][j]:.4f}, Type de similarité: cosine")

                # Assurer une évaluation correcte
                evaluation = st.radio(
                    f"La réponse à la question est-elle correcte ?",
                    ("Oui", "Non"),
                    index=0 if st.session_state.evaluations[i] is None else (0 if st.session_state.evaluations[i] == 1 else 1),
                    key=f"eval_{i}_{response['question']}"  # Correction du key
                )

                st.session_state.evaluations[i] = 1 if evaluation == "Oui" else 0
            else:
                st.write("Erreur : pas de réponse générée pour cette question.")
            st.write("-" * 50)

        # Bouton pour calculer les métriques
        if st.button("Calculer les métriques"):
            if all(eval is not None for eval in st.session_state.evaluations):
                st.session_state.show_metrics = True
            else:
                st.warning("Veuillez évaluer toutes les réponses avant de calculer les métriques.")

    # Affichage des métriques
    if st.session_state.show_metrics and st.session_state.evaluations:
        st.write("### Résultats de l'évaluation")

        precision = precision_score([1] * len(st.session_state.evaluations), st.session_state.evaluations)
        recall = recall_score([1] * len(st.session_state.evaluations), st.session_state.evaluations)
        f1 = f1_score([1] * len(st.session_state.evaluations), st.session_state.evaluations)

        st.write(f"**Précision :** {precision:.2f}")
        st.write(f"**Rappel :** {recall:.2f}")
        st.write(f"**F1-score :** {f1:.2f}")
