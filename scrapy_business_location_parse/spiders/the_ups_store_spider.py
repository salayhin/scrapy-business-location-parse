import scrapy, pdb, json
from scrapy_business_location_parse.items import TheUpsStore
from scrapy_business_location_parse.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import time


class SevenElevenSpider(scrapy.Spider):
    name = "the_ups_stores"
    url = SITE_URL + 'data/t/places#filters={"$and":[{"country":{"$eq":"US"}}]}&q=7-Eleven'

    start_urls = ['file:///projects/uw-projets/uw/scrapy-business-location-parse/data/the_ups_stores/the_ups_stores_data_01.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/the_ups_stores/the_ups_stores_data_02.json',
                  'file:///projects/uw-projets/uw/scrapy-business-location-parse/data/the_ups_stores/the_ups_stores_data_03.json']

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        for data in jsonresponse["response"]["data"]:

            the_ups_store_obj = TheUpsStore()
            the_ups_store_obj['factual_id'] = data['factual_id']
            the_ups_store_obj['name'] = data['name']
            the_ups_store_obj['address'] = data['address']
            the_ups_store_obj['locality'] = data['locality']
            the_ups_store_obj['region'] = data['region']
            the_ups_store_obj['post_code'] = data['postcode']
            the_ups_store_obj['country'] = data['country']
            the_ups_store_obj['tel'] = data['tel']
            the_ups_store_obj['website'] = data['website']
            the_ups_store_obj['latitude'] = data['latitude']
            the_ups_store_obj['longitude'] = data['longitude']
            the_ups_store_obj['category_labels'] = ', '.join(data['category_labels'][0])
            the_ups_store_obj['chain_name'] = data['chain_name']

            yield the_ups_store_obj

