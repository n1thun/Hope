from foreclosurescraper.items import ForeclosureItem, ForeclosureHistoryItem, PersonItem
from scrapy.exceptions import CloseSpider

from api.models import Foreclosure, ForclosureStatusHistory, Person

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
        print("Getting listings")
        for href in response.xpath("//a/@href").extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_case)

    def parse_case(self, response):
        # Get case
        try:
            print("Getting case")
            hxs = scrapy.Selector(response)
            listing_hxs = hxs.xpath('//table[contains(@class, "table-striped")][1]//tr/td[2]//text()')
            history_hxs = hxs.xpath('//table[contains(@class, "table-striped")][2]//tr')
            foreclosure_item = ForeclosureItem()
            foreclosure_item['address'] = listing_hxs[5].extract()
            foreclosure_item['city'] = listing_hxs[6].extract()[:-9]
            foreclosure_item['state'] = listing_hxs[6].extract()[-8:-6]
            foreclosure_item['zip'] = listing_hxs[6].extract()[-5:]
            foreclosure_item['deed_of_trust_amount'] = listing_hxs[8].extract()
            foreclosure_item['sale_date'] = listing_hxs[2].extract()

            if not foreclosure_item['zip'].isnumeric():
                return
            if foreclosure_item['deed_of_trust_amount'].find("$") == -1:
                return

            f = Foreclosure.objects.create(**dict(foreclosure_item))
            f.save()
            raise CloseSpider("Check the database")


            total_history = []
            for history in history_hxs:
                if (history.xpath('td[1]/text()').extract()) == "Status":  # Header
                    continue
                history_item = ForeclosureHistoryItem()
                history_item['status'] = history.xpath('td[1]/text()').extract()
                history_item['date'] = history.xpath('td[2]/text()').extract()

                if history_item['date'] == []:
                    continue

                total_history.append(dict(history_item))

            person_item = PersonItem()
            person_item['name'] = self.fix_name(listing_hxs[4].extract())

            foreclosure_item['defendant'] = dict(person_item)
            foreclosure_item['foreclosure_history'] = total_history

            yield foreclosure_item
        except:
            return

    @staticmethod
    def fix_name(name):
        return name.replace(" ET AL", "")
