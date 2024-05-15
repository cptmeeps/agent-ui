import os

def create_session_folder(session_name):
    os.makedirs(session_name, exist_ok=True)

def get_session_folder(session_name):
    return os.path.abspath(session_name)