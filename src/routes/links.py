from flask import Blueprint, jsonify, make_response, request, send_file
from src.db.links import add_link_to_bucket, update_bucket_id_in_link
from src.main import main_fn
from src.links_category import LinkCategory

links_blueprint = Blueprint('links', __name__)

@links_blueprint.route('/links/health', methods=['GET'])
def health_check():
    return jsonify({ 'status': 'healthy'})

@links_blueprint.route('/links', methods=['POST'])
def generate_link():

    try:
        request_data  = request.get_json()

        if 'category' not in request_data:
            return jsonify({ 
                'status': 'bad request',
                'error message': 'category not found'
            }), 400

        category = request_data['category']
        link_id = request_data['link_id']
        # link_name = request_data['link_name']

        if category not in LinkCategory:
            return jsonify({ 
                'status': 'bad request',
                "error message": 'Bad category'
            }), 400
        
        link_audio = main_fn(category)
        
        # with open(f"links/{link_name}.mp3", "wb") as f:
        #     f.write(link_audio.getvalue())

        # Store the audio to the bucket
        bucket_obj = add_link_to_bucket(link_audio)
        update_bucket_id_in_link(link_id, bucket_obj)
        
        return jsonify({
            'status' : 'success'
        }), 200
    except Exception as e:
        return jsonify({
            'status' : e
        }), 500

    # return voice
