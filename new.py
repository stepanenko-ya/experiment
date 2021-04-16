import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
#
# main_r = requests.get("http://www.freeproxylists.net/ru/",
#                       headers={"user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'})
# print(main_r.status_code)
# soup = BeautifulSoup(main_r.content, "html.parser")
res = [{'http': 'http://148.72.152.156:3128', 'https': 'http://148.72.152.156:3128'}, {'http': 'http://3.141.186.75:3128', 'https': 'http://3.141.186.75:3128'}, {'http': 'http://45.153.33.166:3128', 'https': 'http://45.153.33.166:3128'}, {'http': 'http://132.248.196.2:8080', 'https': 'http://132.248.196.2:8080'}, {'http': 'http://176.113.73.97:3128', 'https': 'http://176.113.73.97:3128'}]
with open("zzz.txt", "w") as f:
    print(type(str(res)))
    # for r in res:
    #     # print(type(str(r)))
    #
    f.write("" + str(res) + "")
