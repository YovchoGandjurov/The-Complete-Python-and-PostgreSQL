from user import User
from database import Database


my_user = User('test6@test.te', 'Test', 'Lastname Test', None)

Database.initialise()

my_user.save_to_db()

first_user_by_email = User.load_from_db_by_email('test6@test.te')
print(first_user_by_email)

# my_user.save_to_db()
