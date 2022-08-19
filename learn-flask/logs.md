# Learn Flask
Following along with this [tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) on YouTube, this log file was created to document progress on learning the Flask framework for backend web development in Python. 

## Steps
- [X] Create a new directory to house the project.
- [X] `cd` into the project dir.
- [X] Type `virtualenv env` into the terminal to create a new virtual environment with the name `env`. This name can be anything but `env` is the convention. You should now see a new folder with the name you'd specified.
- [X] Activate the venv using `env\Scripts\activate.ps1` on powershell or `env\Scripts\activate.bat` on cmd. You'll see the terminal prompt change to indicate you're in a venv.
- [X] You can verify whether the venv is active by running `pip -V` and checking the path to the pip in use.
- [X] Install dependencies. `pip install flask flask-sqlalchemy` to install flask and it's dependencies in this venv.
- [X] Create a new file named `app.py` and run it using `py app.py` to deploy the app on your localhost.

###### Note about using virtual environments:
- All the packages needed for the project are located within this directory which makes the project more portable in a collaborative setting.
- Requirements are installed into the working directory directly.
- Virtual environments are the standard when it comes to collaborative projects due to the easy package management. 