# app.py - is the main file that runs the Flask server.

from flask import Flask, send_from_directory
from flask_cors import CORS 

# init_flask
app = Flask(__name__, static_folder='static')
# integrate_flask_cors
CORS(app)
# enable_debug_mode
app.config['DEBUG'] = True

# define_route_for_index
@app.route('/')
def serve_index():
  return send_from_directory('templates', 'index.html')

# configure_static_serving
@app.route('/<path:file_path>')
def serve_static(file_path):
  return send_from_directory('static', file_path)

if __name__ == '__main__':
  app.run()