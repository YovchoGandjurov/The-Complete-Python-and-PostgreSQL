import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
load_dotenv(dotenv_path=Path('.') / '.env')


def connect():
    return psycopg2.connect(user='postgres', password=os.getenv('DB_PASS'),
                            database='learning', host='localhost')
