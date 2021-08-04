from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask import session as login_session
import random
from database import *

import webbrowser
# This is a sample Python script.
app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='templates/assets'  # Name of directory for static files
)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['psw']
        if query_by_name(username) == query_by_password(password):
            login_session['logged_in'] = True
            login_session['name'] = username
            return redirect(url_for('volunteer', login_session=login_session))
        return render_template('index.html')
    else:
        login_session['logged_in'] = False
        return render_template('index.html')



@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if login_session['logged_in']:
        return render_template('a_main.html')
    else:
        return redirect(url_for('main'))

@app.route('/volunteer_ar')
def volunteer_ar():
    if login_session['logged_in']:
        return render_template('main-ar.html')
    else:
        return redirect(url_for('main'))

@app.route('/volunteer_he')
def volunteer_he():
    if login_session['logged_in']:
        return render_template('main-he.html')
    else:
        return redirect(url_for('main'))

# Press the green button in the gutter to run the script.
if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
        debug=True
    )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
