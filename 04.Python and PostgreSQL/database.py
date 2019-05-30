from psycopg2 import pool
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
load_dotenv(dotenv_path=Path('.') / '.env')


connection_pool = pool.SimpleConnectionPool(
            1,
            1,
            user='postgres',
            password=os.getenv('DB_PASS'),
            database='learning',
            host='localhost'
        )


class ConnectionFromPool:
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = connection_pool.getconn()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        connection_pool.putconn(self.conn)
