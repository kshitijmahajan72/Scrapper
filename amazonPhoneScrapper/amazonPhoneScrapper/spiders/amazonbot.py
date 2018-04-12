# -*- coding: utf-8 -*-
import scrapy


class AmazonbotSpider(scrapy.Spider):
    name = 'amazonbot'
    allowed_domains = ['www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T3L4_w?rh=n%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_36%3A1318505031']
    start_urls = ['https://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T3L4_w?rh=n%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_36%3A1318505031/']

    def parse(self, response):
        #pass
        titles = response.css(".s-access-title::text").extract()
        price = response.css(".s-price::text").extract()

        for itm in zip(titles,price):
            data = {
            'Name' : itm[0],
            'Price' : itm[1],

            }
            yield data
