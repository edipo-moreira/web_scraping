import requests


class WebScrapingController:
    def __init__(self, url):
        self.url = url

    def GetResponse(self) -> requests.Response:
        return requests.get(self.url)
