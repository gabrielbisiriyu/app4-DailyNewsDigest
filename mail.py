import smtplib  # THIS IS AN EMAIL LIBRARY
import ssl
import os


def send_email_now(message=""):
    standar_host = "smtp.gmail.com"  # THIS IS A STANDARD HOST FOR Gmail
    standard_port = 465  # ALSO STANDARD PORT
    username = "guyex1996@gmail.com"

    password = os.getenv("PASSWORD")
   
    receiver = "guyex1996@gmail.com"

  
    my_context = ssl.create_default_context()  # FOR SENDING SECURE EMAIL

    with smtplib.SMTP_SSL(host=standar_host, port=standard_port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)





