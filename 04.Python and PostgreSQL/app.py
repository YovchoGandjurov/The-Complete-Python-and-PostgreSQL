from user import User


# my_user = User('test@test.te', 'Jose', 'Salvatierra', 1)
# my_user.save_to_db()

first_user = User.load_from_db_by_email('test@test.te')
print(first_user)
