from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Home page</h1>"