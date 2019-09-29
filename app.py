from flask import Flask, render_template, request
import logging
import sys
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        gmailaddress = "assistantofcantu@gmail.com"
        gmailpassword = "8>mGW-Vj"
        mailto = request.form['email']
        space = """
        
                """
        msg = MIMEMultipart()
        msg['From'] = request.form['name']
        msg['To'] = 'David Cantú'
        msg['Subject'] = request.form['subject']
        msg_content1 = MIMEText('Buen dia, le llego un mensaje de este correo ' +mailto, 'plain', 'utf-8')
        msg.attach(msg_content1)
        msg_content3 = MIMEText(space)
        msg.attach(msg_content3)
        msg_content2 = MIMEText(request.form['message'])
        msg.attach(msg_content2)
        text = str(msg)
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        mailServer.sendmail(gmailaddress, "davidcantumartinez@gmail.com" , text)
        print(" \n Sent!")
        mailServer.quit()
        return render_template('about.html')