# Flask port number: localhost:5000

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/contact')
def Contact_page():
    return render_template("contact.html")

@app.route('/home')
def Home_page():
    return "Home Page"

@app.route('/gallery')
def Gallery_page():
    return "Gallery Page"

if __name__ == "__main__":
    app.run()

