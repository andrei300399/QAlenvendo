import requests


class ApiClient:
    def __init__(self, host):
        self.host = host

    def get(self, url, params):
        return requests.get(f"{self.host}/{url}", params)
