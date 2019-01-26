from time import sleep

import pymysql
import scrapy

db = pymysql.connect("192.168.1.13", "root", "", "carton", charset="utf8")
cursor = db.cursor()


class dilidili_paly_address(scrapy.Spider):
    name = "play_address"

    temUrl = []

    def __init__(self):
        print("")

    def start_requests(self):

        myUrl = self.getUrl()

        for c in myUrl:
            self.temUrl.append(str(c[0]))

        yield self.make_requests_from_url(self.temUrl[0])

    def getUrl(self):
        sql = "select video_address from video"
        try:
            cursor.execute(sql)
            address = cursor.fetchall()
        except:
            db.rollback()
            print("错误")
        return address

    def UpdateDB(self, url, temp):
        sql = 'UPDATE video set play_address ="%s"' % (url) + ' WHERE video_address = "%s"' % (temp)
        try:
            cursor.execute(sql)
            sleep(2)
            db.commit()
            print("成功", sql)
        except:
            print("失败", sql)
            db.rollback()

    def parse(self, response):
        my_Value = response.xpath("//iframe/@src").extract()[0]

        try:
            print(self.temUrl)
            self.UpdateDB(my_Value, self.temUrl[0])
            if len(self.temUrl) > 0:
                self.temUrl.pop(0)
                print(self.temUrl)
                yield self.make_requests_from_url(self.temUrl[0])

        except:
            print("结束")
