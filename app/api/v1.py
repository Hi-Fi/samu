from flask import Blueprint, request, jsonify
from app.swap import change_words

v1 = Blueprint("v1", __name__)

@v1.route('/samu', methods=['POST'])
def word_change():
    json_data = request.json
    if json_data is not None:
        return jsonify(change_words(json_data))
    return "Payload missing", 400

@v1.route('/samu', methods=['GET'])
def word_change_instruction():
    return "Only POST supported"