import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# DATABASE CONNECTION STRING
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Proton45@localhost:5432/fyyurDB'
SQLALCHEMY_TRACK_MODIFICATIONS = True