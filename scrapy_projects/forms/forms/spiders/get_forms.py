import scrapy


class GetFormsSpider(scrapy.Spider):
    name = 'get_forms'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/']

    def parse(self, response):
        pass
