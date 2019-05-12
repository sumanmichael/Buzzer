from twilio.rest import Client
import time


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '' #Account_SID here

auth_token = ''  #Authentication_Token Here

client = Client(account_sid, auth_token)

def sms_send(phno,text):
    message = client.messages \
                    .create(
                         body=text,
                         from_='',   #Your VirtualPhone number here
                         to=phno
                     )

