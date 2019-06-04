from database import CursorFromConnectionFromPool
import oauth2
from twitter_utils import consumer
import json
import constants


class User:
    def __init__(self, email, first_name, last_name,
                 oauth_token, oauth_token_secret, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id

    def __repr__(self):
        return f'<user: {self.email}>'

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'INSERT INTO twitter_users (email, first_name, last_name, \
                                    oauth_token, oauth_token_secret) \
                VALUES (%s, %s, %s, %s, %s)',
                (self.email, self.first_name, self.last_name,
                 self.oauth_token, self.oauth_token_secret)
            )

    @classmethod
    def load_from_db_by_email(cls, email):

        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(
                'SELECT * FROM twitter_users WHERE email=%s', (email, )
            )
            user_data = cursor.fetchone()
            if user_data:
                return cls(user_data[1], user_data[2], user_data[3],
                           user_data[4], user_data[5], user_data[0])

    def twitter_request(self, uri, verb='GET'):
        authorized_token = oauth2.Token(self.oauth_token,
                                        self.oauth_token_secret)
        authorized_client = oauth2.Client(consumer, authorized_token)

        # Make Twitter API calls
        response, content = authorized_client.request(uri, verb)
        if response.status != 200:
            print('An error occured when searching!')
        return json.loads(content.decode('utf-8'))
