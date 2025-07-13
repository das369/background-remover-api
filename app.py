from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "Background Remover API is running."

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No image uploaded'}, 400

    input_data = request.files['image'].read()
    output_data = remove(input_data)

    return send_file(
        io.BytesIO(output_data),
        mimetype='image/png',
        as_attachment=True,
        download_name='no-bg.png'
    )

if __name__ == '__main__':
    app.run()