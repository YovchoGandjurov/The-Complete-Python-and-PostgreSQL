from psycopg2 import pool
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
load_dotenv(dotenv_path=Path('.') / '.env')


class Database:
    connection_pool = None

    @classmethod
    def initialise(cls):
        cls.connection_pool = pool.SimpleConnectionPool(
            1,
            10,
            user='postgres',
            password=os.getenv('DB_PASS'),
            database='learning',
            host='localhost'
        )

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, conn):
        cls.connection_pool.putconn(conn)

    @classmethod
    def close_all_connections(cls):
        cls.connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = Database.get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.conn.rollback()
        else:
            self.cursor.close()
            self.conn.commit()
        Database.return_connection(self.conn)
