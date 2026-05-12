FROM python:3.10-slim

WORKDIR /app

# On installe les librairies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le code de l'API
COPY main.py .

# On lance le serveur Uvicorn
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]