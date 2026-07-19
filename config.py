import os
from dotenv import load_dotenv
load_dotenv()


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Try PostgreSQL first, fallback to SQLite if not available
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        SQLALCHEMY_DATABASE_URI = db_url
    else:
        # Fallback to SQLite for testing
        SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
