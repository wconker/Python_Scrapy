import scrapy
import requests

url = "http://web4.cartoonmad.com/home1367/4240/157/001.jpg"
# https://www.cartoonmad.com/comic/424000572018002.html

class DilidiliVideo(scrapy.Spider):
    name = "gf"
    box = [url]
    index_page = 1
    index_Charpest = 157
    start_urls = box

    def parse(self, response):
        print("爬取开始....")
        Contents = response.url

        if self.index_page > 18:
            self.index_page = 1
            self.index_Charpest += 1
            yield self.make_requests_from_url(
                'http://web4.cartoonmad.com/home1367/4240/{0}/001.jpg'.format(self.pars2str(self.index_Charpest)))
        else:
            res = requests.get(Contents)

            with open(self.pars2str(self.index_Charpest) + '00' + self.pars2str(self.index_page) + '.jpg', 'wb') as f:

                f.write(res.content)

            self.index_page += 1

            print(self.index_page)

            v_str = self.pars2str(self.index_page)

            formatUrl = 'http://web4.cartoonmad.com/home1367/4240/' + self.pars2str(
                self.index_Charpest) + '/{0}.jpg'.format(v_str)

            yield self.make_requests_from_url(formatUrl)

    def pars2str(self, num):
        if 0 < num < 10:
            return '00' + str(num)
        if 9 < num < 100:
            return '0' + str(num)
        if num > 99:
            return str(num)
