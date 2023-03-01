from email.message import Emailmessage
import ssl
import smtplib

email_sender = 'codewithtomi@gmail.com'

email_password = 'xqrhuaqncmaugccf'

email_reciever = ''

subject = "dont't forget to subscribe"
body ="""
when you watch a video, hit the subscribe 
"""

em = Emailmessage
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content(body)
