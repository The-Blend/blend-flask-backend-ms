import google.generativeai as genai
import constant
import re

genai.configure(api_key=constant.google_api)

def remove_between_asterisks(text):
    pattern = r'\*\*.*?\*\*'
    return re.sub(pattern, '', text)

def jokes():
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = (f''' 
        You are an RJ named Priya.
        Weite a small joke in an emotional and colloquial manner, 
        as if you re a 20-year-old RJ with a character with a soft voice. 
        Write an intro and outro of the rj.
        Make it feel personalized for a user and the script will be read at evening.
        Dont title the paragraphs or no links or emojies
    ''')

    response = model.generate_content([prompt])

    print(response.text)

    # summary = remove_between_asterisks(response.text)

    return response.text

    # with open(f'{file_path}_summary.csv', 'w', encoding='utf-8') as f:
    #         f.write(response.text)
