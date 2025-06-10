# Booker - PDF to Audiobook Converter

Booker is a simple web application that allows users to convert PDF files into audiobooks using AI voice. This project uses Flask for the web application, PyPDF2 to read PDF files, and gTTS (Google Text-to-Speech) to convert text to speech. Do note it has yet to be improved.

## Features

- Upload a PDF file and convert it to an MP3 audiobook.
- Simple and intuitive UI design.
- Secure file upload and handling.

## Project Structure

```
Booker/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
│       └── logo.png
├── templates/
│   └── index.html
└── uploads/
```

## Requirements

- Python 3.7 or higher
- Flask
- PyPDF2
- gTTS
- pydub

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/WestLee95/Booker.git
cd Booker
```

### 2. Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Access the Application

Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Upload a PDF File**: 
   - Go to the home page.
   - Upload a PDF file using the dropzone provided.

2. **Convert to Audio**: 
   - Click on the "Convert to Audio" button.
   - The application will process the PDF and provide a downloadable MP3 file.

## UI Design

- **Header**: Contains the logo and the application name "Booker".
- **Main Section**: Contains the file upload dropzone and the "Convert to Audio" button.
- **Footer**: Contains placeholder links like About, Products, Pricing, Terms, etc.

## Color Scheme

- Background: `#1A2238`
- Dropzone Border and Button Border: `#9DAAF2`
- Button Background: `#F4DB7D`
- Header and Footer Background: `#FF6A3D`

## Technologies Used

- **Flask**: Web framework for the application.
- **PyPDF2**: For reading PDF files.
- **gTTS**: For converting text to speech.
- **pydub**: For handling audio file manipulation.
- **HTML/CSS**: For the frontend.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

```
