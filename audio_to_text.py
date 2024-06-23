import speech_recognition as sr
from pydub import AudioSegment


def convert_audio_to_text(audio_file_path):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file_path)

    # Convert the audio file to WAV format (if not already in that format)
    if not audio_file_path.endswith('.wav'):
        audio_file_path = 'converted_audio.wav'
        audio.export(audio_file_path, format='wav')

    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Load the audio file using SpeechRecognition
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

        # Recognize (convert from speech to text)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Converted Text: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None



