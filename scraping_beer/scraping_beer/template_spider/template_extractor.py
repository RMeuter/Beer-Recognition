import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BeerItem

class MySpider(CrawlSpider):
    name = 'url'
    allowed_domains = ['myUrl.fr']
    start_urls = ['https://www.myUrl.fr/']
    
    custom_settings = {
        "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagesPipeline': 1},
        "IMAGES_STORE": 'data/myUrl', 
    }
    rules = (
        
        Rule(LinkExtractor(allow=('reg-extractor-link', )), callback='parse_product'),
    )

    def parse_product(self, response):
        beers = response.css("li.product")
        for b in beers:
            img_url = b.css("img.front-image::attr('src')").extract()
            
            beer = BeerItem()
            beer["image_name"] = b.css("img::attr('title')").get()
            beer["image_urls"] = [response.urljoin(img_url[0])]
            beer["price"] = b.css("div.price::text").get()
            beer["tag"] = b.css("div.manufacturer::text").getall()
            yield beer

        self.log(f'Count beer {str(len(beers))}')