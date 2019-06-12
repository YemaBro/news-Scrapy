# -*- coding: utf-8 -*-
import scrapy
from news.items import TencentNews
import json


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    # allowed_domains = ['news.qq.com']
    base_url = 'https://pacaio.match.qq.com/irs/rcd?cid=108&ext=&token=349ee24cdf9327a050ddad8c166bd3e3&page='

    def start_requests(self):
        for page in range(0, 9):
            url = self.base_url + str(page)
            yield scrapy.Request(url=url, callback=self.parse_info, dont_filter=True)

    def parse_info(self, response):
        news = json.loads(response.text).get('data')
        for new in news:
            item = TencentNews()
            item['id'] = new.get('id')
            item['title'] = new.get('title')
            item['intro'] = new.get('intro')
            item['view_count'] = new.get('view_count')
            item['comment_num'] = new.get('comment_num')
            item['publish_time'] = new.get('publish_time')
            item['update_time'] = new.get('update_time')
            item['source'] = new.get('source')
            item['tags'] = [tag for tag, i in new.get('tag_label')]
            item['vurl'] = new.get('vurl')
            item['category'] = [new.get('category1_chn'), new.get('category2_chn'), new.get('category_chn')]
            content_url = item['vurl']
            yield scrapy.Request(url=content_url,
                                 callback=self.parse_content,
                                 meta={'item': item})

    def parse_content(self, response):
        item = response.meta.get('item')
        item['content'] = ''.join(response.xpath("//div[@class='content-article']/p[@class='one-p']/text()").extract())
        yield item
