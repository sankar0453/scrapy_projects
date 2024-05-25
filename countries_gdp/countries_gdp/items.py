# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose

#ItemLoader describes the process ,how will the loaded on to the Item



#Item describes the structure
class CountriesGdpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    country_name = scrapy.Field()
    gdp_nominal = scrapy.Field()
    region = scrapy.Field()
    year = scrapy.Field()
