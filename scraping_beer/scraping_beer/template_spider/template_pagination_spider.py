import json
from ..items import BeerItem

import scrapy
 
class UrlCrawler(scrapy.Spider):
    name = "url"
    start_urls = ['https://www.myUrl.com']
    
    custom_settings = {
        "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagesPipeline': 1},
        "IMAGES_STORE": 'data/myUrl', 
    }

    def parse(self, response):
        beers = response.css("div.pro_outer_box")
        for b in beers:
                img_url = b.css("img::attr('src')").extract()
                name = b.css("img::attr('title')").get()
                
                beer = BeerItem()
                if name != None:
                    beer["image_name"] = name 
                    beer["image_urls"] = [response.urljoin(img_url[0])]
                    beer["price"] = b.css("span.price::text").get()
                    beer["tag"] = b.css("p.manufacturer::text").getall()
                    yield beer
 
        NEXT_PAGE_SELECTOR = "li.pagination_next > a::attr('href')"
        next_page = response.css(NEXT_PAGE_SELECTOR).extract()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page[-1]),
                callback=self.parse
            )