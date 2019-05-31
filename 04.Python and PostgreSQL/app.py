import os
from dotenv import load_dotenv
from pathlib import Path

from user import User
from database import Database

load_dotenv()
load_dotenv(dotenv_path=Path('.') / '.env')


Database.initialise(
    user='postgres',
    password=os.getenv('DB_PASS'),
    database='learning',
    host='localhost'
)

my_user = User('test7@test.te', 'Test', 'Lastname Test', None)

my_user.save_to_db()

first_user_by_email = User.load_from_db_by_email('test7@test.te')
print(first_user_by_email)

# my_user.save_to_db()
