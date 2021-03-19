from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("sqlite:///events.db")



@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        name = request.form.get("name")
        event = request.form.get("event_type")
        date = request.form.get("date")
        
        ## CHECK IF USER HAS INPUT ALL FIELDS
        if not name:
            return render_template("error.html", message = "Please input the event name to proceed")
        if not event:
            return render_template("error.html", message = "Please select the event type to proceed")
        if event not in EVENTS:
            return render_template("error.html", message = "This is not a valid event type")
            
        db.execute("INSERT INTO event (event_type, name, date) VALUES(?,?,?)", event, name, date)
        return redirect("/")
    else:
        events = db.execute("SELECT * FROM event")
        return render_template("index.html", events = events)
        
