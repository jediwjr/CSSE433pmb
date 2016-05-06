from flask import (Flask, render_template, request, flash, redirect, url_for,
session)
import uuid
from cassandra_functions import init_db, view_messages_c, send_message_c

app = Flask(__name__)

@app.route('/')
def index():
    init_db()
    return render_template('index.html', methods=['GET, POST'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['logged_in'] = True
        return redirect(url_for('.index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('.index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/view_messages', methods=['GET', 'POST'])
def view_messages():
    rows = view_messages_c()
    messages = [row[1] for row in rows]
    return render_template('view_messages.html', messages=messages)

@app.route('/post_message', methods=['POST'])
def post_message():
    send_message_c(uuid.uuid4(), request.form['text'])
    flash('Message Sent')
    return redirect(url_for('send_message'))

@app.route('/send_geo', methods=['get'])
def send_geo():
    return render_template('send_geo.html')

@app.route('/send_message', methods=['GET'])
def send_message():
    return render_template('send_message.html')

if __name__ == '__main__':
    app.secret_key = 'secret key'
    app.debug = True
    app.run()
