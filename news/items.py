# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentNews(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    intro = scrapy.Field()
    view_count = scrapy.Field()
    comment_num = scrapy.Field()
    publish_time = scrapy.Field()
    update_time = scrapy.Field()
    source = scrapy.Field()
    tags = scrapy.Field()
    vurl = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()


class MobileNewsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    intro = scrapy.Field()
    view_count = scrapy.Field()
    comment_num = scrapy.Field()
    publish_time = scrapy.Field()
    source = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()