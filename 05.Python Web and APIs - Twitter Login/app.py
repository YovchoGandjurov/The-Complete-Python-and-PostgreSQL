from flask import Flask, render_template, session, redirect
from twitter_utils import get_request_token, get_oath_verifier_url


app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token

    return redirect(get_oath_verifier_url(request_token))


app.run(port=4995)
