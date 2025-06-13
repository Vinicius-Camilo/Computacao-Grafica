from flask import Flask, request, send_file, jsonify, send_from_directory
from steganography import encode_image, decode_image
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve o index.html na raiz
@app.route('/')
def index():
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
    return send_from_directory(frontend_path, 'index.html')

# Serve arquivos estáticos do frontend (css, js, etc)
@app.route('/<path:filename>')
def static_files(filename):
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
    return send_from_directory(frontend_path, filename)

@app.route('/encode', methods=['POST'])
def encode():
    if 'image' not in request.files or 'message' not in request.form:
        return jsonify({'error': 'Nenhuma imagem ou texto'}), 400

    image_file = request.files['image']
    message = request.form['message']

    if image_file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    encoded_image_path = os.path.join(
        UPLOAD_FOLDER, f"encoded_{image_file.filename}"
    )
    encode_image(image_path, message, encoded_image_path)

    return send_file(encoded_image_path, as_attachment=True)

@app.route('/decode', methods=['POST'])
def decode():
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem'}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(image_path)

    message = decode_image(image_path)

    if message is None:
        return jsonify({'message': 'Nenhuma mensagem secreta encontrada'}), 200

    return jsonify({'message': message}), 200

if __name__ == '__main__':
    app.run(debug=True)