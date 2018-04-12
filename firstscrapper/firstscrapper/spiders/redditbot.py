# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']

    def parse(self, response):
        #extracts the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        time = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        #creating dictionary of extracted content
        for items in zip(titles,votes,time,comments):
            data={
            'title' : items[0],
            'votes' : items[1],
            'created' : items[2],
            'comments' : items[3],
            }
            #give the scrapped info to scrapy
            yield data
