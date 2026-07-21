from openrouter_h import ask_ai

def handle_ai(sender, text, sms):
    reply = ask_ai(text)
    sms.send(sender, reply)