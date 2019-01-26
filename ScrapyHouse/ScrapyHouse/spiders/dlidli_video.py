import re

import pymysql as pymysql
import scrapy

# jojo地址
url = "http://www.dilidili.wang/anime/jojo/"

# db = pymysql.connect("192.168.1.13", "root", "", "carton", charset="utf8")
# cursor = db.cursor()


class DilidiliVideo(scrapy.Spider):
    name = "dilidili"
    box = [url]
    start_urls = box

    def __init__(self):
        print("初始化dilidili")

    def parse(self, response):
        source = response.xpath('//div[@class="swiper-slide"]/ul')

        # self.InsertIntoDB("1", "1", "1", "1", "1")
        for c in source:
            source_ul = c.xpath("li").extract()
            for d in source_ul:
                rex_url = r'<a.*? href="(.*?)".*?>.*?</a>'
                rex_title=r'<em.*?>(.*?)</em>'
                rex_num = r'<span.*?>(.*?)</span>'
                result=re.search(rex_url,d)
                result_title =re.search(rex_title,d)
                result_num = re.search(rex_num,d)

                # self.InsertIntoDB("",result_title.group(1).strip('<span>').replace("</span>",""),result.group(1),"0",result_num.group(1))


            break
    #
    # def InsertIntoDB(self, arg1, arg2, arg3, arg4, arg5):
    #
    #     insertSql = 'insert into video (play_address,video_name,video_address,video_category,video_episode) values ("%s","%s","%s","%s","%s")' % (
    #         arg1, arg2, arg3, arg4, arg5)
    #
    #     try:
    #         cursor.execute(insertSql)
    #         db.commit()
    #         print("提交成功！")
    #
    #     except:
    #         db.rollback()
    #         print("提交失败",insertSql)
    #
    # def ConnectMyDB(self):
    #     sqlStr = "select * from conker"
    #     cursor.execute(sqlStr)
    #     fetch = cursor.fetchone()
    #     print(fetch)
