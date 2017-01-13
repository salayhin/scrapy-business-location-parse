import scrapy, pdb, json
from scrapy_business_location_parse.items import McDonald
from scrapy_business_location_parse.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import time


class SevenElevenSpider(scrapy.Spider):
    name = "mc_donalds"
    url = SITE_URL + 'data/t/places#filters={"$and":[{"country":{"$eq":"US"}}]}&q=7-Eleven'

    start_urls = ['file:///projects/uw-projets/uw/scrapy-business-location-parse/data/mc_donalds/mc_donalds_data_01.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/mc_donalds/mc_donalds_data_02.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/mc_donalds/mc_donalds_data_03.json']

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        for data in jsonresponse["response"]["data"]:

            mc_donald_obj = McDonald()
            mc_donald_obj['factual_id'] = data['factual_id']
            mc_donald_obj['name'] = data['name']
            mc_donald_obj['address'] = data['address']
            mc_donald_obj['locality'] = data['locality']
            mc_donald_obj['region'] = data['region']
            mc_donald_obj['post_code'] = data['postcode']
            mc_donald_obj['country'] = data['country']
            mc_donald_obj['tel'] = data['tel']
            mc_donald_obj['website'] = data['website']
            mc_donald_obj['latitude'] = data['latitude']
            mc_donald_obj['longitude'] = data['longitude']
            mc_donald_obj['category_labels'] = ', '.join(data['category_labels'][0])
            mc_donald_obj['chain_name'] = data['chain_name']

            yield mc_donald_obj

