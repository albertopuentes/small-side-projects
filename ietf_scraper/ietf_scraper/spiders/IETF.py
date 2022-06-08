import scrapy


class IetfSpider(scrapy.Spider):
    name = 'IETF'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #css example: title = response.css('span.title::text').get()
        #xpath example:
        title = response.xpath('//span[@class="subheading"]/text()').getall()
        return {"title": title}
