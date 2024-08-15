from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import io
from pdf2image import convert_from_bytes

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    
    if file.filename.lower().endswith('.pdf'):
        # Converte o PDF para imagens
        images = convert_from_bytes(file.read())
        # Realiza OCR em cada página do PDF
        text = ""
        for i, image in enumerate(images):
            text += pytesseract.image_to_string(image) + "\n"
    else:
        # Se não for um PDF, trata como imagem
        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)

    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)