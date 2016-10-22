__author__ = 'Jonathan Morton'
import scrapy

__author__ = 'Jonathan Morton'


class CivilViewSpider(scrapy.Spider):
    name = "civil"
    allowed_domains = ['civilview.com']
    start_urls = ['https://salesweb.civilview.com/']
    items = []

    def parse(self, response):
        # Get initial counties
        for href in response.xpath("//a/@href").extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_listing_table)

    def parse_listing_table(self, response):
        # Get details
        for href in response.xpath("//a/@href"):
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_case)

    def parse_case(self, response):
        # Get case
        # Todo create items from Django model
        return
