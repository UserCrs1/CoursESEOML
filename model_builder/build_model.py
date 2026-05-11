import os
# TO DO 1 : Importer les classes AutoModelForSequenceClassification et AutoTokenizer de la librairie transformers
# ...

MODEL_NAME = "tblard/tf-allocine"
MODEL_DIR = "/shared_model"  # Chemin absolu pour le volume Docker

print(f"Téléchargement du modèle {MODEL_NAME}...")

# TO DO 2 : Télécharger le modèle. 
# ATTENTION : Ce modèle a été créé avec TensorFlow. 
# Trouvez le paramètre booléen à ajouter pour le convertir automatiquement (pour PyTorch) lors du téléchargement.
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    # ??? = True
)

# TO DO 3 : Télécharger le Tokenizer associé au modèle
# tokenizer = ...

os.makedirs(MODEL_DIR, exist_ok=True)

# TO DO 4 : Sauvegarder LE MODÈLE ET LE TOKENIZER dans le dossier MODEL_DIR
# model...
# tokenizer...

print(f"Modèle et Tokenizer sauvegardés avec succès dans {MODEL_DIR}")