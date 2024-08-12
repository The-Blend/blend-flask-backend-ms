from io import BytesIO
from gtts import gTTS
from gtts.tts import gTTSError

text = "Hello, this is a sample text to speech conversion using Google Text-to-Speech."
language = 'en'

def text_to_speech(text):
    try:
        speech = gTTS(text=text, lang=language, slow=False)
        audio_bytes = BytesIO()
        speech.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except gTTSError as e:
        print("There was an error converting text to speech: ", e)
