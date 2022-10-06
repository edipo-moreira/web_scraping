from bs4 import BeautifulSoup

from controller.webscraping import WebScrapingController


class WebScrapingOperator:
    def __init__(self, url):
        self.url = url

    def GetPageResponse(self) -> BeautifulSoup:
        response = WebScrapingController(url=self.url).GetResponse()
        return BeautifulSoup(response.content, "html.parser")

    def getHTMLValuesByTag(
        self, soup: BeautifulSoup, tag_name: str, tag_attribute: str, tag_value: str
    ):
        return soup.find(tag_name, {tag_attribute: tag_value})
