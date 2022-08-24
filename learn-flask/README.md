# 1. Learn Flask
Following along with this [tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) on YouTube, this log file was created to document progress on learning the Flask framework for backend web development in Python. 
## 1.1. Table of Contents
- [1. Learn Flask](#1-learn-flask)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. Checklist](#12-checklist)
  - [1.3. Notes](#13-notes)
    - [1.3.1. Virtual Environments](#131-virtual-environments)
    - [1.3.2. Substituting the string for an html page](#132-substituting-the-string-for-an-html-page)
    - [1.3.3. Template Inheritance](#133-template-inheritance)
    - [1.3.4. Static content](#134-static-content)
    - [1.3.5. Database connectivity](#135-database-connectivity)
    - [1.3.6. Creating the database model](#136-creating-the-database-model)

---

## 1.2. Checklist
**Initialisation**
- [X] Create a new directory to house the project.
- [X] `cd` into the project dir.
- [X] Type `virtualenv env` into the terminal to create a new virtual environment with the name `env`. This name can be anything but `env` is the convention. You should now see a new folder with the name you'd specified.
- [X] Activate the venv using `env\Scripts\activate.ps1` on powershell or `env\Scripts\activate.bat` on cmd. You'll see the terminal prompt change to indicate you're in a venv.
- [X] You can verify whether the venv is active by running `pip -V` and checking the path to the pip in use.

**Installing dependencies**
- [X] Install dependencies. `pip install flask flask-sqlalchemy` to install flask and it's dependencies in this venv.

**Deploying app**
- [X] Create a new file named `app.py` and run it using `py app.py` to deploy the app on your localhost.

**Adding routes**
- [X] Create folders named `static` and `templates`.
- [X] Create `index.html` inside `templates`.
- [X] Now, instead of returning a string in our app, we'll `return render_template(index.html)`.
- [X] Create boilerplate html code in `index.html` and refresh the project.

**Using template inheritance**
- [X] Create a master html file to inherit from. 
- [X] Inherit that file in `index.html`.

**Adding css**
- [X] Make a css folder.
- [X] Create a `main.css` file with some basic rule sets.
- [X] Link `main.css` to the master html file.

**Adding database functionality**
- [ ] Import `sqlalchemy`

---

## 1.3. Notes
Use these notes by reading the bit that corresponds to the step you're on in the checklist.
### 1.3.1. Virtual Environments
- All the packages needed for the project are located within this directory which makes the project more portable in a collaborative setting.
- Requirements are installed into the working directory directly.
- Virtual environments are the standard when it comes to collaborative projects due to the easy package management. 

### 1.3.2. Substituting the string for an html page
- Two folders needed to be created. One named static and the other, templates. 
- In the templates folder, we create a file named `index.html`. 
- By creating this file, we can now return a render of the html file it in our app when defining the route.
- When specifying the name of the file to render, we need not specify the full path since Flask knows to look in the templates folder.

### 1.3.3. Template Inheritance
- This is achieved by creating a master html page that is inherited into every other page so as to cut redundant code.
- For this, create a new file in templates named `base.html`. This will be our skeleton. 
- In this page, use Jinja2 syntax to create a block like so.
```html
    {% block head/body %}
    {% endblock %}
```
- Jinja2 is the template engine that Flask uses. We create a block in the code that we'll utilise to insert our code into on all the other pages when we inherit this template. 
- The `base.html` file uses one block for the head and another for the body.
- Now, to inherit `base.html`, change `index.html` to be, 
```html
    <!-- Inherit from base.html -->
    {% extends 'base.html' %}

    {% block head %}
    <!-- Code for the head goes here -->
    {% endblock %}

    {% block body %}
    <!-- Code for the body goes here -->
    {% endblock %}
```

### 1.3.4. Static content
- In the static folder, make a new folder named css and create a file named `main.css`.
- Put some basic rule sets in the `main.css` file for example,
    ```css
    body {
        margin: 0;
        font-family: sans-serif;
    }
    ```
- This stylesheet now needs to be linked in the `base.html` master html file. However, the css file cannot directly be linked as a path. We gotta make use of more Jinja2 syntax. We link the stylesheet by doing the following,
  1. Importing the function `url_for()` from flask in our `app.py`. Our Flask import then becomes, 
        ```python 
        from flask import flask, render_template, url_for
        ```
  2. Link the stylesheet using
        ```html
        <!-- Notice the use of single quotes within the double quotes -->
        <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
        ```
    When using `{{}}`, this makes sure that the return type of the arguments is a string. This is why it's used to slot in the path of a file in string form. 
- The same applies if you were trying to link a JavaScript file. It would be `filename='js/main.js'` instead.

### 1.3.5. Database connectivity
- Import SQLAlchemy into the python app. The import statements now are,
    ```py
    from flask import Flask, render_template, url_for
    from flask_sqlalchemy import SQLAlchemy
    ```
- We configure the app to check for a database that's using sqlite. We reference this using a relative path. This is what the code looks like,
    ```py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    ```
- Then, initialising the database,
    ```py
    db = SQLAlchemy(app)
    ```
### 1.3.6. Creating the database model
- Make a class to instantiate a database. Should look something like this,

    ```py
    class Model(db.model):
        id = db.Column(db.Integer, primary_key=True)
        # Making sure that the user doesn't leave this field empty
        content = db.Column(db.String(200), nullable=False)
        # Make sure to include the datetime library
        # datetime.utcnow returns the current time
        date_created = db.Column(db.DateTime, default=datetime.utcnow)
    ```
- Each field of the class is a new attribute in the database.
- Importing datetime looks like, 

    ```py
    from datetime import datetime
    ```
- In addition, define a function to return a string every time a new element is created. Like so,

    ```py
    # Creating a repr function to represent each task (object) as a string
    def __repr__(self):
        retString = 'Task #{}'.format(self.id)
        
        return retString
    ```
- In Python, `__repr__` is a special method used to represent a class’s objects as a string. `__repr__` is called by the repr() built-in function. You can define your own string representation of your class objects using the `__repr__` method.
- [This blog post](https://www.educative.io/answers/what-is-the-repr-method-in-python) is a good resource to learn about the `__repr__` method in Python. 