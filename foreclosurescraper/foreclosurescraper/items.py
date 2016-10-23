# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class ForeclosureItem(Item):
    defendant = Field() #A PersonItem
    address = Field()
    sale_date = Field()
    city = Field()
    state = Field()
    zip = Field()
    deed_of_trust_amount = Field()
    foreclosure_history = Field() #Array of ForeclosureHistoryItems

class PersonItem(Item):
    name = Field()
    address = Field()
    city = Field()
    state = Field()
    zip = Field()
    age = Field()
    date_of_birth = Field()
    in_continuum_of_care = Field()
    in_shelter = Field()

class ForeclosureHistoryItem(Item):
    status = Field()
    date = Field()



