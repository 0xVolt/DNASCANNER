from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        retString = 'Task #{}'.format(self.id)
        
        return retString


@app.route('/', methods=['POST', 'GET'])
def index():
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
        

# By default, the method list consists of 'GET'
@app.route('/delete/<int:id>')
def delete(id):
    taskToDelete = Model.query.get_or_404(id)
    
    try:
        db.session.delete(taskToDelete)
        db.session.commit()
        
        return redirect('/')
    except:
        return 'There was an issue deleting that task.'


# Functionality to update tasks
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    taskToUpdate = Model.query.get_or_404(id)
    
    if request.method == 'POST':
        taskToUpdate.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating that task.'
    else:
        return render_template('update.html', task=taskToUpdate)    


if __name__ == '__main__':
    app.run(debug=True)