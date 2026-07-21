from LibreSMS import LibreSMS
import os
import time
from dotenv import load_dotenv
from openrouter_h import ask_ai

load_dotenv()

BASE = os.getenv("BASE")
TOKEN = os.getenv("TOKEN")

sms = LibreSMS(BASE, TOKEN)

PROCESSING = False
PIN = "jk1"

def handle_message(message):
    global PROCESSING

    PROCESSING = True

    try:
        sender = message.get("sender")
        text = message.get("message", "")

        command = f"ai {PIN} "

        if text.lower().startswith(command):
            reply = ask_ai(text[len(command):])
            sms.send(sender, reply)

    except Exception as e:
        print("Message handling error:", e)

    finally:
        PROCESSING = False

def poll_sms():
    while True:
        try:
            response = sms.receive()

            if response.get("Success") and response.get("Data"):
                messages = response["Data"].get("messages", [])

                if messages and not PROCESSING:
                    for msg in messages:
                        handle_message(msg)

                else:
                    print("No new messages")

            else:
                print("SMS retrieval failed:", response)

        except Exception as e:
            print("Polling error:", e)

        time.sleep(2)


if __name__ == "__main__":
    print("SMS bot started...")
    poll_sms()