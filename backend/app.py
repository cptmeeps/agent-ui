from flask import Flask
from database import db
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Import models after db initialization
with app.app_context():
  from models import UserConfiguration, APIInteractionLog, FileMetadata

@app.route('/')
def home():
  return "Hello, Flask with SQLite!"

@app.route('/api/request', methods=['POST'])
def api_request():
  from request_handler import handle_request
  return handle_request()

if __name__ == '__main__':
  app.run(debug=True)