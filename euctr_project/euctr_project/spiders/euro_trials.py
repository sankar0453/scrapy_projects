import scrapy


class EuroTrialsSpider(scrapy.Spider):
    name = "euro_trials"
    allowed_domains = ["www.clinicaltrialsregister.eu"]
    start_urls = ["https://www.clinicaltrialsregister.eu/ctr-search/search?query=&page=4"]

    def parse(self, response):
        table_container = response.xpath('//div[contains(@class , "result")]/table')
        for table in table_container:
            eudract_number = table.xpath('.//span[contains(text(), "EudraCT Number")]/following-sibling::text()').get()
            protocol_elements = table.xpath('.//span[contains(text(), "Trial protocol")]/following-sibling::a')
            
            for protocol_element in protocol_elements:
                protocol_url = protocol_element.xpath('@href').get()
                
                if eudract_number  :
                    yield {
                        'EudraCT Number': eudract_number.strip(),
                        'Trial Protocol': protocol_url.strip(),
                    } 

 