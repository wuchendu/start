# -*- coding: utf-8 -*-
import scrapy


class DianyingSpider(scrapy.Spider):
    name = 'dianying'
    allowed_domains = ['http://www.id97.com/movie/']
    start_urls = ['http://www.id97.com/movie/']
    page = 1
    #parse方法就是将解析当前页的数据，解析完成后提交一个新页给引擎，引擎又封装一个request对象，传入response，再去解析新页
    def parse(self, response):
        data_list = response.xpath('//div[@class="col-xs-12"]/div/div[@class="movie-item-in"]')


        #此处的for循环是解决一页数据的抓取解析的功能
        for data in data_list:
            item = {}
            video_name = data.xpath('./a/@title').extract_first()
            img_url = data.xpath('./a/img[@class="lazy"]/@data-original').extract_first()
            video_num = data.xpath('./div/h1/em/text()').extract_first()
            #解析电影详细页面的网址
            detail_url = data.xpath('./a/@href').extract_first()
            item = {
                'video_name':video_name,
                'img_url':img_url,
                'video_num':video_num,
            }
            # 此时item是不完整的不能获取详细页面的电影信息导演信息，所以注释不回传item
            #所以再次请求Request 让引擎去回掉 callback self.parse_info 函数 meta 传递 item 给到 函数中
            # yield item
            yield scrapy.Request(url =detail_url,callback=self.parse_info,dont_filter=True,meta={'item':item})

        #解析一页数据之后，在把新的网址传给引擎
        # 1.先确定要提交的网址是什么
        #     http://www.id97.com/movie/   +  下一页的参数  ?page=
        if self.page <2:
            self.page += 1
            next_url = 'http://www.id97.com/movie/' + '?page=' + str(self.page)
            # 2把url提交给引擎
            # url 表示的是下一页爬取网页的地址， callback 回调的函数 dont_filter 设置不过滤次网址
            #
            yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=True)

    def parse_info(self,response):

        item = response.meta['item']

        director = response.xpath("//div[@class='col-xs-9 movie-info padding-right-5']//div[@class='row']/div[2]/table/tbody/tr[1]/td[2]/a/text()").extract_first()

        item['director'] = director

        yield item
