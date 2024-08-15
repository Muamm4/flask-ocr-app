# Use uma imagem base do Python
FROM python:3.9-slim

# Instale as dependências do Tesseract OCR e Poppler
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo
COPY . .

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]