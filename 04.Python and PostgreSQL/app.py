from user import User


my_user = User('test4@test.te', 'Test', 'Lastname Test', None)
my_user.save_to_db()

first_user_by_email = User.load_from_db_by_email('test4@test.te')
print(first_user_by_email)

my_user.save_to_db()
