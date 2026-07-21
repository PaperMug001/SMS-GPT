import requests

class LibreSMS:

    def __init__(self, base, token):
        self.base = base
        self.headers = {
            "Authorization": token
        }

    def send(self, to, message):
        return requests.post(
            f"{self.base}/sendsms",
            headers=self.headers,
            json={
                "to": to,
                "message": message
            }
        )

    def receive(self):
        return requests.get(
            f"{self.base}/getmessages",
            headers=self.headers
        ).json()