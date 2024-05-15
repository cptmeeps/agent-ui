from flask import jsonify

def create_response(message, data=None):
    response = {"message": message, "data": data}
    return jsonify(response)