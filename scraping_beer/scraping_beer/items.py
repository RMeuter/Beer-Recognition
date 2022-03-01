# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeerItem(scrapy.Item):
    # define the fields for your item here like:
    # https://www.geeksforgeeks.org/how-to-download-files-with-scrapy/
    image_name  = scrapy.Field()
    tag   = scrapy.Field()
    price = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
