from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core import answer_quest

# Initialisation de l'application FastAPI
app = FastAPI()

# Modèle Pydantic pour la requête
class QuestionRequest(BaseModel):
    question: str

# Route POST pour répondre à une question
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Répond à une question en utilisant le modèle Gemini et retourne la réponse, les sources et les scores.
    """
    question = request.question

    # Appeler la fonction answer_quest pour obtenir la réponse
    response, docs, scores = answer_quest(question, enable_insert=True)  

    # Vérifier si une réponse a été générée
    if response:
        return {
            "question": question,
            "response": response,
            "sources": [
                {
                    "source": doc.metadata['source'],
                    "focus_area": doc.metadata['focus_area']
                }
                for doc in docs
            ],
            "scores": scores
        }
    else:
        # Lever une exception si aucune réponse n'a été générée
        raise HTTPException(
            status_code=500,
            detail="Erreur lors de la génération de la réponse"
        )

# Route GET pour vérifier que l'API est en ligne
@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur l'API HealthGenie Chatbot !"}