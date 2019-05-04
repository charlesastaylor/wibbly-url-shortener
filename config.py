import os

from flask.cli import load_dotenv


load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
