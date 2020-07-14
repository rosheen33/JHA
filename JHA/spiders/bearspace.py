# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider
from w3lib.url import add_or_replace_parameter

from JHA.items import ArtWorkItem


class BearspaceSpider(CrawlSpider):
    name = 'bearspace'
    allowed_domains = ['bearspace.co.uk']
    start_urls = ['https://www.bearspace.co.uk/purchase']

    # rules = (
    #     Rule(
    #         SgmlLinkExtractor(restrict_css='[data-hook=product-list-grid-item]'),
    #         follow=True, callback='parse_item'
    #     ),
    # )

    def parse(self, response):
        links = response.css('[data-hook=product-list-grid-item] a::attr(href)').getall()
        for l in links:
            yield Request(l, callback=self.parse_item)

        if response.css('[data-hook=load-more-button]'):
            page_no = response.meta.get('page', 1) + 1
            next_page_url = add_or_replace_parameter(response.url, 'page', page_no + 1)
            yield Request(next_page_url, callback=self.parse, meta={'page': page_no})

    def parse_item(self, response):
        item_loader = ItemLoader(item=ArtWorkItem(), response=response)
        item_loader.add_value('url', response.url)
        item_loader.add_css('title', 'h1[data-hook=product-title]::text')
        item_loader.add_css('media', '[data-hook=magic-zoom-link]::attr(href)')
        item_loader.add_css('price_gbp', '[data-hook=formatted-primary-price] ::text')

        description = response.css('[data-hook=description] ::text').re_first(
            '\d+[cm|CM|cms]*\s*[x|X]\s*[width]*\s*\d+[cm|CM|cms]*'
        )
        item_loader.add_value('height_cm', description)
        item_loader.add_value('width_cm', description)

        yield item_loader.load_item()
