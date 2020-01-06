# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyscrapyPipeline(object):
    def process_item(self, item, spider):

        print('期数：{} 号码{}'.format(item['qishu'], item['num']))
        return item
