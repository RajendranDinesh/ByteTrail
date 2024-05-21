import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = 'e4c4af3815b51b832c3ca4e6977ec4000b8736e0304d1b0eae74b23a46d050c9'
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DATABASE')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
