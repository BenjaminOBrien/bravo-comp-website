# Modules
from app import app
from flask import render_template, send_from_directory

# Routes
@app.route("/")
def index():
    return render_template("content/index.html"), 200

@app.route("/roster")
def roster():
    return render_template(
        "content/roster.html",
        roster = [
            "Zack Snider", "Wesley Husky", "Aaron Hanley",
            "Benjamin O'Brien", "Bryson Flowers", "Luke Chaney",
            "Philip Crawford", "Tynor Kelly", "Jaxon Brown",
            "Gabrielle Fedrick", "Maximus Melton", "Elijah Vance"
        ]
    ), 200

@app.route("/about")
def about_us():
    return render_template("content/about.html"), 200

# Static files
@app.route("/s/<path:path>")
def get_static_file(path):
    return send_from_directory("app/static", path, conditional = True)
