# Imports needed to make the code work
import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

if path.exists('env.py'):
    import env

# Setting environment variables needed to connect to MongoDB
# Those variables are to be inputed manually to Heroku to make the deployment work
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


# index.html / homepage
# This is the default route, to be desplayed when the site is loaded
@app.route('/')
@app.route('/index_page')
def index_page():
    return render_template("index.html", recipes=mongo.db.recipes.find())



# 'Browse Recipes' option from the navbar
# Recipes are retrieved - i.e. read - from the database
@app.route('/recipes_list')
def recipes_list():
    return render_template("recipes_list.html", recipes=mongo.db.recipes.find())



# 'Post Recipe' option from the navbar is represented with the next TWO app.route-s
# First app.route renders the 'Add a Recipe' form
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", recipes=mongo.db.recipes.find())



# Second app.route insets -i.e. writes - the data entered in the 'Add a Recipe' form to the database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes_list'))


# Editing / updating recipes is represented with the next TWO app.route-s
# First app.route renders the 'Edit Recipe' form
# It first retrieves (reads) the selected recipe's data from the database
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)


# Second app.route writes (updates) the data back to the database
# It updates the listed fields ('recipe_name' etc.) in the DB's document with the corresponding unique id
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                 {
        'recipe_name': request.form.get('recipe_name'),
        'preparation_time': request.form.get('preparation_time'),
        'recipe_description': request.form.get('recipe_description'),
        'image_src': request.form.get('image_src'),
        'recipe_details': request.form.get('recipe_details')
    })
    return redirect(url_for('recipes_list'))


# Deletes recipe from the database
# Part of the 'Edit Recipe' form
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes_list'))


# 'View' recipe option
@app.route('/recipe_details/<recipe_id>')
def recipe_details(recipe_id):
    try:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template('recipe_details.html', recipe=the_recipe)
    except Exception:
        return render_template("404.html")


# 'About' page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
