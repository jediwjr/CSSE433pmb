from flask import (Flask, render_template, request, flash, redirect, url_for,
session)
import uuid
from cassandra_functions import init_db, view_messages_c, send_message_c, edit_message_c, delete_message_c
from mongo_functions import add_user, get_user
from neo4j_functions import create_user, create_message, add_like, likes, remove_like
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    init_db()
    if(not(session.get('logged_in'))):
        session['username'] = ''
    return render_template('index.html', methods=['GET, POST'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        result = get_user(request.form['username'], request.form['password'])
        if(result == None):
            flash('Incorrect username or password')
            return redirect(url_for('login'))
        else:
            session['logged_in'] = True
            session['username'] = request.form['username']
            return redirect(url_for('.index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session['username']= ''
    return redirect(url_for('.index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if(request.method == 'POST'):
        if(request.form['username'] == ''):
            flash('You must enter a username')
            return redirect(url_for('signup'))
        if(request.form['password'] == ''):
            flash('You must enter a password')
            return redirect(url_for('signup'))
        if(request.form['password'] != request.form['confirm_password']):
            flash('Passwords do not match')
            return redirect(url_for('signup'))
        else:
            un = request.form['username']
            add_user(un, request.form['password'])
            create_user(un)
            return redirect(url_for('.index'))

@app.route('/view_messages', methods=['GET', 'POST'])
def view_messages():
    rows = view_messages_c()
    returned = [row for row in rows]
    return render_template('view_messages.html', returned=returned, chunklist=chunkList, like_func=likes)

@app.route('/edit_message', methods=['GET'])
def edit_message():
  msg_id = request.args.get('msgid')
  newtext = request.args.get('newtext')
  edit_message_c(msg_id, newtext)
  return redirect(url_for('view_messages'))

@app.route('/delete_message', methods=['GET', 'POST'])
def delete_message():
    m_id = request.form['msg_id']
    delete_message_c(m_id)
    return redirect(url_for('view_messages'))

@app.route('/post_message', methods=['POST'])
def post_message():
    username = session['username']
    text = request.form['text']
    lon = request.form['lon']
    lat= request.form['lat']
    msg_id = uuid.uuid4()
    send_message_c(msg_id, text, username, lat, lon)
    create_message(str(msg_id))
    flash('Message Sent')
    return redirect(url_for('send_message'))

@app.route('/send_message', methods=['GET'])
def send_message():
    return render_template('send_message.html')

def chunkList(l, chunksize):
    chunks = []
    for i in range(0, len(l), chunksize):
        chunks.append(l[i:i+chunksize])
    return chunks

@app.route('/like_message', methods=['GET', 'POST'])
def like_message():
    username = session['username']
    msg = request.form['msg_id']
    add_like(username,msg)
    return redirect(url_for('view_messages'))

@app.route('/unlike_message', methods=['GET','POST'])
def unlike_message():
    username = session['username']
    msg = request.form['msg_id']
    remove_like(username,msg)
    return redirect(url_for('view_messages'))

if __name__ == '__main__':
    app.secret_key = 'secret key'
    app.debug = True
    app.run()
