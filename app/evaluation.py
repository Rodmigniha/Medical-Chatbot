import os
from dotenv import load_dotenv
from sklearn.metrics import precision_score, recall_score, f1_score
from app import answer_quest  # Importer la fonction answer_quest de app.py

# Charger les variables d'environnement
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Évaluer le chatbot sur les questions de l'utilisateur
def evaluate_chatbot():
    # Demander à l'utilisateur de saisir ses questions
    print("Entrez vos questions (une par ligne). Tapez 'fin' pour terminer :")
    questions = []
    while True:
        question = input("Question : ")
        if question.lower() == 'fin':
            break
        questions.append(question)

    results = []

    for question in questions:
        # Utiliser la fonction answer_quest pour générer une réponse (sans enregistrement)
        reponse, docs, scores = answer_quest(question, enable_insert=False)
        
        if reponse:
            print(f"Question : {question}")
            print(f"Réponse générée : {reponse}")
            print(f"Sources ayant permis de répondre :")
            for i, doc in enumerate(docs):
                print(f"- Source: {doc.metadata['source']}, Focus Area: {doc.metadata['focus_area']}")
                print(f"  Score de similarité: {scores[i]:.4f}, Type de similarité: cosine")
            print("-" * 50)

            # Demander à l'utilisateur d'évaluer la réponse
            is_correct = input("La réponse est-elle correcte ? (oui/non) : ").strip().lower() == "oui"
            results.append(is_correct)
        else:
            print(f"Erreur : pas de réponse générée pour la question : {question}")

    # Calculer les métriques
    if results:
        precision = precision_score([1] * len(results), results)  # Toutes les réponses sont considérées comme positives
        recall = recall_score([1] * len(results), results)
        f1 = f1_score([1] * len(results), results)

        print(f"Précision: {precision:.2f}")
        print(f"Rappel: {recall:.2f}")
        print(f"F1-score: {f1:.2f}")
    else:
        print("Aucune réponse valide générée pour calculer les métriques.")

if __name__ == "__main__":
    evaluate_chatbot()