import scrapy
from ..items import AmazonscrapeItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ['https://www.amazon.com/b/?ie=UTF8&node=16857165011&ref_=sv_b_3']

    def parse(self, response):
        items = AmazonscrapeItem()

        product_name = response.css('.acs-product-block__product-title .a-truncate-full::text').extract()
        product_author = response.css('.acs-product-block__contributor .a-truncate-full').css('::text').extract()
        product_price = response.css('.acs-product-block__price').css('::text').extract()
        product_imagelink = response.css('.acs-product-block__product-image::attr(src)').extract()
        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items