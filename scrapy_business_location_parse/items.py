# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SevenEleven(scrapy.Item):
    factual_id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    post_code = scrapy.Field()
    country = scrapy.Field()
    neighborhood = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    hours_of_operations = scrapy.Field()
    category_labels = scrapy.Field()
    chain_name = scrapy.Field()


class McDonald(scrapy.Item):
    factual_id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    post_code = scrapy.Field()
    country = scrapy.Field()
    neighborhood = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    hours_of_operations = scrapy.Field()
    category_labels = scrapy.Field()
    chain_name = scrapy.Field()


class DunkinDonut(scrapy.Item):
    factual_id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    post_code = scrapy.Field()
    country = scrapy.Field()
    neighborhood = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    hours_of_operations = scrapy.Field()
    category_labels = scrapy.Field()
    chain_name = scrapy.Field()


class TheUpsStore(scrapy.Item):
    factual_id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    post_code = scrapy.Field()
    country = scrapy.Field()
    neighborhood = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    hours_of_operations = scrapy.Field()
    category_labels = scrapy.Field()
    chain_name = scrapy.Field()


class JimmyJohnsGourmetSandwich(scrapy.Item):
    factual_id = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    post_code = scrapy.Field()
    country = scrapy.Field()
    neighborhood = scrapy.Field()
    tel = scrapy.Field()
    website = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    hours_of_operations = scrapy.Field()
    category_labels = scrapy.Field()
    chain_name = scrapy.Field()