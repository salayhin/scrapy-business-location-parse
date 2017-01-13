import scrapy, pdb, json
from scrapy_business_location_parse.items import JimmyJohnsGourmetSandwich
from scrapy_business_location_parse.config import SITE_URL
from scrapy.selector import HtmlXPathSelector
import time


class SevenElevenSpider(scrapy.Spider):
    name = "jimmy_johns_gourmet_sandwiches"
    url = SITE_URL + 'data/t/places#filters={"$and":[{"country":{"$eq":"US"}}]}&q=7-Eleven'

    start_urls = ['file:///projects/uw-projets/uw/scrapy-business-location-parse/data/jimmy_johns_gourmet_sandwiches/jimmy_johns_gourmet_sandwiches_data_01.json']

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())

        for data in jsonresponse["response"]["data"]:

            jimmy_johns_gourmet_sandwich_obj = JimmyJohnsGourmetSandwich()
            jimmy_johns_gourmet_sandwich_obj['factual_id'] = data['factual_id']
            jimmy_johns_gourmet_sandwich_obj['name'] = data['name']
            jimmy_johns_gourmet_sandwich_obj['address'] = data['address']
            jimmy_johns_gourmet_sandwich_obj['locality'] = data['locality']
            jimmy_johns_gourmet_sandwich_obj['region'] = data['region']
            jimmy_johns_gourmet_sandwich_obj['post_code'] = data['postcode']
            jimmy_johns_gourmet_sandwich_obj['country'] = data['country']
            jimmy_johns_gourmet_sandwich_obj['tel'] = data['tel']
            #jimmy_johns_gourmet_sandwich_obj['website'] = data['website']
            jimmy_johns_gourmet_sandwich_obj['latitude'] = data['latitude']
            jimmy_johns_gourmet_sandwich_obj['longitude'] = data['longitude']
            jimmy_johns_gourmet_sandwich_obj['category_labels'] = ', '.join(data['category_labels'][0])
            #jimmy_johns_gourmet_sandwich_obj['chain_name'] = data['chain_name']

            yield jimmy_johns_gourmet_sandwich_obj

