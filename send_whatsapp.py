import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
my_whatsapp = os.environ["MY_WHATSAPP_NUMBER"]

client = Client(account_sid, auth_token)

# The shared Twilio WhatsApp Sandbox number — same for every account.
SANDBOX_NUMBER = "whatsapp:+14155238886"

message = client.messages.create(
    body="Hello on WhatsApp from Twilio! 🎉",
    from_=SANDBOX_NUMBER,
    to=f"whatsapp:{my_whatsapp}",   # note the whatsapp: prefix
)

print(f"Sent! Message SID: {message.sid}")
print(f"Status: {message.status}")