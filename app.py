from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body", "")
    sender = request.form.get("From", "")
    print(f"Incoming from {sender}: {incoming_msg}")  # so you can watch it arrive

    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)