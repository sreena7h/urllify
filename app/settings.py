from dotenv import load_dotenv
import os


load_dotenv()

if os.getenv('DEBUG', default='false').lower() == 'true':
    DEBUG = True
else:
    DEBUG = False

HOST = os.getenv('HOST')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_AGENT = os.getenv('DATABASE_AGENT')
DATABASE_NAME = os.getenv('DATABASE_NAME')

