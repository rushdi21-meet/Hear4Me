from flask import Flask, jsonify, request, render_template, redirect, url_for
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



@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

# Press the green button in the gutter to run the script.
if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
        debug=True
    )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
