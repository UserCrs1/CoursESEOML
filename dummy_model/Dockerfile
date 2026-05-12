FROM python:3.10-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du script (assure-toi que le nom du fichier est identique)
COPY generate_dummies.py .

# On lance uniquement le script Python
CMD ["python", "generate_dummies.py"]