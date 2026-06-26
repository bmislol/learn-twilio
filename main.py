import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()  # reads .env into the environment

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
from_number = os.environ["TWILIO_PHONE_NUMBER"]

client = Client(account_sid, auth_token)

# Twilio's Virtual Phone — a simulated device in your Console.
# Anything sent here shows up under Messaging > Virtual Phone.
VIRTUAL_PHONE = "+18777804236"

message = client.messages.create(
    body="Hello from Twilio 👋 my first SMS!",
    from_=from_number,
    to=VIRTUAL_PHONE,
)

print(f"Sent! Message SID: {message.sid}")
print(f"Status: {message.status}")