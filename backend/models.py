from database import db

class UserConfiguration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(128), unique=True, nullable=False)
    settings = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class APIInteractionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_configuration.id'), nullable=False)
    api_endpoint = db.Column(db.String(256), nullable=False)
    request_payload = db.Column(db.Text, nullable=False)
    response_payload = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class FileMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_configuration.id'), nullable=False)
    session_name = db.Column(db.String(128), nullable=False)
    file_name = db.Column(db.String(256), nullable=False)
    file_path = db.Column(db.String(512), nullable=False)
    file_type = db.Column(db.String(64), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())