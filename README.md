# **An Online Cookbook Project**


This project was built for the purposes of one of my personal projects ("milestone projects") at Code Institute.

This was a data-centric development project: the requirements were:

>build a full-stack site that allows your users to manage a common dataset about a particular domain.

Or, slightly more specifically:

>Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain.

Another important note was:

>No authentication is expected for this project. The focus is on the data, rather than any business logic.

There were a few project ideas suggested, and I chose to try and create an online cookbook.

---

## Table of Contents
1. [**Design and Features**](#design-and-features)
    - [**Project Purpose**](#project-purpose)
        - [**_User Stories_**](#user-stories)
    - [**Design**](#design)
        - [**_Fonts_**](#fonts)
        - [**_Images_**](#images)
        - [**_Navigation_**](#navigation)
        - [**_Responsive Design_**](#responsive-design)
        - [**_Wireframes_**](#wireframes)
    - [**Features**](#features)
2. [**Technologies Used**](#technologies-used)
3. [**Testing and Features Left to Implement**](#testing-and-features-left-to-implement)
    - [**Testing**](#testing)
        - [**Deployment**](#deployment)
    - [**Features Left to Implement**](#features-left-to-implement)
4. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---

## **Design and Features**

### **Project Purpose**

In addition to what was already mentioned above, like the data 
handling infrastrucutre (building a MongoDB-backed Flask-based web app), 
the core focus of the project is providing a CRUD (**C**reate, **R**ead, **U**pdate, **D**elete) functionality for a user 
through a main navigation menu and a structured layout.

In other words:

>create functionality for users to create, locate, display, edit and delete records

and also hopefully do that in a both visually appealing and user friendly manner (ease of use).


#### **_User Stories_**

External user’s goals:

- Find and share recipes
- The site is visually catchy and easy enough and simple to use
- The site offers some kind of browse-through list or gallery of recipes, with recipe images included

### **Design**

#### **_Fonts_**

Site uses two fonts:
 - `Lobster`
 - `Indie Flower`

 `Lobster` is primarily used for heading, and `Indie Flower` for paragraph based text. Idea was to use two fonts 
 that work well together, in both how they look combined on the page, and that they complement each other: 
 `Lobster` makes the heading stand out more, and `Indie Flower` increases readability, when there is more text.

 The fonts were also chosen to fit semantically with the site's imagery, in trying to provide a "homey", "casual" feeling 
 to the site - something evocative of "home cooking" - while on the other hand trying to maintain an impression of something 
 nevertheless "professionally designed".

 So, for instance, `Lobster` can be evocative of a fine dining menu look, while on the other hand still remaining not too stern, or "serious"; 
 `Indie Flower` looks like a handwritten font, evocative of recipes in household family cookbooks, while on the other hand still being not too "scribly" (as actual handwriting can be), and 
 thus still maintaining needed level of readability.

#### **_Images_**

 Following what is described about the fonts, imagery used tries to follow suite in maintaining than balance, and giving an coherent desired overall feel. 

 Index page and the About page have the same background image, thus linking them together.

 That image is of a cup of cofee on a saucer with some pastry. The image is postion on the far right of the background, leaving a lot of white space to the left: 
 that space is utilized to display site's images (carousel on the index page) and text without obscuring them.

 The image itself gives that "homey" feel - while still being clearly professionally done and staged (the placement of the cinammon decorations etc.) - it is evocative of having somebody over to your home, and serving them a cup 
 of cofee and some pastry - maybe while waiting for a homecooked meal to be ready (connects to the index page, the landing page, the first page - you just got here, welcome); or maybe just after you've finished such a meal (connects to the 
 About page - we've eaten, it's cofee time, time to talk "about", about yourselves possibly (About page is about the site)).

 Navbar and footer background is the same, and is the same on all the subsites. It's reminiscent of a tablecloth - possibly a fine dining one, possibly a special occassions home-kept one. What suggests a tablecloth is that the background isn't 
 "just red" for instance: it hassome shadows, slight crinkles, etc. The shadows work well with the text.

 The text color of the navbar and footer is white, over a dark background; while the text on the index and About pages is black, over a white background - providing an opposite contrast relation between tha navbar and footer, and pages' text.

 The "Browse Recipes" page displays recipes on cards. The layout is four cards per row on desktop. 
 The background of the pafe is white, with no image, so as not to obstruct viewing of the recipe cards.

 Rest of the pages are concerned with the recipes' text. They either provide a detailed viewing of a selected recipe, or a form for either editing or adding a recipe. 
 All those pages have the same background image: that of an old, worn-out cookbook, opened wide on a blank page. That would be evocative of an old family cookbook, that's been 
 in one's home for a while.

 The form that opens for adding a new recipe has it's own background, over the cookbook: that of a piece of paper from a notebook. Some of those old family cookbooks sometimes 
 have pages from other notebooks with recipes inserted into them, for instance as the cookbook gets filled out over time, and there's no more space for new recipes, etc.

 The form for editing an existing recipe also has a notebook paper background, but in this case that piece of paper is crinkled (as oposed to the smooth one for adding a new recipe): 
 symbolically, the idea is that when you add a new recipe the page is new, not written on before; when you edit a recipe, the page has already been in use, so it shows signs of wear, it's been crinkled.

 When you open a detailed recipe view, you're just seeing the recipe over the old cookbook backround: you reading a recipe "from the book", that made into the book, is neither being just entered, nor edited.  

 There's a "Q" favicon implemented as well - corresponding to the site's name: "Q-zine" (chosen because it sounds like "cuisine").

#### **_Navigation_**

Navbar consist of a site title/logo, which also functions as a home button, And three other links to subsites: "Browse Recipes", "Post Recipes", and "About".

Footer has some copyright text example, and links in the forms of social media icons. Those links aren't set up to lead anywhere.

Navbar and footer appear on all the site's pages.

The recipes' cards on the "Browse Recipes" page have buttons, in the form of either just icons, or buttons with text inside, that lead to the Edit Recipe form, page where the recipe's details are displayed, 
or they show a short preview of the recipe.

#### **_Responsive Design_**

The project basically takes on Materialize's responsive design structure, with practically no alterations.

Main feature on smaller screen, as opposed to the desktop view, is that the navbar's links to the subsites 
condense into a hamburger menu, which then open the sidebar where those links are now located. On smaller screens the site's logo 
remains in the navbar (does not get moved to the sidebar), and is centered.

#### **_Wireframes_**
Some (staggeringly) crude wireframes (yep, I do (still) use a pen(cil) and paper)) can be 
seen here:
- [main/index page](wireframes/sketch_main_page.JPG)
- [recipe list page](wireframes/sketch_recipe_list_page.JPG)
- [recipe card layout](wireframes/sketch_recipe_card.JPG)

MongoDB collection schema example for the project can be seen here:
- [MongoDB collection schema](wireframes/MS3_MongoDB_schema.JPG)


### **Features**


## **Technologies Used**

- **_IDE and code storage_**
    - GitPod - used as the online IDE
    - GitHub - for the storage of the code online
- **_Back-End_**
    - Python 3
        - Flask
        - Jinja
        - PyMongo
        - DNSPython
- **_Database_**
    - MongoDB Atlas
- **_Front-End_**
    - HTML
    - CSS
        - Materialize
        - Material Icons
        - Font Awesome
        - Google Fonts
    - JavaScript
        - jQuery

- **_Deployment_**
    - Heroku

## **Testing and Features Left to Implement**

### **Testing**

### **Features Left to Implement**

**_Carousel "randomizer"_**

Currently, the carousel and the index page displays all the images from the database, 
in the sequence in which they are stored in the database, which is chronologically. And the 
sequence resets - i.e. starts from the beginning - each time the index page is loaded.

So, if an image stored in the database last, it would go to the back of the carousel, and get displayed last. 
It's a FIFO principle, basically (**F**irst **I**n **F**irst **O**ut - i.e. what is stored in the database 
first, is displayed out in the carousel first also).

With a larger number of entries, some of the images would in practice never get displayed, or more precicely, 
they would never get _seen_, as it could be not expected for a user to stay on the index page long enough for those 
particulary images to be displayed on the carousel.

Or, in other words, some of the images would not "get a fair chance to be seen". And the idea, or the desire, is that all 
images, which represent recipes, get treated equally in that regard.

I attempted to change the "step" option of the carousel - i.e. parameter which controls the image display pattern: default "step" is 1, 
which means the carousel displays the next image in the que. So if the "step" is set to, for instance, 3, the carousel would display every 
third image. But, that doesn't visually look right, becuase the transition to the following image doesn't render seamlessly, but it rather 
looks like the carousel is spinning at great speed until it reaches the desired image.

So a "carousel randomizer" is an idea where the carousel is set to display images in random sequence, and the sequence is randomized (or "shuffled") 
anew every time the index page is loaded.

**_Delete confirmation_**

Currently the delete button in the Edit Recipe form form is set up that you only press it once, and the recipe is deleted. I'd like to have an additional 
"delete confirmation" feature set up: when the delete button is pressed, a message would pop up (using a Materialize "modal", for instance) asking the user 
to confirm deletion.

**_Character restriciton_**

Currently, there is no character restriction in the forms, when adding a new recipe. Implementing such a feature might be beneficial, namely for such fields in 
the form as the recipe's name, and short description.

**_Further form styling_**

Maybe make the forms (for adding and editing recipes) more visually appeling, based on user feedback, in regards to typography, or button styling. Possibly adding further data entry fields about the recipes, such 
as serving, ingredients, course (main, side, starter, etc.), or meal (breakfast, lunch, dinner).

**_Search bar_**

Currently there is none.

## **Credits**

### **Content**

Content on the index and About pages was written by me.

Recipes entered in the database at the moment of writting this, were taken from these sources:

- https://tasty.co/recipe/baked-avocado-eggs
- https://www.delish.com/cooking/recipe-ideas/a26728380/baked-pineapple-salmon-recipe/
- https://www.bbcgoodfood.com/recipes/spaghetti-meatballs
- https://www.allrecipes.com/recipe/257198/thin-crust-pizza-dough/
- https://www.bbcgoodfood.com/recipes/chorizo-mozzarella-gnocchi-bake

### **Media**

All recipes images diplayed on the site as of the moment of writting this are rendered via their URL's, so a source 
for the image is always evident.

All the other images used, stored in the project on GitPod, are from:

- https://hipwallpaper.com/
- https://wallpaperaccess.com/

except for the 404 image, which is from:

- https://www.freepik.com/

Icons used are from:

- https://material.io/resources/icons/?style=baseline
- https://fontawesome.com/

### **Acknowledgements**

For the core know-how on how to build a project like this, I've used Code Institutes "Task Manager" 
tutorial project:

- https://github.com/Code-Institute-Solutions/TaskManager

In regards to designing an online cookbook specifically, I've browsed through my fellow students' projects, 
such as:

- https://github.com/sohailshams/cookbook
- https://github.com/sabinemm/recipe-site-ms3
- https://github.com/amybru/byoboba
- https://github.com/Trevbytes/Chickpeas
- https://github.com/ss00831/milestone3
- https://github.com/ajgoward/daddies_recipes_MS3
- https://github.com/lewisclark4/CI-MilestoneProjectThree
- https://github.com/ceciliabinck/cook-with-me

As writing the readme.md goes, for me, since project one, it's always been W.D.C.L.D.: 
What Did Claire Lally Do?:

- https://github.com/ClaireLally8

Other resources used:

- https://www.lipsum.com/
- https://www.diffchecker.com/diff
- https://jpg2png.com/
- https://convertico.com/
