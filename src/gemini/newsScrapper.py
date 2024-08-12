import google.generativeai as genai
import constant
import re

genai.configure(api_key=constant.google_api)

def remove_between_asterisks(text):
    pattern = r'\*\*.*?\*\*'
    return re.sub(pattern, '', text)

def news_sum(content):
    # try:
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #         content = file.read()
    #         print(f"Content of {file_path} opened")
    # except FileNotFoundError:
    #     print(f"File {file_path} not found.")
    # except IOError:
    #     print(f"An error occurred while reading the file {file_path}.")

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # prompt = (f'''
    #     Use these inputs the {content} to write a script and only the script for an RJ named Priya. 
    #     Create multiple 4-5 scripts for the interesting news making it each link.
    #     I'll be giving this script directly to a text to voice AI. so no need to have title or description.
    #     just give me bullents of each links for each script.
    #     each link has to be short and sweet for time {constant.time}.
    #     Make the script in an emotional and colloquial manner, 
    #     as if you re a 20-year-old RJ with a character with a soft voice. 
    #     Write an intro and outro for each if needed.
    #     Make it feel personalized for a user. 
    #     Make it time specific if you think it helps.
    # ''')

    prompt = (f''' 
        Use these inputs the {content} to write a summary for an RJ named Priya.
        use the best 1-2 news for the interesting news and make it each links.
        each link has to be short and sweet for time {constant.time}.
        Make the script in an emotional and colloquial manner, 
        as if you re a 20-year-old RJ with a character with a soft voice. 
        Consider each paragraph as seperate links.
        Write a small intro and outro of the rj for each link.
        Make it feel personalized for a user.
        Dont title the paragraphs or links or emojis
    ''')

    response = model.generate_content([prompt])

    print(response.text)

    # summary = remove_between_asterisks(response.text)

    return response.text

    # with open(f'{file_path}_summary.csv', 'w', encoding='utf-8') as f:
    #         f.write(response.text)
