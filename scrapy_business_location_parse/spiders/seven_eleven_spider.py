import scrapy, pdb
from scrapy_business_location_parse.items import SevenEleven
from scrapy_business_location_parse.config import SITE_URL


class SevenElevenSpider(scrapy.Spider):
    name = "seven_eleven"
    url = SITE_URL + 'data/t/places#filters={"$and":[{"country":{"$eq":"US"}}]}&q=7-Eleven'
    start_urls = [url]

    print(start_urls)

    def parse(self, response):
        pdb.set_trace()

        for category in response.css('ul.categoryList li'):
            category_obj = SevenEleven()

            category_obj['name'] = category.css('div.bookSubjectCaption h2::text').extract_first()
            category_obj['url'] = SITE_URL + category.css('a::attr(href)').extract_first()

            yield category_obj

