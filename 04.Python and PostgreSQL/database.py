from psycopg2 import pool
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
load_dotenv(dotenv_path=Path('.') / '.env')

connection_pool = pool.SimpleConnectionPool(
    1,
    10,
    user='postgres',
    password=os.getenv('DB_PASS'),
    database='learning',
    host='localhost'
)
