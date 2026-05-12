from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
def faire_une_prediction(surface: int, nb_pieces: int):
    # Fausse prédiction pour la démo
    prix = surface * 5000 + nb_pieces * 10000
    return {"prix_estime": prix}