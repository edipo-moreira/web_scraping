import logging
import time
from config import Config
from operators.webscraping import WebScrapingOperator
from operators.country import CountryOperator


def main():
    url = "https://www.scrapethissite.com/pages/simple/"
    filename = "scrapethissite.csv"

    web_scraping_operator = WebScrapingOperator(url)
    CountryOperator(web_scraping_operator, filename).ProcessWithRetry()


if __name__ == "__main__":
    main()
