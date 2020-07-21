# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]

# name of database
app.config['MONGO_DBNAME'] = 'database-test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:moninananM4!@cluster0-qezhz.mongodb.net/database-test?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    print("hello")
    collection = mongo.db.events
    events = collection.find({})
    return render_template('index.html', events=events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event":"First Day of Class, yo", "date":"2019-08-21"})
    # return a message to the user
    return "Event added"

@app.route('/events/new', methods = ['GET', 'POST'])
def new_event():
    if request.method == 'GET':
        print("get request happened")
        return redirect("/")
        # return render_template('new_event.html')
    else:
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        user_name = request.form['user_name']

        collection = mongo.db.events
        collection.insert({"event":event_name, "date":event_date, "user": user_name})
        return redirect(url_for('index'))
        