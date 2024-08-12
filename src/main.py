from io import BytesIO
import schedule
import time
import os
from pathlib import Path

from src.gemini.jokes import jokes
from src.gemini.newsScrapper import news_sum
from src.pynews import news_scrap
from src.text_to_voice import text_to_speech
from pydub import AudioSegment
# from elevenlabsApi import convet_text_to_audio


def main_fn(cat):
   
    if(cat == 'joke'):
        summary = jokes()
    else:
        news_data = news_scrap(cat)
        summary = news_sum(news_data)

    my_file = Path( os.getcwd() + "\\src\\fillers\\soft_bgm.mp3")
    print (my_file)

    # final_voice = AudioSegment.from_file(my_file, format="mp3")

    voice = text_to_speech(summary)
    speech_audio = AudioSegment.from_file(voice, format="mp3")
    speech_audio = speech_audio.speedup(1.2, 150, 25)

    audio_with_music = speech_audio.overlay(AudioSegment.from_mp3(my_file), position=10, loop=True)

    # final_voice = final_voice + audio_with_music
    # voice = text_to_speech(summary)


    combined_audio_bytes = BytesIO()
    audio_with_music.export(combined_audio_bytes, 
                            format="mp3", 
                            parameters=["-ar", "44100"])
    combined_audio_bytes.seek(0)  

    return combined_audio_bytes

    # with open('scrapped_news/sports.csv_summary.csv', encoding='utf-8') as file:
    #     summary_file = file.read()
    #convet_text_to_audio(summary_file)

