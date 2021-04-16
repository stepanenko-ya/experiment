import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

class Proxy:
    proxy_url = "https://www.ip-adress.com/proxy-list"
    proxy_lst = []

    def __init__(self):
        r = requests.get(self.proxy_url, headers={"User-Agent": UserAgent().chrome})
        soup = BeautifulSoup(r.content, "html.parser")
        finder = soup.find('table').find('tbody').find_all("tr")
        for f in finder:
            ip = f.find("td").get_text()
            self.proxy_lst.append(ip)

    def pars_proxy(self):
        good_prox = []
        for pr in self.proxy_lst:
            prox= {'http': "http://" + pr, 'https': "http://" + pr}
            print(prox)
            try:
<<<<<<< HEAD
                main_r = requests.get("https://www.myxa.com.ua/srs/get-ip/", headers=header, proxies=prox)
                print(main_r)
=======
                test = requests.get("https://www.google.com", proxies=prox)

                if test.status_code == 200:
                    good_prox.append(prox)
>>>>>>> c4a334f879e11441710fb5847541b445da591b32
            except:
                continue
        return good_prox


def pars_main():
    res = [{'http': 'http://159.89.221.73:3128', 'https': 'http://159.89.221.73:3128'}, {'http': 'http://159.65.189.75:80', 'https': 'http://159.65.189.75:80'}, {'http': 'http://144.217.254.175:3128', 'https': 'http://144.217.254.175:3128'}, {'http': 'http://198.50.163.192:3129', 'https': 'http://198.50.163.192:3129'}, {'http': 'http://202.61.51.204:3128', 'https': 'http://202.61.51.204:3128'}, {'http': 'http://178.128.125.16:44417', 'https': 'http://178.128.125.16:44417'}, {'http': 'http://162.255.201.37:8080', 'https': 'http://162.255.201.37:8080'}, {'http': 'http://165.225.77.47:9400', 'https': 'http://165.225.77.47:9400'}]
    return res
# for i in res:

    #     yield i

#
# def pars_shop(ip):
#     print(ip)
#     try:
#         req = requests.get("https://www.work.ua/jobs-kyiv-it/?advs=1",
#                               headers={"User-Agent": UserAgent().chrome},
#                               proxies=ip)
#         soup = BeautifulSoup(req.content, "html.parser")
#         positions = soup.find_all("h2")
#         for one in positions:
#             position = one.find("a").get("title")
#             print(position)
#     except:
#         print("Ooops")
#

def pars_shop(ip):
    xxx = True
    while xxx:
        w = random.choice(ip)
        print(w)

        try:
            req = requests.get("https://www.work.ua/jobs-kyiv-it/?advs=1",
                                  headers={"User-Agent": UserAgent().chrome},
                                  proxies=w)
        except:
            print("Ooops")
        else:
            print(req)
            soup = BeautifulSoup(req.content, "html.parser")
            positions = soup.find_all("h2")
            for one in positions:
                position = one.find("a").get("title")
                print(position)
            xxx = False

        # continue

# a = Proxy()
# result = a.pars_proxy()
xxx = pars_main()
# next(next_ip)
pars_shop(xxx)



