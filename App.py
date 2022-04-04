# Flask port number: localhost:5000

from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my website"

@app.route('/contact')
def Contact_page():
    return "Contact page"

@app.route('/home')
def Home_page():
    return "Home Page"

@app.route('/gallery')
def Gallery_page():
    return "Gallery Page"

if __name__ == "__main__":
    app.run()

