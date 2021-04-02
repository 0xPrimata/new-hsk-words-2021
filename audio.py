import pandas as pd
import pypinyin
import pyttsx3
from google.cloud import texttospeech

pinyin1 = open('pinyin1.txt', encoding="utf8").read().split('\n')
pinyin2 = open('pinyin2.txt', encoding="utf8").read().split('\n')
pinyin3 = open('pinyin3.txt', encoding="utf8").read().split('\n')
pinyin4 = open('pinyin4.txt', encoding="utf8").read().split('\n')
pinyin5 = open('pinyin5.txt', encoding="utf8").read().split('\n')
pinyin6 = open('pinyin6.txt', encoding="utf8").read().split('\n')
pinyin = [pinyin1, pinyin2, pinyin3, pinyin4, pinyin5, pinyin6]
def audioit(file):
    comp = []
    for text in file:
        a = text.split(',')
        audiopath = synthesize_text(a[0],a[2])
        print(audiopath)
        b=text+","+audiopath
        comp.append(b)
    return comp

def synthesize_text(text, output):
    """Synthesizes speech from the input string of text."""
    

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="cmn-CN",
        name="cmn-CN-Wavenet-A",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open(f"audios/{output}.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file f"{output}.mp3"')
        return f"audios/{output}.mp3"



# for i in range(0, 6):
#     file = audioit(pinyin[i])
#     with open(f'complete{i+1}.txt', 'w',encoding='utf8') as f:
#         for item in file:
#             f.write("\n%s" % item)
file = audioit(pinyin[4])
with open(f'complete{5}.txt', 'w',encoding='utf8') as f:
    for item in file:
        f.write("\n%s" % item)