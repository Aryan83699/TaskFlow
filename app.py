from flask import Flask , url_for,redirect,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped,mapped_column

app=Flask(__name__)
# app = Flask(__name__)

app.config["SECRET_KEY"] = "Aryan@2005"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db=SQLAlchemy(app)


class User(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(nullable=False,unique=True)
    password:Mapped[str]=mapped_column(nullable=False)
    


with app.app_context():

    db.create_all()

    existing_user = User.query.filter_by(
        email="singharyan90827@gmail.com"
    ).first()

    if not existing_user:
        db.session.add(
            User(
                email="singharyan90827@gmail.com",
                password="Aryan@2005"
            )
        )
        db.session.commit()




@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    email = request.form.get("Email")
    password = request.form.get("Password")

    user = User.query.filter_by(
        email=email,
        password=password
    ).first()

    if user:
        flash("Welcome To My Project")
        return redirect(url_for("home"))

    flash("Invalid Email or Password")
    return redirect(url_for("home"))



if __name__=="__main__":
    app.run(debug=True,port=5000)


    
