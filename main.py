from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite3'
app.config['SECRET_KEY'] = "thelegitprogrammer&wecodeinpython"

db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    todo = db.Column(db.String(100))

    def __repr__(self):
        return self.todo

@app.route('/')
def index():
    return render_template('index.html', todos=Todos.query.all()[::-1])

@app.route('/add', methods = ['POST', 'GET'])
def add_todo():
    if request.method == 'POST':
        todo_item = request.form['todo']
        if todo_item:
            TODO = Todos(todo=todo_item)   
            db.session.add(TODO)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_todo(id):
    todo_to_delete = Todos.query.get_or_404(id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()