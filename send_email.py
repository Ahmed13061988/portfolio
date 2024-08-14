import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "mesoshooter@gmail.com"
password = "ctaneqysdsvmvnos"
receiver = "mesoshooter@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Test!
Hello!
How are you?
Bye
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

