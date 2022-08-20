# Learn Flask
Following along with this [tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) on YouTube, this log file was created to document progress on learning the Flask framework for backend web development in Python. 

## Timeline
- [X] Create a new directory to house the project.
- [X] `cd` into the project dir.
- [X] Type `virtualenv env` into the terminal to create a new virtual environment with the name `env`. This name can be anything but `env` is the convention. You should now see a new folder with the name you'd specified.
- [X] Activate the venv using `env\Scripts\activate.ps1` on powershell or `env\Scripts\activate.bat` on cmd. You'll see the terminal prompt change to indicate you're in a venv.
- [X] You can verify whether the venv is active by running `pip -V` and checking the path to the pip in use.
- [X] Install dependencies. `pip install flask flask-sqlalchemy` to install flask and it's dependencies in this venv.
- [X] Create a new file named `app.py` and run it using `py app.py` to deploy the app on your localhost.
- [X] Create folders named `static` and `templates`.
- [ ] Create `index.html` inside `templates`.
- [ ] Now, instead of returning a string in our app, we'll `return render_template(index.html)`.
- [ ] Create boilerplate html code in `index.html` and refresh the project.
- [ ] Create a master html file to inherit from. 
- [ ] Inherit that file in `index.html`.
- [ ] Make a css folder.
- [ ] Create a `main.css` file with some basic rule sets.
- [ ] Link `main.css` to the master html file.

## Notes
Use these notes by reading the bit that corresponds to the step you're on in the timeline.
### Virtual Environments
- All the packages needed for the project are located within this directory which makes the project more portable in a collaborative setting.
- Requirements are installed into the working directory directly.
- Virtual environments are the standard when it comes to collaborative projects due to the easy package management. 

### Substituting the string for an html page
- Two folders needed to be created. One named static and the other, templates. 
- In the templates folder, we create a file named `index.html`. 
- By creating this file, we can now return a render of the html file it in our app when defining the route.
- When specifying the name of the file to render, we need not specify the full path since Flask knows to look in the templates folder.

### Template Inheritance
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

### Static content
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