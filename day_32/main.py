# Import Modules
from datetime import datetime
import smtplib

gmail_user = 'user_gmail.com'
gmail_password = 'userpassword'

birthday_date = (8, 9)
today = datetime.now()
today_tuple = (today.month, today.day)
# Mail settings
sent_from = gmail_user
to = [gmail_user]
subject = 'Happy Birthday!'
email_text = """
Dear NAME,

It's your birthday! Have a great day!

All my love,

Eviln<3
"""

if today_tuple == birthday_date:
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        print("email sent!")
    except Exception as e:
        print(repr(e))
        print("Something went wrong:(!")
