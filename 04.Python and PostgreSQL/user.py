from database import CursorFromConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f'<user: {self.email}>'

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'INSERT INTO users (email, first_name, last_name) \
                VALUES (%s, %s, %s)',
                (self.email, self.first_name, self.last_name)
            )

    @classmethod
    def load_from_db_by_email(cls, email):

        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'SELECT * FROM users WHERE email=%s', (email, )
            )
            user_data = cursor.fetchone()
            return cls(user_data[1], user_data[2], user_data[3],
                       user_data[0])
