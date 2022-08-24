from flask import Flask, render_template, url_for
# Import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Add config for sqlalchemy
# Telling our app where the database is
# '///' is a relative path and '////' is an absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initialise the database
db = SQLAlchemy(app)

# Create the database model
class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    
    # This is always set automatically and never manually since it has a default field
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Creating a repr function to represent each task (object) as a string
    def __repr__(self):
        retString = 'Task #{}'.format(self.id)
        
        return retString

@app.route('/')
def index():
    return render_template('2-template-inheritance-index.html')

if __name__ == '__main__':
    app.run(debug=True)