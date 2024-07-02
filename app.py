import os
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader
from gtts import gTTS
import tempfile

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def convert_pdf_to_audio(filepath):
    try:
        with open(filepath, 'rb') as file:
            reader = PdfFileReader(file)
            number_of_pages = reader.numPages
            text = ''
            for page in range(number_of_pages):
                text += reader.getPage(page).extract_text() + ' '
            
            # Debugging: Check extracted text
            if not text.strip():
                print("No text found in the PDF.")
                return None
            
            print(f"Extracted text: {text[:100]}...")  # Print first 100 characters of extracted text
            
            tts = gTTS(text)
            temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
            temp_audio_file.close()
            tts.save(temp_audio_file.name)
            return temp_audio_file.name
    except Exception as e:
        print(f"Error during PDF to audio conversion: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file"
        
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            output_path = convert_pdf_to_audio(filepath)
            
            if output_path:
                return send_file(output_path, as_attachment=True)
            else:
                return "Could not extract text from PDF or convert to audio."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
