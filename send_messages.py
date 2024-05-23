# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#This code just calls the twilio api to queue a text message

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# Your Auth Token from twilio.com/console


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_num = os.environ['TWILIO_PHONE_NUMBER']
client = Client(account_sid, auth_token)

def text(PhoneNum, message):
    message = client.messages \
        .create(
            body=message,
            from_=account_num,
            status_callback='http://postb.in/1234abcd',
            to=PhoneNum
        )

