# import os
import africastalking
from flask import Flask,request,render_template
import json, urllib 

app = Flask(__name__)

username ="sandbox"
api_key ="03be5802382511da751b6452ac1134df5c5e5b7155466fe8e591f115e5807b97"
africastalking.initialize(username,api_key)

sms = africastalking.SMS

@app.route("/",methods=["GET","POST"])
def main():
    if request.method == "POST":
        sms_message =request.form['smsMessage']
        phone_number = request.form['phoneNumber']

        print(sms_message)
        print(phone_number)

        response = sms.send(sms_message,[phone_number])
        print(response)

    return render_template('index.html')
        
if __name__ == "__main__":
    app.run(debug=True)