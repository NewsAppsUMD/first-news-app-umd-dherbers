from flask import Flask
from flask import render_template
app = Flask(__name__)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)