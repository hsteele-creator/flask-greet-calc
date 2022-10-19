from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return f"""<h1>welcome!</h1>"""

@app.route("/welcome/<place>")
def welcome_place(place="hello"):
    return f"""<h1>welcome {place}!</h1>"""