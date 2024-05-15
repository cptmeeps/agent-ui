from app import db
from models import UserConfiguration, APIInteractionLog, FileMetadata

def add_user_configuration(api_key, settings):
    user_config = UserConfiguration(api_key=api_key, settings=settings)
    db.session.add(user_config)
    db.session.commit()

def get_user_configuration(api_key):
    return UserConfiguration.query.filter_by(api_key=api_key).first()