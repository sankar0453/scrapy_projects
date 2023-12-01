import scrapy


class EuroTrialsSpider(scrapy.Spider):
    name = "euro_trials"
    allowed_domains = ["www.clinicaltrialsregister.eu"]
    start_urls = ["https://www.clinicaltrialsregister.eu/ctr-search/search?query="]

    def parse(self, response):
        pass
