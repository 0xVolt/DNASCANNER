# Learn Flask
Following along with this [tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) on YouTube, this log file was created to document progress on learning the Flask framework for backend web development in Python.

## 1. Table of Contents
- [Learn Flask](#learn-flask)
  - [1. Table of Contents](#1-table-of-contents)
  - [2. Checklist](#2-checklist)
  - [3. Notes](#3-notes)
    - [3.1. Virtual Environments](#31-virtual-environments)
    - [3.2. Substituting the string for an html page](#32-substituting-the-string-for-an-html-page)
    - [3.3. Template Inheritance](#33-template-inheritance)
    - [3.4. Static content](#34-static-content)
    - [3.5. Database connectivity](#35-database-connectivity)
    - [3.6. Creating the database model](#36-creating-the-database-model)
    - [3.7. Creating the database](#37-creating-the-database)
  - [4. Creating the Task Master app](#4-creating-the-task-master-app)
    - [4.1. Creating the basic layout](#41-creating-the-basic-layout)
    - [4.2. Creating a task](#42-creating-a-task)
      - [4.2.1. Programming the logic](#421-programming-the-logic)
      - [4.2.2. Putting it all together](#422-putting-it-all-together)
    - [4.3. Making the table update dynamically](#43-making-the-table-update-dynamically)
    - [4.4. Adding functionality to delete tasks](#44-adding-functionality-to-delete-tasks)
    - [4.5. Adding functionality to update tasks](#45-adding-functionality-to-update-tasks)

---

## 2. Checklist
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
- [X] Import `sqlalchemy`
- [X] Configure sqlite database
- [X] Initialise database
- [X] Create a database model using a class
- [X] Ensure that an `__repr__` string is implemented through the class
- [X] Setup database using the py interpreter in the terminal

**Build Task Master app**
- [X] Make separate `base.html`, `index.html`, `main.css` and `app.py` files for the project
- [X] Write `index.html`
  - [X] Create a div
    - [X] Add header and table
    - [X] Add links to the static row
    - [X] Add a form at the end after table
- [X] Edit `main.css` to format table
- [X] Write more logic in `app.py`
  - [X] Creation of tasks
  - [X] Deletion of tasks
  - [X] Updating tasks
    - [X] Create a separate dynamic page to edit tasks

**Wrapping up**
- [X] Complete documentation

---

## 3. Notes
Use these notes by reading the bit that corresponds to the step you're on in the checklist.
### 3.1. Virtual Environments
- All the packages needed for the project are located within this directory which makes the project more portable in a collaborative setting.
- Requirements are installed into the working directory directly.
- Virtual environments are the standard when it comes to collaborative projects due to the easy package management. 

### 3.2. Substituting the string for an html page
- Two folders needed to be created. One named static and the other, templates. 
- In the templates folder, we create a file named `index.html`. 
- By creating this file, we can now return a render of the html file it in our app when defining the route.
- When specifying the name of the file to render, we need not specify the full path since Flask knows to look in the templates folder.

### 3.3. Template Inheritance
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

### 3.4. Static content
- In the static folder, make a new folder named css and create a file named `main.css`.
- Put some basic rule sets in the `main.css` file for example,
    ```css
    body {
        margin: 0;
        font-family: sans-serif;
    }
    ```
- This stylesheet now needs to be linked in the `base.html` master html file. However, the css file cannot directly be linked as a path. We gotta make use of more Jinja2 syntax. We link the stylesheet by doing the following,
    1. **Note: `url_for` no longer needs to be imported from Flask to be able to link the `main.css` file. It just becomes redundant.** For academic purposes, importing the function `url_for()` from flask in our `app.py` looks like, 
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

### 3.5. Database connectivity
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
### 3.6. Creating the database model
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

### 3.7. Creating the database
- Head to the terminal. Make sure your env is activated.
- Start an interactive Python shell. Type in `python` or `py` to start up an interpreter prompt.
- To create the database, type in, 
```py
1. from app import db
2. db.create_all()
```
- The python script needs to be named `app.py` since we've initialised using the scripts name. 
- On running the second command, a new `__pycache__` folder will be created along with our database element.
- You no longer need the terminal since the database has been setup following the above steps.

## 4. Creating the Task Master app
### 4.1. Creating the basic layout
- Write a new `index.html` file with a header and a table.
- This is the basic structure of the table we're creating. 
    ```html
    <div class="content">
        <h1>Task Master</h1>

        <table>
            <!-- Making columns -->
            <tr>
                <th>Task</th>
                <th>Added</th>
                <th>Actions</th>
            </tr>
            <tr>
                <!-- Create two empty rows -->
                <td></td>
                <td></td>
                <td>
                    <!-- Create two links -->
                    <a href="">Delete</a>
                    <br>
                    <a href="">Update</a>
                </td>
            </tr>
        </table>
    </div>
    ```
- Edit the `main.css` file to add,
    ```css
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    ```
    To make sure that the table is displayed with a border.
- Heading to `app.py`, we need to add another parameter named `methods` to the `@app.route()`. By default, the route is able to `'GET'` but unable to `'POST'`. We need to set it to perform both operations. The new `app.route()` header becomes,
    ```py
    @app.route('/', methods=['POST', 'GET'])
    ```
    We can now *post* through this route to send data to our database.
- Now, adding a form to our table, the action takes place in this route, i.e., `'/'` and the method would be `'POST'`. That looks something like this,
    ```html
    <form action="/" method="POST"></form>
    ```
    This form takes two inputs, one is the actual content and the second is a submit. The form ends up like this,
    ```html
    <form action="/" method="POST">
        <input type="text" name="content" id="content">
        <input type="submit" value="Add task">
    </form>
    ```
- For now, the second row of the table isn't updated dynamically. That's going to change soon. 
- Editing the `app.py` script, we add the logic to push data to our database. We first import `requests` from Flask.
- The import statement changes to,
    ```py
    from flask import Flask, render_template, request
    ```
- The `index()` function changes to,
    ```py
    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST':
            # Does virtually nothing
            pass
        else:
            return render_template('index.html')
    ```
### 4.2. Creating a task
- Create a request variable and passing in the id of the input from the form. Then use that request variable to create a new object of the database model.
- This object becomes our task which we will then push to the database.
#### 4.2.1. Programming the logic
- Check if the button was pressed on the site, i.e., the method employed is the *post* method.
    ```py
    if request.method == 'POST':
    ```
- Extracting the data from the form in the table. The `content` is in reference to the `name` of the input field and **not** `id`,
    ```py
    taskContent = request.form['content']
    ```
- Creating a new task with the extracted data
    ```py
    newTask = Model(content=taskContent)
    ```
- Updating the database
    ```py
    # Pushing the new task created to the database
    try:
        # Look familiar? This code pushes data to our database
        db.session.add(newTask)
        db.session.commit()
        
        # Remember to import redirect back to the index page
        return redirect('/')
    except:
        # This should never fail ideally
        return 'There was an issue adding your task to the database.'
    ```
    We write `return redirect('/')` so that the index page is displayed after updating the database. Also, update the import statement to include `redirect` like so,
    ```py
    from flask import Flask, render_template, request, redirect
    ```
- If the submit button is never pressed, this means that the method employed is the *get* method. We're just reading the page and nothing else. This method is called by default.
- When we're using the *get* method, we just sort all the tasks by the most recently created and displaying them.
    ```py
    else:
        # This looks at all the database contents and returns them in the order of their creation
        tasks = Model.query.order_by(Model.dateCreated).all()
        
        # Passing the tasks variable into the render_template() function
        return render_template('index.html', tasks=tasks)
    ```
- If instead, you want to display the most recent task created, use,
    ```py
    tasks = Model.query.order_by(Model.dateCreated).first()
    ```
#### 4.2.2. Putting it all together
```py
# If the submit button on the form is pressed
if request.method == 'POST':
    # Pass in the id of the input to extract
    taskContent = request.form['content']
    
    # Create an object of the table having content as the extracted content above
    newTask = Model(content=taskContent)
    
    # Pushing the new task created to the database
    try:
        # Look familiar? This code pushes data to our database
        db.session.add(newTask)
        db.session.commit()
        
        # Remember to import redirect back to the index page
        return redirect('/')
    except:
        # This should never fail ideally
        return 'There was an issue adding your task to the database.'
else:
    # This looks at all the database contents and returns them in the order of their creation
    tasks = Model.query.order_by(Model.dateCreated).all()
    # tasks = Model.query.order_by(Model.dateCreated).first()
    
    # Passing the tasks variable into the render_template() function
    return render_template('index.html', tasks=tasks)
```

### 4.3. Making the table update dynamically
- Adding Jinja2 syntax to our table in `index.html` to show a row for each task in the database. We use a for loop to iterate through the tasks in the task list. This task list comes from the above code passing `tasks` to `render_template()`. 

- The updated row dynamically becomes,
    ```html
    {% for task in tasks %}
        <tr>
            <!-- First column for content of the task -->
            <td>{{ task.content }}</td>
            <!-- Second column for the date created -->
            <!-- date() ensures that it's in the intended format -->
            <td>{{ task.dateCreated.date() }}</td>
            <td>
                <!-- Create a link -->
                <a href="">Delete</a>
                <br>
                <a href="">Update</a>
            </td>
        </tr>
    {% endfor %}
    ```
- It was at this point that the `task.content` field refers to the `name` of the input and not the `id`.
 
### 4.4. Adding functionality to delete tasks
- We query the database on the `id` field and not the name field like we did before. This is because the `id` field is our primary key. 
- We set the routes for these pages to be dynamic according to the `id` of the task.
- The route then becomes,
    ```py
    # By default, the method list consists of 'GET'
    @app.route('/delete/<int:id>')
    ```
- Defining the delete function right after as,
    ```py
    def delete(id):
        # More on this after
        taskToDelete = Model.query.get_or_404(id)
        
        try:
            db.session.delete(taskToDelete)
            db.session.commit()
            
            return redirect('/')
        except:
            return 'There was an issue deleting that task.'
    ```
- Here,
    ```py
    taskToDelete = Model.query.get_or_404(id)
    ```
    queries the database to find the task with the passed `id` or to return a `404` error if not found.
    The rest of the function's code has been discussed before and an explanation would be redundant.

### 4.5. Adding functionality to update tasks
- The idea is to make a separate page where there's a form to update a certain task. This form would look very similar to the form at the home page.
- Changes to `app.py` are as follows,
    1. Added the route for the page to update the files.
        ```py
        # Functionality to update tasks
        @app.route('/update/<int:id>', methods=['GET', 'POST'])
        ```
    2. Defining the function to update tasks.
        ```py
        # Passing in id as a parameter
        def update(id):
            # Querying for the task to update
            taskToUpdate = Model.query.get_or_404(id)
            
            # If a response was logged from the form
            if request.method == 'POST':
                # Extract from the form
                taskToUpdate.content = request.form['content']
                
                # Edit database
                try:
                    db.session.commit()
                    return redirect('/')
                except:
                    return 'There was an issue updating that task.'
            # Just display the update.html page if there isn't a response
            else:
                return render_template('update.html', task=taskToUpdate)
        ```
- Created a new file named `update.html` which inherits from `base.html`.
    ```html
    {% extends 'base.html' %}

    {% block head %}
    <title>Update Task</title>
    {% endblock %}

    {% block body %}
    <div class="content">
        <h1>Update Task</h1>

        <!-- Creating a form where the link is dynamically updated according to task.id -->
        <form action="/update/{{ task.id }}" method="POST">
            <input type="text" name="content" id="content" value="{{ task.content }}">
            <input type="submit" value="Update">
        </form>
    </div>
    {% endblock %}   
    ```

**That wraps up the documentation for this extremely short and simple project in flask.**

**[Back to top.](#1-learn-flask)**

---