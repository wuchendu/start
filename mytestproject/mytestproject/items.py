# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MytestprojectItem(scrapy.Item):
    #图片路径
    img_url = scrapy.Field()
    #电影名称
    video_name = scrapy.Field()
    #电影评分
    video_num = scrapy.Field()

    #导演姓名
    director = scrapy.Field()
