# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SnpPerformanceItem(scrapy.Item):
    Number = scrapy.Field()
    Company = scrapy.Field()
    Symbol = scrapy.Field()
    YTD_Return = scrapy.Field()

