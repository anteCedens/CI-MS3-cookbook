import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

if path.exists('env.py'):
    import env

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# index.html / homepage


@app.route('/')
@app.route('/index_page')
def index_page():
    return render_template("index.html", recipes=mongo.db.recipes.find())

# Browse Recipes


@app.route('/recipes_list')
def recipes_list():
    return render_template("recipes_list.html", recipes=mongo.db.recipes.find())

# Contact Us


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
