import os
# SOLUTION TO DO 1
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_NAME = "tblard/tf-allocine"
MODEL_DIR = "/shared_model"

print(f"Téléchargement du modèle {MODEL_NAME}...")

# SOLUTION TO DO 2
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    from_tf=True # Conversion TensorFlow -> PyTorch
)

# SOLUTION TO DO 3
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

os.makedirs(MODEL_DIR, exist_ok=True)

# SOLUTION TO DO 4
model.save_pretrained(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)

print(f"Modèle et Tokenizer sauvegardés avec succès dans {MODEL_DIR}")