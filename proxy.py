import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random


url = 'https://www.myxa.com.ua/srs/get-ip/'

# header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
# # proxy = {'http': 'http://188.190.255.14:8085', 'https': 'http://188.190.255.14:8085'}
#
# proxy = {'http': "socks5://192.111.139.165:19402", 'https': "socks5://192.111.139.165:19402"}
res = [{'http': 'http://148.72.152.156:3128', 'https': 'http://148.72.152.156:3128'}, {'http': 'http://3.141.186.75:3128', 'https': 'http://3.141.186.75:3128'}, {'http': 'http://45.153.33.166:3128', 'https': 'http://45.153.33.166:3128'}, {'http': 'http://132.248.196.2:8080', 'https': 'http://132.248.196.2:8080'}, {'http': 'http://176.113.73.97:3128', 'https': 'http://176.113.73.97:3128'}]

r = requests.get(url, headers={"User-Agent": UserAgent().chrome}, proxies=random.choice(res))

# # r = requests.get(url, headers={"User-Agent": UserAgent().chrome}, proxies=proxy, verify=False)
#
print(r.status_code)
print(r.text)
    # soup = BeautifulSoup(r.content, "html.parser")
    # finders = soup.find_all(class_='')
    # for finder in finders:
    #
    #     f = finder.find().get()
    #     print(f)


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')









