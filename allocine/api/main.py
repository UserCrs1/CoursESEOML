from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="API d'Analyse de Sentiment (Allociné)")

MODEL_DIR = "/shared_model"

class TextRequest(BaseModel):
    text: str

# SOLUTION TO DO 1 : 
# On utilise pipeline en précisant que le modèle et le tokenizer se trouvent dans MODEL_DIR
print("Chargement du modèle en mémoire...")
sentiment_analyzer = pipeline("sentiment-analysis", model=MODEL_DIR, tokenizer=MODEL_DIR)
print("Modèle prêt !")

@app.post("/predict")
async def predict_sentiment(request: TextRequest):
    # SOLUTION TO DO 2 :
    # Le pipeline renvoie une liste contenant un dictionnaire. On prend le premier élément [0].
    result = sentiment_analyzer(request.text)[0]
    
    # SOLUTION TO DO 3 :
    return {
        "text": request.text, 
        "prediction": result['label'],
        "confidence": round(result['score'], 4) # On arrondit pour faire plus propre
    }