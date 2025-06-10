Alright Mayor 🤠, let’s whip up a clean, sharp, and slightly friendly `README.md` for your **Booker** project—professional enough to impress the dev folks, but still easy on the eyes and vibes.

---

````markdown
# 📖 Booker - Turn PDFs into Audio, Instantly

[Live Demo 🚀](https://booker-pdf-to-audio.onrender.com/)  
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/downloads/release/python-3110/)  
![Screenshot](./screenshot.png)

---

## ✨ Overview

**Booker** is a lightweight web app that lets users convert PDF documents into audio with just a few clicks. Whether you're on the move, multitasking, or simply prefer listening over reading—Booker makes it easy to *read with your ears*.

Built with Python 3.11 and Flask, the app is designed for simplicity, speed, and accessibility.

---

## 🛠 Tech Stack

- **Backend**: Python 3.11, Flask
- **Frontend**: HTML, CSS (with a sprinkle of minimal styling)
- **Text-to-Speech**: pyttsx3 (offline TTS engine)
- **File Handling**: PDFMiner for extracting text from PDFs
- **Hosting**: Render

---

## 🚀 Features

- 📂 Upload a PDF file
- 🔊 Convert the entire document into audio
- 💾 Download the audio as an MP3
- ⚡ Simple, responsive UI for all screen sizes
- 💬 Offline-friendly text-to-speech (no external APIs!)

---

## 📸 Screenshot

![Booker UI](./assets/screenshot.png)

---

## 🧠 How It Works

1. User uploads a `.pdf` file.
2. App extracts text from the PDF.
3. Text is fed into `pyttsx3` to generate speech.
4. The audio is saved as an `.mp3` and made available for download.

---

## 🧰 Local Setup

Want to run it locally? Easy.

```bash
# Clone the repo
git clone https://github.com/WestLee95/Booker.git
cd Booker

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
````

Then open your browser and go to:
**`http://localhost:5000`**

---

## 📂 Folder Structure

```
Booker/
│
├── static/            # CSS, JS, and static assets
├── templates/         # HTML files (Flask views)
├── uploads/           # Temporarily stores uploaded PDFs
├── audio/             # Stores generated audio files
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
└── README.md          # You're here
```

---

## ⚠️ Known Limitations

* Only supports English PDFs (for now).
* Audio generation may take longer for large files.
* Some complex PDF layouts (tables, images) might not read well.

---

## 💡 Future Plans

* Multilingual support
* Voice customization (pitch, speed, gender)
* Save user preferences
* Bookmarking or text highlighting

---


## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

