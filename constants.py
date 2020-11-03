from dotenv import load_dotenv
import os

load_dotenv()

DBNAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

TARGET_TABLE = os.getenv('TARGET_TABLE')
