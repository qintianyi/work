# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem


class Sipder1Spider(scrapy.Spider):
    start_num = 19090
    diff_num = 10
    url = r'http://datachart.500.com/dlt/zoushi/newinc/jbzs_foreback.php?expect=all&from={}&to={}'

    name = 'sipder1'
    allowed_domains = ['datachart.500.com']
    # start_urls = ['http://datachart.500.com/dlt/']

    def start_requests(self):
        end_num = self.start_num + self.diff_num
        url = self.url.format(self.start_num, end_num)
        print(url)
        yield scrapy.Request(url=url, meta={'last_end_num': end_num}, callback=self.parse, dont_filter=False)

    def parse(self, response: scrapy.http.response.Response):

        last_end_num = response.meta['last_end_num']
        resutl = response.xpath("//table[@id='chartsTable']//tr")

        for tr in resutl:
            num = tr.xpath(".//td[contains(@class,'chartBall01')]/text()|.//td[contains(@class,'chartBall02')]/text()").extract()  # type:list
            if num is not None and len(num) > 0:

                # yield num
                qishu = tr.xpath("./td[1]/text()").extract_first()

                # print('期数：{} 号码{}'.format(qishu, num))
                item = MyscrapyItem()
                item['qishu'] = qishu
                item['num'] = num


                yield item
        if last_end_num < 19148:
            start_num = last_end_num + 1
            end_num = start_num + self.diff_num
            print(self.url.format(start_num, end_num))
            yield scrapy.Request(url=self.url.format(start_num, end_num), meta={'last_end_num': end_num}, callback=self.parse,  dont_filter=False)
