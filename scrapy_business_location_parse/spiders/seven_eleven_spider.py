import scrapy, pdb, json
from scrapy_business_location_parse.items import SevenEleven
from scrapy_business_location_parse.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import time


class SevenElevenSpider(scrapy.Spider):
    name = "seven_eleven"
    url = SITE_URL + 'data/t/places#filters={"$and":[{"country":{"$eq":"US"}}]}&q=7-Eleven'

    start_urls = ['file:///projects/uw-projets/uw/scrapy-business-location-parse/data/seven_eleven/seven_eleven_data_01.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/seven_eleven/seven_eleven_data_02.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/seven_eleven/seven_eleven_data_03.json']

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        for data in jsonresponse["response"]["data"]:

            seven_obj = SevenEleven()
            seven_obj['factual_id'] = data['factual_id']
            seven_obj['name'] = data['name']
            seven_obj['address'] = data['address']
            seven_obj['locality'] = data['locality']
            seven_obj['region'] = data['region']
            seven_obj['post_code'] = data['postcode']
            seven_obj['country'] = data['country']
            seven_obj['tel'] = data['tel']
            seven_obj['website'] = data['website']
            seven_obj['latitude'] = data['latitude']
            seven_obj['longitude'] = data['longitude']
            seven_obj['category_labels'] = ', '.join(data['category_labels'][0])
            seven_obj['chain_name'] = data['chain_name']

            yield seven_obj

