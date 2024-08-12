import requests
import os
import constant


import datetime


timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")



with open('summary.csv', encoding='utf-8') as file:
    summary_file = file.read()

def get_api_key():
    return os.environ[constant.elevenlabs_api]
def get_id():
    url ="https://api.elevenlabs.io/v1/voices"

    header = {
        "Accept": "application/json",
        "xi-api-key": 'sk_a398488858ab493801aa6509074802ccbe54ade0aa2ff5fe',
        "Content-Type": "application/json"
    }

    response = requests.get(url,headers=header)

    data=response.json()


    for voice in data['voices']:
        print(f"{voice['name']}: {voice['voice_id']}")

def convet_text_to_audio(text_content: str,voice_id="EXAVITQu4vr4xnSDxMaL"):
     header = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": constant.elevenlabs_api
        
    }
    
     print("Header======",header)
     data = {
         "text": text_content,
         "model_id": "eleven_multilingual_v2",
         "voice_settings": {
             "stability":0.5,
             "similarity_boost":0.5
         }
     }

     CHUNK_SIZE=1024

     

     url= f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

     response = requests.post(url, json=data,headers=header)

     print(response)

     output_file_path="news_out.mp3"

     with open(output_file_path,'wb') as f:
         for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
             if chunk:
                 f.write(chunk)
    
     return output_file_path


# convet_text_to_audio(summary_file)