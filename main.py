from flask import Flask, render_template, request
from flask import make_response
from flask import redirect
from flask import session, url_for

app = Flask(__name__)
app.config['SECRET_KEY']= 'favchienyourdi'


@app.route('/')
def index():
    if not session.get("name", None):
         return redirect(url_for('registration'))
    username = session.get('name',None)
    return render_template('index.html', username=username)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    session['name'] = None
    if request.method == 'POST':
        form = request.form

        first_name = form['first_name']
        last_name = form['last_name']
        username = form['username']
        password = form['password']

        session['name'] = f'{username}'
        return redirect(url_for('index'))
    return render_template('registration.html')

@app.route('/movie/<movie_name>', methods=['GET','POST'])
def movie(movie_name):
    link = request.args.get('link')
    username = session.get('name', None)
    return render_template('movie.html', movie_name=movie_name, link=link, username=username) 