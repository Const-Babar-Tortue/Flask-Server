from os import environ
from datetime import timedelta


class Config:
    # General
    TESTING = environ.get("TESTING")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")
    JWT_AUTH_HEADER_PREFIX = "Bearer"
    JWT_EXPIRATION_DELTA = timedelta(seconds=604800)

    SQLALCHEMY_DATABASE_URI = "sqlite:///./data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("TRACK_MODIFICATION")
