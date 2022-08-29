from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    
    # This is always set automatically and never manually since it has a default field
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Creating a repr function to represent each task (object) as a string
    def __repr__(self):
        retString = 'Task #{}'.format(self.id)
        
        return retString


@app.route('/', methods=['POST', 'GET'])
def index():
    # If the submit button on the form is pressed
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=True)