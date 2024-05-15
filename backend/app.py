from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Import models here to ensure they are known to SQLAlchemy
from models import UserConfiguration, APIInteractionLog, FileMetadata

@app.route('/')
def home():
    return "Hello, Flask with SQLite!"

if __name__ == '__main__':
    app.run(debug=True)