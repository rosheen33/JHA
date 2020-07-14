# -*- coding: utf-8 -*-
import scrapy


class ChristiesSpider(scrapy.Spider):
    name = 'christies'
    allowed_domains = ['christies.com']
    start_urls = ['https://www.christies.com/lotfinder/Lot/peter-doig-b-1959-the-architects-home-5973059-details.aspx']

    def parse(self, response):
        item = {}
        item['artist'] = ' '.join(response.css('.lotName ::text').getall()).strip()
        item['title'] = response.css('.itemName ::text').get()
        item['price_gpb'] = response.css('#main_center_0_lblPriceRealizedPrimary::text').get().strip('GBP')
        item['price_usd'] = response.css('#main_center_0_lblPriceRealizedSecondary::text').get()
        item['price_est_gpb'] = response.css('#main_center_0_lblPriceEstimatedPrimary::text').get().replace('GBP', '')
        item['price_est_usd'] = response.css('#main_center_0_lblPriceEstimatedSecondary::text').get()
        item['image'] = response.css('#imgLotImage::attr(src)').get()
        item['sel_date'] = response.css('#main_center_0_lblSaleDate ::text').get()
        yield item
