import os
import sys
import unittest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from operators.webscraping import WebScrapingOperator
from controller.webscraping import WebScrapingController
from operators.country import CountryOperator


class TestSum(unittest.TestCase):
    def test_get_response(self):
        controller = WebScrapingController("https://www.google.com")
        self.assertEqual(controller.GetResponse().ok, True, "Must be a response")

    def test_get_page_response(self):
        controller = WebScrapingController("https://www.google.com")
        soup = WebScrapingOperator(controller.url).GetPageResponse().find("div")
        self.assertEqual(
            "div" in [tag.name for tag in soup.find_all()],
            True,
            "Must be a BeautifulSoup",
        )

    def test_get_html_value_by_tag(self):
        controller = WebScrapingController("https://www.google.com")
        soup = WebScrapingOperator(controller.url).GetPageResponse()

        page = WebScrapingOperator(controller.url).getHTMLValuesByTag(
            soup, "b", "class", "gb1"
        )
        self.assertEqual(
            page.text.strip() == "Pesquisa", True, "Must be a BeautifulSoup"
        )

    def test_process_scraping(self):
        controller = WebScrapingController(
            "https://www.scrapethissite.com/pages/simple/"
        )
        web_scraping_operator = WebScrapingOperator(controller.url)

        process = CountryOperator(web_scraping_operator, "teste.csv").ProcessScraping()
        self.assertEqual(process, True, "Must be a BeautifulSoup")


if __name__ == "__main__":
    unittest.main()
