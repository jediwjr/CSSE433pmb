from flask import Flask
from flask import render_template
from cassandra_functions import init_db, view_messages_c, send_message_c

app = Flask(__name__)

@app.route('/')
def index():
    init_db()
    return render_template('index.html', methods=['GET, POST'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

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
    send_message_c(2, request.form['text'])
    flash('Message Sent')
    return redirect(url_for('send_message'))

@app.route('/send_message', methods=['GET'])
def send_message():
    return render_template('send_message.html')

if __name__ == '__main__':
    app.run()
