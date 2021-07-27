from flask import Flask, render_template, request ,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sujannya.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False)
    message =db.Column(db.String(200), nullable=False)


@app.route('/')
def hello_world(): 
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def cf():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']

        cn=Contact(name=name,email=email,message=message)
        db.session.add(cn)
        db.session.commit()
    return redirect("/")  

if __name__ == "__main__":
    app.run(debug=True)    