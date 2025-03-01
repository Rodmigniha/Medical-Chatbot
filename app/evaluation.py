import streamlit as st
from sklearn.metrics import precision_score, recall_score, f1_score
from app import answer_quest  # Importer la fonction answer_quest de app.py

def evaluation_mode():
    """Mode évaluation : testez le chatbot en évaluant ses réponses."""
    st.title("HealthGenie Chatbot - Mode Évaluation")
    
    st.write("""
    ### Mode Évaluation
    Entrez vos questions ci-dessous pour évaluer les réponses du chatbot.
    """)
    
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
        st.session_state.evaluations = []
        st.session_state.show_metrics = False
        
        # Générer les réponses pour chaque question
        for question in st.session_state.questions:
            reponse, docs, scores = answer_quest(question, enable_insert=False)
            if reponse:
                st.session_state.responses.append({
                    "question": question,
                    "reponse": reponse,
                    "sources": docs,
                    "scores": scores
                })
            else:
                st.session_state.responses.append({
                    "question": question,
                    "reponse": None,
                    "sources": [],
                    "scores": []
                })
    
    # Afficher les réponses et collecter les évaluations
    if st.session_state.responses:
        st.write("### Réponses générées")
        
        for i, response in enumerate(st.session_state.responses):
            st.write(f"**Question :** {response['question']}")
            if response['reponse']:
                st.write(f"**Réponse générée :** {response['reponse']}")
                st.write("**Sources ayant permis de répondre :**")
                for j, doc in enumerate(response['sources']):
                    st.write(f"- Source: {doc.metadata['source']}, Focus Area: {doc.metadata['focus_area']}")
                    st.write(f"  Score de similarité: {response['scores'][j]:.4f}, Type de similarité: cosine")
                
                # Évaluation de l'utilisateur
                if len(st.session_state.evaluations) <= i:
                    st.session_state.evaluations.append(None)  # Initialiser l'évaluation
                
                evaluation = st.radio(
                    f"La réponse à la question '{response['question']}' est-elle correcte ?",
                    ("Oui", "Non"),
                    index=0 if st.session_state.evaluations[i] is None else (0 if st.session_state.evaluations[i] == 1 else 1),
                    key=f"eval_{i}"
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
    
    # Afficher les métriques si elles sont disponibles
    if st.session_state.show_metrics and st.session_state.evaluations:
        st.write("### Résultats de l'évaluation")
        
        # Calculer les métriques
        precision = precision_score([1] * len(st.session_state.evaluations), st.session_state.evaluations)
        recall = recall_score([1] * len(st.session_state.evaluations), st.session_state.evaluations)
        f1 = f1_score([1] * len(st.session_state.evaluations), st.session_state.evaluations)

        st.write(f"**Précision:** {precision:.2f}")
        st.write(f"**Rappel:** {recall:.2f}")
        st.write(f"**F1-score:** {f1:.2f}")