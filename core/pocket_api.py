import requests

class PocketAPI:
    def __init__(self, email, password):
        self.session = requests.Session()
        self.email = email
        self.password = password
        self.token = None

    def login(self):
        r = self.session.post(
            "https://api.pocketoption.com/login",
            json={"email": self.email, "password": self.password}
        )
        if r.status_code == 200 and r.json().get("token"):
            self.token = r.json()["token"]
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})
            return True
        return False

    def trade(self, asset, amount, direction, duration):
        payload = {
            "asset": asset,
            "amount": amount,
            "action": direction,
            "duration": duration
        }
        r = self.session.post("https://api.pocketoption.com/trade", json=payload)
        return r.json()
