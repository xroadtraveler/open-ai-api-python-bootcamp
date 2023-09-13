import openai
import os

openai.api_key = os.getenv('OPENAI_CLASS_API_KEY')

## Transcribe:
with open('05 Like a Stone.mp3', 'rb') as audio_file:
    transcript = openai.Audio.transcribe('whisper-1', audio_file)
    print(transcript)


## Translate:
audio_file = open('12 Primavera.mp3', 'rb')
transcript = openai.Audio.translate('whisper-1', audio_file)
print(transcript)

