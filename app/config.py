import os

class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Use PostgreSQL in production/docker
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/mydb")

class TestingConfig(BaseConfig):
    # Use SQLite for testing if needed, or use PostgreSQL for consistency
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/mydb")
    DEBUG = True
    SECRET_KEY = 'somekey'