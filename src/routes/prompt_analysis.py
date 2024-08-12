from flask import Flask, request, jsonify, Blueprint
import spacy

nlp = spacy.load("en_core_web_sm")


prompt_blueprint = Blueprint('prompt', __name__)

@prompt_blueprint.route('/prompt', methods=['POST'])
def prompt():
    data = request.json

    if(not data):
        return jsonify({
            'status' : 'Bad Request'
        }), 400
    
    received_string = data.get('prompt', '')
    emotion, genre, link = analysis_prompt(received_string)

    return jsonify({
        "prompt": received_string, 
        "emotion": emotion, 
        "genre": genre, 
        "link": link
    })


def analysis_prompt(prompt):
    doc = nlp(prompt)

    emotion = None
    genre = None
    news=None
    
    emotion_keywords = ['sad', 'happy', 'depressed', 'calm', 'chill','melody']
    genre_keywords = ['pop', 'rock', 'classic', 'jazz']
    link_key = ['sports', 'business', 'stocks', 'education', 'health', 'technology','stock']

 
    for token in doc:
        if token.text.lower() in emotion_keywords:
            emotion = token.text.lower()
        if token.text.lower() in genre_keywords:
            genre = token.text.lower()
        if token.text.lower() in link_key:
            news=token.text.lower()
    
    return emotion, genre,news