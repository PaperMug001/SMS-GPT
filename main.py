from LibreSMS import LibreSMS
import os
import time
from dotenv import load_dotenv
from openrouter_h import ask_ai
from commands import *

load_dotenv()

BASE = os.getenv("BASE")
TOKEN = os.getenv("TOKEN")

sms = LibreSMS(BASE, TOKEN)

PROCESSING = False
PIN = os.getenv("PIN")

commands = ["ai", "wh"]


def handle_message(message):
    global PROCESSING

    sender = message.get("sender")
    text = message.get("message", "").strip()

    if PROCESSING:
        sms.send(sender, "Cannot execute. Another command is currently running.")
        return

    PROCESSING = True

    try:
        # Split command and arguments
        parts = text.split(" ", 2)

        if len(parts) < 2:
            return

        command = parts[0].lower()
        pin = parts[1]

        # Check PIN
        if pin != PIN:
            print("Invalid PIN")
            return

        # Get remaining message after command + pin
        args = parts[2] if len(parts) > 2 else ""

        # Execute command
        if command == "ai":
            handle_ai(sender, args, sms)

        elif command == "wh":
            # handle_wh(sender, args, sms)
            print("Weather is hot here")

        else:
            print("Unknown command:", command)

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

                if messages:
                    for msg in messages:
                        handle_message(msg)
            else:
                print("SMS retrieval failed:", response)

        except Exception as e:
            print("Polling error:", e)

        time.sleep(2)


if __name__ == "__main__":
    print("SMS Command started...")
    poll_sms()