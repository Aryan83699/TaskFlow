from flask import Flask , url_for,redirect,render_template,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from psutil import users
from sqlalchemy.orm import Mapped,mapped_column
import random
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()



# session['otp']=str(otp)
# session['email']-email


app=Flask(__name__)
# app = Flask(__name__)


SERVER_EMAIL=os.getenv("SERVER_EMAIL")
APP_PASS=os.getenv("APP_PASS")

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



def send_otp(receiver_email,otp):
    msg=EmailMessage()
    msg["Subject"]="Email Verification"
    msg["From"]="aryansingha887@gmail.com"
    msg["To"]=receiver_email

    msg.set_content(f"Your OTP is {otp} \n Don't Share it with anybody")

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(
           SERVER_EMAIL,
            APP_PASS
        )

        smtp.send_message(msg)



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
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
    return render_template('register.html')



@app.route('/register',methods=['GET','POST'])
def register():
    email=request.form.get("REmail")
    password=request.form.get("pass")
    cpassword=request.form.get("pass_1")


    if password!=cpassword:
        flash("Invalid Email or Password")
        return redirect(url_for("register")) 

    
    session['email']=email
    session['password']=password

    otp=random.randint(100000,999999)

    session['otp']=str(otp)
    session['email']=email
    send_otp(email, otp)

    return render_template('verify.html')



@app.route('/verify',methods=['POST'])
def verify():

    user_otp=request.form.get('otp')
    
    if user_otp==session.get('otp'):
        existing_user = User.query.filter_by(
        email=session.get("email")
    ).first()

    if not existing_user:
        db.session.add(User(
                    email=session.get("email"),
                    password=session.get("password")
                ))
        db.session.commit()   
        flash("Email Verified")
        return None 

    flash("Fuck You")
    User.query.all()
    # for user in users:
    #     print(user.name, user.email)
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True,port=5000)


    
