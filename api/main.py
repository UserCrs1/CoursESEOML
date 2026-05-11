from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialisation de l'application FastAPI
app = FastAPI(title="API d'Analyse de Sentiment (Allociné)")

# Le dossier où le modèle sera partagé par le Builder (via Docker Volume)
MODEL_DIR = "/shared_model"

# Définition du format de la requête attendue
class TextRequest(BaseModel):
    text: str

# TO DO 1 : Charger le modèle d'analyse de sentiment en mémoire.
# Attention : Le modèle doit être chargé depuis MODEL_DIR (qui fera office de cache)
# et non retéléchargé depuis internet.
print("Chargement du modèle en mémoire...")
# sentiment_analyzer = ... 
print("Modèle prêt !")


@app.post("/predict")
async def predict_sentiment(request: TextRequest):
    """
    Cette route reçoit du texte et renvoie un sentiment (POSITIF/NEGATIF).
    """
    # TO DO 2 : Utiliser le modèle 'sentiment_analyzer' sur le texte reçu
    # result = ...
    
    # TO DO 3 : Renvoyer un dictionnaire propre avec le texte, la prédiction et le score de confiance
    return {
        "text": request.text, 
        "prediction": "Remplacer par le label du modèle",
        "confidence": 0.0 # Remplacer par le score du modèle
    }