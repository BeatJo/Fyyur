import os
import psycopg2

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:azertyuuop@localhost:5432/fyyur'
SQLALCHEMY_TRACK_MODIFICATIONS = False
