import os
import joblib
import numpy as np
from sklearn.dummy import DummyClassifier, DummyRegressor

# 1. Définition du dossier partagé (le Volume Docker)
MODEL_DIR = "/shared_model_dummy"

# On s'assure que le dossier existe avant d'y écrire
os.makedirs(MODEL_DIR, exist_ok=True)

print("Création des modèles bouchons (Dummy Models) pour débloquer l'équipe API...\n")

# ---------------------------------------------------------
# 1. FAUX MODÈLE DE CLASSIFICATION (ex: Spam ou Non Spam)
# ---------------------------------------------------------
print("Entraînement du faux modèle de Classification...")

# Fausse donnée : 10 exemples, 2 variables
X_dummy_classif = np.random.rand(10, 2)
# Catégories (le 0 est majoritaire)
y_dummy_classif = [0, 1, 0, 0, 1, 0, 0, 0, 1, 0] 

# Entraînement du faux modèle (prédit toujours la classe majoritaire)
model_classif = DummyClassifier(strategy="most_frequent")
model_classif.fit(X_dummy_classif, y_dummy_classif)

# Sauvegarde dans le dossier partagé
path_classif = os.path.join(MODEL_DIR, "model_classification.pkl")
joblib.dump(model_classif, path_classif)

print(f"✅ Modèle sauvegardé : {path_classif} (Prédira toujours '0')\n")


# ---------------------------------------------------------
# 2. FAUX MODÈLE DE RÉGRESSION (ex: Prix d'un appartement)
# ---------------------------------------------------------
print("Entraînement du faux modèle de Régression...")

# Fausse donnée : 10 exemples, 2 variables
X_dummy_reg = np.random.rand(10, 2)
# Faux prix en euros
y_dummy_reg = [150000, 200000, 180000, 250000, 300000, 160000, 220000, 190000, 210000, 240000] 

# Entraînement du faux modèle (prédit toujours la moyenne des prix)
model_reg = DummyRegressor(strategy="mean")
model_reg.fit(X_dummy_reg, y_dummy_reg)

# Sauvegarde dans le dossier partagé
path_reg = os.path.join(MODEL_DIR, "model_regression.pkl")
joblib.dump(model_reg, path_reg)

print(f"✅ Modèle sauvegardé : {path_reg} (Prédira toujours la moyenne)\n")

