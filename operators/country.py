import os
import time
from config import Config
from controller.webscraping import WebScrapingController
from models.country import Country
from operators.utils import Utils

logger = Config.LOGGER.value


class CountryOperator:
    def __init__(self, web_scraping_operator: WebScrapingController, filename: str):
        self.web_scraping_operator = web_scraping_operator
        self.current_path = Config.CURRENT_PATH.value
        self.filename = filename
        self.url = web_scraping_operator.url

    def ProcessScraping(self) -> bool:
        soup = self.web_scraping_operator.GetPageResponse()
        results = self.web_scraping_operator.getHTMLValuesByTag(
            soup=soup, tag_name="section", tag_attribute="id", tag_value="countries"
        )

        countries = results.find_all("div", class_="col-md-4 country")

        countries_objects = []
        for country in countries:
            name = self.web_scraping_operator.getHTMLValuesByTag(
                soup=country,
                tag_name="h3",
                tag_attribute="class",
                tag_value="country-name",
            )
            capital = self.web_scraping_operator.getHTMLValuesByTag(
                soup=country,
                tag_name="span",
                tag_attribute="class",
                tag_value="country-capital",
            )
            population = self.web_scraping_operator.getHTMLValuesByTag(
                soup=country,
                tag_name="span",
                tag_attribute="class",
                tag_value="country-population",
            )
            area = self.web_scraping_operator.getHTMLValuesByTag(
                soup=country,
                tag_name="span",
                tag_attribute="class",
                tag_value="country-area",
            )

            countries_objects.append(
                Country(
                    name=name.text.strip(),
                    capital=capital.text.strip(),
                    population=population.text.strip(),
                    area=area.text.strip(),
                ).to_dict()
            )

        Utils.listToCsv(countries_objects, self.current_path, self.filename)

        if os.path.isfile(f"{self.current_path}/{self.filename}"):
            logger.info(f"File {self.filename} created/updated!")
            return True
        else:
            return False

    def ProcessWithRetry(self):
        for attempt in range(Config.ATTEMPTS.value):
            log_attempt = f"[attempt: {attempt}]"
            logger.info(
                f"{log_attempt} - Starting scraping on site [{self.url}] and creating csv"
            )

            try:
                processed = self.ProcessScraping()
                if processed:
                    logger.info(
                        f"{log_attempt} - Finishing scraping on site [{self.url}] and creating csv"
                    )
            except Exception as e:
                logger.error(f"{log_attempt} - {e} - Scraping Error")
                time.sleep(Config.RETRY_TIME.value)
                continue
            else:
                break
