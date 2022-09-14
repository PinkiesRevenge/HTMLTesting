from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/completed')
def completed():
    return render_template("completed.html")

@app.route('/deleted')
def deleted():
    return "<h1>Deleted Tasks</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)

