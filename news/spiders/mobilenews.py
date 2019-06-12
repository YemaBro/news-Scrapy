# -*- coding: utf-8 -*-
import scrapy
import re
import random
from news.items import MobileNewsItem


class MobileNews(scrapy.Spider):
    name = 'mobilenews'
    allowed_domains = ['www.cnmo.com']
    base_url = 'http://www.cnmo.com/phone/news/{page}/'

    def start_requests(self):
        for page in range(1, 10):
            url = self.base_url.format(page=page)
            yield scrapy.Request(url=url, callback=self.parse_info, dont_filter=True)

    def parse_info(self, response):
        news = response.css('.listbox .libox .txtbox')
        for new in news:
            item = MobileNewsItem()
            item['url'] = new.css("a::attr(href)").extract_first()
            id_l = re.findall('\d+', item['url'])
            item['id'] = id_l[0]
            item['title'] = new.css("a h2::text").extract_first()
            item['intro'] = new.css("a p::text").extract_first()
            item['view_count'] = random.randint(99, 9999)
            item['comment_num'] = random.randint(22, 2222)
            item['tags'] = new.css(".botbox ul li span a::text").extract()
            for i in range(len(item['tags'])):
                item['tags'][i] = item['tags'][i].strip()
            yield scrapy.Request(url=item['url'], callback=self.parse_detail, meta={'item': item}, dont_filter=True)

    def parse_detail(self, response):
        item = response.meta.get('item')
        # details = response.xpath("//div[@class='cpage']/div[@id='cleft']/")
        item['source'] = response.xpath("//div[@class='cpage']/div[@id='cleft']/div[@class='ctitle']/div[@class='ctitle_spe']/div[@class='fl']/span[@class='text_auther']/text()").get()
        item['publish_time'] = response.xpath("//div[@class='cpage']/div[@id='cleft']/div[@class='ctitle']/div[@class='ctitle_spe']/div[@class='fl']/span[3]/text()").get()
        item['content'] = ''.join(response.xpath("//div[@class='cpage']/div[@id='cleft']/div[@class='ctext']/p/text()").getall())
        yield item
