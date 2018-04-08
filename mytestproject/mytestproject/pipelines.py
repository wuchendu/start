# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request

class MytestprojectPipeline(object):
    #当启动程序是启动该方法，值启动一次
    def open_spider(self,spider):
        self.fp = open('idm97dianying.json','w',encoding='utf-8')
    #当程序结束的使用该方法
    def close_spider(self,spider):
        self.fp.close()

    #每次返回一个item这个方法就调用一次
    def process_item(self, item, spider):
        #此处的item参数就是dianying.py中parse方法返回的
        string = json.dumps(item,ensure_ascii=False)
        self.fp.write(string + '\n')

        #加入功能 下载图片
        # 每次传入的item就是一个电影信息，一个电影信息里面的img_url 从 item 读取即可
        img_url= item['img_url']
        #图片的名字也可以从item读取
        video_name = item['video_name']
        # print(img_url)
        # print(video_name[0])
        #变成图片的全路径
        img_path = r'C:\Users\Administrator\Desktop\1702\Spider Crawler\day07\image\\'+ video_name + '.jpg'
        # print(img_path)
        urllib.request.urlretrieve(img_url,img_path)
        return item
