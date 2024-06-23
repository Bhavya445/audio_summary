import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QInputDialog
from ai import Chatbot
import threading
from audio_to_text import convert_audio_to_text

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 680, 400)
        self.chat_area.setReadOnly(True)

        # audio file path button
        self.filepath_button = QPushButton("Enter Audio Path", self)
        self.filepath_button.setGeometry(10, 420, 150, 40)
        self.filepath_button.clicked.connect(self.enter_audio_path)

        # Number of words button
        self.words_button = QPushButton("Set Summary Length", self)
        self.words_button.setGeometry(170, 420, 150, 40)
        self.words_button.clicked.connect(self.set_summary_length)
        self.words_button.setEnabled(False)  # Initially disabled

        # Summarize button
        self.summarize_button = QPushButton("Summarize", self)
        self.summarize_button.setGeometry(330, 420, 150, 40)
        self.summarize_button.clicked.connect(self.summarize)
        self.summarize_button.setEnabled(False)  # Initially disabled

        self.audio_file_path = None
        self.summary_length = None

        self.show()

    def enter_audio_path(self):
        audio_file_path, _ = QInputDialog.getText(self, 'Enter Audio File Path', 'Path:')
        if audio_file_path:
            self.audio_file_path = audio_file_path
            self.words_button.setEnabled(True)

    def set_summary_length(self):
        summary_length, ok = QInputDialog.getInt(self, 'Set Summary Length', 'Number of words:')
        if ok:
            self.summary_length = summary_length
            self.summarize_button.setEnabled(True)

    def summarize(self):
        if not self.audio_file_path or not self.summary_length:
            self.chat_area.append("<span style='color: yellow'>Audio path or summary length not provided.</span></p>")
            return

        thread = threading.Thread(target=self.process_audio_file)
        thread.start()

    def process_audio_file(self):
        self.chat_area.append("<span style='color: yellow'>Processing audio file...</span></p>")
        try:
            text = convert_audio_to_text(self.audio_file_path)
            if text:
                summary = self.chatbot.get_response(f"Summarize the following text in {self.summary_length} words: {text}")
                self.chat_area.append(f"<p><span style='color: #87CEEB'>Summary:</span> <span style='color: yellow'>{summary}</span></p>")
            else:
                self.chat_area.append("<span style='color: yellow'>Could not understand the audio file.</span></p>")
        except Exception as e:
            self.chat_area.append(f"<span style='color: yellow'>Error processing audio file: {str(e)}</span></p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
