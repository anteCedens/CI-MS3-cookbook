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


@app.route('/')
@app.route('/index_page')
def index_page():
    return render_template("index.html", recipes=mongo.db.recipes.find())


@app.route('/recipes_list')
def recipes_list():
    return render_template("recipes_list.html", recipes=mongo.db.recipes.find())


@app.route('/sign_in')
def sign_in():
    return render_template('signin.html')


@app.route('/recipe_details/<recipe_id>')
def recipe_details(recipe_id):
    try:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template('recipe_details.html', recipe=the_recipe)
    except Exception:
        return render_template("404.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
