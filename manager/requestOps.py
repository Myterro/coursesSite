from requests import Session


class RequestsOps:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = Session()
        self.session.auth = (self.username, self.password)

    def get(self, url):
        request = self.session.get(url)
        return request

    def post(self, url, json):
        request = self.session.post(url, json=json)
        return request
