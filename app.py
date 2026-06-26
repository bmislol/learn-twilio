import os
from flask import Flask, request
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
import anthropic

load_dotenv()

app = Flask(__name__)
claude = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from .env automatically

SYSTEM_PROMPT = (
    "You are a helpful assistant replying over WhatsApp. "
    "Keep your answers short and conversational, since they're read on a phone."
)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body", "")
    sender = request.form.get("From", "")
    print(f"Incoming from {sender}: {incoming_msg}")

    try:
        message = claude.messages.create(
            model="claude-haiku-4-5-20251001",   # swap to claude-sonnet-4-6 for a smarter bot
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": incoming_msg}],
        )
        reply_text = message.content[0].text
    except Exception as e:
        print(f"Claude error: {e}")
        reply_text = "Sorry, something went wrong on my end. Try again in a sec."

    print(f"Replying: {reply_text}")

    resp = MessagingResponse()
    resp.message(reply_text)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)