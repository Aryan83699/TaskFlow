from asyncio import tasks

from flask import Flask, Response, jsonify , url_for,redirect,render_template,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from psutil import users
from sqlalchemy.orm import Mapped,mapped_column
import random
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson import json_util




load_dotenv()

app=Flask(__name__)
# app = Flask(__name__)


SERVER_EMAIL=os.getenv("SERVER_EMAIL")
APP_PASS=os.getenv("APP_PASS")
MONGODB_URI=os.getenv("MONGODB_URI")

app.config["SECRET_KEY"] = "Aryan@2005"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db=SQLAlchemy(app)

client = MongoClient(MONGODB_URI,tls=True,tlsAllowInvalidCertificates=True)
db2 = client["task_db"]


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
    session['user_id']=user.id if user else None
    if user:
        # flash("Welcome To My Project")
        return render_template("tasks.html")

    flash("Invalid Email or Password")
    return render_template('register.html')



@app.route('/register',methods=['GET','POST'])
def register():
    email=request.form.get("REmail")
    password=request.form.get("pass")
    cpassword=request.form.get("pass_1")


    if password!=cpassword:
        flash("Invalid Email or Password")
        redirect(url_for("register"))
        return None 

    
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
        user=db.session.add(User(
                    email=session.get("email"),
                    password=session.get("password")
                ))
        session['user_id']=user.id
        db.session.commit()   
        flash("Email Verified")
        return None 

    flash("Fuck You")
    # User.query.all()
    # for user in users:
    #     print(user.name, user.email)
    return redirect(url_for("login"))



@app.route('/view_tasks')
def view():
    date=request.args.get('date')
    print(date)
    try:
        client.admin.command("ping")
        print("Connected successfully!")
    except Exception as e:
        print(e)

    tasks=db2.user_task.find({
        "user_id": session.get('user_id'),
        "date": str(date)
    })
    return Response(
        json_util.dumps(tasks),
        mimetype="application/json"
    )


@app.route('/delete_task',methods=['GET','POST','DELETE'])
def delete_task():

    query =db2.user_task.delete_one({
        "user_id":int(session.get("user_id")),
        "date": request.args.get('date'),
        "task":request.args.get('task')
    })
    
    
    if query.deleted_count==1:
        return jsonify({
            "sucess":True,
            "message":"Task Deleted Successfully"
        })
    return jsonify({
        "success":False,
        "message":"Task Not Found"
    }),404  

@app.route('/insert_task',methods=['UPDATE','GET','POST'])
def insert_task():
    result=db2.user_task.insert_one({
        "user_id":session.get("user_id"),
        "task":request.args.get('task'),
        "date":request.args.get("date"),
        "completed":"False"
    })

    if result.inserted_id:
        return jsonify({
            "success": True,
            "message": "Task inserted successfully."
        })

    return jsonify({
        "success": False,
        "message": "Failed to insert task."
    }), 500
    


@app.route('/update_task',methods=['PUT','GET','POST'])
def update_task():
    result=db2.user_task.update_one({
        "user_id":session.get("user_id"),
        "task":request.args.get('task'),
        "date":request.args.get('date')
    },
    {
        "$set":{"completed":request.args.get("status")}
    } )

    if result.modified_count:
        return jsonify({
            "success": True,
            "message": "Task inserted successfully."
        })

    return jsonify({
        "success": False,
        "message": "Failed to insert task."
    }), 500


if __name__=="__main__":
    app.run(debug=True,port=5000)


    
