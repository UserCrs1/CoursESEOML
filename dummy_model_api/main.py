import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Dummy Models")

# Le même chemin que celui utilisé par le générateur !
MODEL_DIR = "../shared_model_dummy"

path_classif = os.path.join(MODEL_DIR, "model_classification.pkl")
path_reg = os.path.join(MODEL_DIR, "model_regression.pkl")

# 1. Chargement des modèles au démarrage de l'API
print("Chargement des modèles...")
try:
    model_classif = joblib.load(path_classif)
    model_reg = joblib.load(path_reg)
    print("✅ Modèles chargés avec succès !")
except FileNotFoundError:
    print(f"⚠️ ERREUR : Modèles introuvables dans {MODEL_DIR}.")
    print("Avez-vous bien monté le dossier contenant les fichiers .pkl ?")
    model_classif = None
    model_reg = None

# 2. Format de la requête attendue (nos modèles attendent 2 variables)
class FeaturesInput(BaseModel):
    feature_1: float
    feature_2: float

# 3. Route pour la Classification
@app.post("/predict/classif")
def predict_classif(data: FeaturesInput):
    if model_classif is None:
        raise HTTPException(status_code=404, detail="Modèle classification non trouvé")
    
    # Scikit-learn attend un tableau 2D, ex: [[0.5, 0.8]]
    X = np.array([[data.feature_1, data.feature_2]])
    prediction = model_classif.predict(X)
    
    return {"prediction": int(prediction[0]), "type": "Classification"}

# 4. Route pour la Régression
@app.post("/predict/reg")
def predict_reg(data: FeaturesInput):
    if model_reg is None:
        raise HTTPException(status_code=404, detail="Modèle régression non trouvé")
    
    X = np.array([[data.feature_1, data.feature_2]])
    prediction = model_reg.predict(X)
    
    return {"prediction": float(prediction[0]), "type": "Regression"}