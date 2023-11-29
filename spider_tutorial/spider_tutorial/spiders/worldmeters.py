import scrapy


class WorldmetersSpider(scrapy.Spider):
    name = "worldmeters"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # title=response.xpath("//h1/text()").get()
        countries=response.xpath("//td/a")
        for counry in countries:
            country_name=counry.xpath(".//text()").get()
            link = counry.xpath(".//@href").get()
            
            #absoulte_url
            # absolute_url = f'https://ww.worldometers.info/{link}'
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)
           
            #relative url
            yield response.follow(url=link,callback=self.parse_contry,meta={"country":country_name}) 
            
            # {
            #     'country_name' : country_name,
            #     "link": link
            # }
            
    def parse_contry(self,response):
        # response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        country = response.request.meta['country']
        rows=response.xpath("(//table[contains(@class,'table')])[1]/tbody/tr")
        
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            
            yield{
                "country" :country,
                "year": year,
                "population":population
            }