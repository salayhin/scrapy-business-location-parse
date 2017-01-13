import scrapy, pdb, json
from scrapy_business_location_parse.items import DunkinDonut
from scrapy_business_location_parse.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import time


class SevenElevenSpider(scrapy.Spider):
    name = "dunkins_donuts"
    url = SITE_URL + 'data/t/places#filters={"$and":[{"country":{"$eq":"US"}}]}&q=7-Eleven'

    start_urls = ['file:///projects/uw-projets/uw/scrapy-business-location-parse/data/dunkins_donuts/dunkins_donuts_data_01.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/dunkins_donuts/dunkins_donuts_data_02.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/dunkins_donuts/dunkins_donuts_data_03.json']

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        for data in jsonresponse["response"]["data"]:

            dunkins_donut_obj = DunkinDonut()
            dunkins_donut_obj['factual_id'] = data['factual_id']
            dunkins_donut_obj['name'] = data['name']
            dunkins_donut_obj['address'] = data['address']
            dunkins_donut_obj['locality'] = data['locality']
            dunkins_donut_obj['region'] = data['region']
            dunkins_donut_obj['post_code'] = data['postcode']
            dunkins_donut_obj['country'] = data['country']
            dunkins_donut_obj['tel'] = data['tel']
            dunkins_donut_obj['website'] = data['website']
            dunkins_donut_obj['latitude'] = data['latitude']
            dunkins_donut_obj['longitude'] = data['longitude']
            dunkins_donut_obj['category_labels'] = ', '.join(data['category_labels'][0])
            dunkins_donut_obj['chain_name'] = data['chain_name']

            yield dunkins_donut_obj

