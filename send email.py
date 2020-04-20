import smtplib

from email.mime.text import MIMEText

import email.utils

sender_email = "zeefu21@gmail.com"
sender_name = "zeefu"

password = "R640wmd174!"

receiver_email = "zeefu@trixcorp.com"
receiver_name = "mohammed"

email_text = '''
            new dummy text following industry standards
'''

def broadcast_email():

    print("\nSending Email... \n")

    message = MIMEText(email_text)
    message['To'] = email.utils.formataddress((receiver_email, receiver_name))
    message['From'] = email.utils.formataddress((sender_email, sender_name))
    message['Subject'] = ' Email automation test '
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendemail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("\nEmail Broadcasted ...\n")

broadcast_email()
