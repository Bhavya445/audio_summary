
## 🎙️ Meeting Audio Summarizer with AI

An intelligent desktop app that converts **spoken meeting audio** into text and provides a **coherent summary** using **Cohere's LLM API**. Built using `PyQt6`, `SpeechRecognition`, and `Cohere`, this tool enables streamlined summarization of long meetings in just a few clicks.

---

### ✨ Features

* 🎧 Convert audio (MP3, WAV, etc.) to text using Google Speech Recognition
* 🧠 Summarize content using **Cohere’s `command-xlarge-nightly` model**
* 🖥️ Easy-to-use GUI built with **PyQt6**
* 📁 Input any local audio file path
* ✂️ Choose desired summary length (number of words)
* ⚡ Multithreaded processing for smooth UI performance

---


### 🧠 How It Works

1. **User provides an audio file path**
2. **Audio is transcribed to text** using Google's Speech-to-Text
3. **Cohere LLM** summarizes the content into a compact paragraph
4. Output is displayed in the application’s GUI

---

### 🚀 Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/Bhavya445/audio_summary
cd audio_summary
```

#### 2. Install Dependencies

Make sure you have Python 3.9+ installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install cohere PyQt6 SpeechRecognition pydub
```

Also install **FFmpeg**, required by `pydub`:

* On Mac: `brew install ffmpeg`
* On Ubuntu: `sudo apt install ffmpeg`
* On Windows: Download from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add to PATH

---

### 🔑 Setup Cohere API Key

1. Sign up at [cohere.com](https://cohere.com)
2. Get your API key
3. Open `ai.py` and replace the placeholder:

```python
api_key = 'your_cohere_api_key_here'
```

---

### 🧪 Running the App

```bash
python main.py
```

* Click **"Enter Audio Path"** and provide the local path to your audio file (MP3/WAV)
* Set the desired **summary length** in number of words
* Click **"Summarize"** to generate a concise summary

---

### 📁 Project Structure

```bash
├── ai.py                  # Cohere model wrapper
├── audio_to_text.py       # Audio to text converter using Google STT
├── main.py                # Main PyQt6 GUI application
├── requirements.txt       # Python dependencies
└── README.md              # You're here
```

---

### 🛡️ Notes

* Google Speech Recognition works best with clear audio in English.
* For large audio files, consider downsampling to improve performance.
* Make sure `.wav` conversion works via `pydub` by validating `ffmpeg` is in your system path.

---

### 🧠 Example Prompt to LLM

```text
Summarize the following text in 50 words: <transcribed meeting text>
```

---
