#Importing the necessary packages for the application
import os
from flask import Flask, redirect, render_template, request
from flask_mail import Mail, Message

app=Flask(__name__)
#Inserting the necessary configurations that is important for sending an email. It is taken from the Flask-Mail documentation

app.config["MAIL_DEFAILT_SENDER"]=os.getenv("MAIL_DEFAULT_SENDER")
#os.getenv is used for hiding the email used for sender address for security purposes
#app.config["MAIL_DEFAILT_SENDER"]="xxxxx@yyy.com"

app.config["MAIL_PASSWORD"]=os.getenv("MAIL_PASSWORD")
#os.getenv is used for hiding the password used for the mail for sending the email for security purposes
#app.config["MAIL_PASSWORD"]="xxxxx"

app.config["MAIL_PORT"]=587
#MAIL_PORT is the basic standard that mail servers use to send email to one another across the internet

app.config["MAIL_SERVER"]="smtp.gmail.com"
#smtp.gmail.com is google's outgoing SMTP sever offered by Google Mail

app.config["MAIL_USE_TLS"]=True
#MAIL_USE_TLS is borrowed from the Flask-Mail documentation

app.config["MAIL_USERNAME"]=os.getenv("MAIL_USERNAME")
#os.getenv is used for hiding the mailing username for security purposes
#app.config["MAIL_USERNAME"]="xxxxx@yyy.com"

mail=Mail(app)

SPORTS=[
    "Dodgeball",
	"Soccer",
	"Football",
	"Basketball",
	"Tennis",
	"Polo"
]

#Basic URL Application route
@app.route("/")
def indexpage():
    return render_template("index.html", sports=SPORTS)

#Registration Application route
@app.route("/registeration",methods=["POSTS"])
def registeration():
    email=request.form.get("email")
    if not email:
        return render_template("error.html",message="Missing Email")
    return render_template("error.html",message="Missing Name")
    if sport not in SPORTS:
        return render_template("error.html",message="Invalid sport")

    message=Message("You are registered",recipients=[email])
    mail.send(message)


    REGISTRANTS[name]=sport

    return render_template("success.html")