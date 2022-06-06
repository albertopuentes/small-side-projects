import scrapy


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['en.widipedia.org']
    start_urls = ['http://en.widipedia.org/']

    def parse(self, response):
        pass
