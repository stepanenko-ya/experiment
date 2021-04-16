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
        with open("proxy_list", "w") as f:
            for proxy in self.proxy_lst:
                prox = str(proxy.strip()) + ", "
                f.write(prox[:-1])


        # good_prox = []
        # for pr in self.proxy_lst:
        #     prox = {'http': "http://" + pr, 'https': "http://" + pr}
        #     with open("proxy_list", "w") as f:
        #         f.write("__________________")
        #         try:
        #             # test = requests.get("https://www.myxa.com.ua/srs/get-ip/", proxies=prox, timeout=6)
        #             # if test.status_code == 200:
        #             # f.write(str(prox))
        #             good_prox.append(prox)
        #         except:
        #             continue
        # return good_prox


def ip_lst():
    res = [{'http': 'http://148.72.152.156:3128', 'https': 'http://148.72.152.156:3128'}, {'http': 'http://3.141.186.75:3128', 'https': 'http://3.141.186.75:3128'}, {'http': 'http://45.153.33.166:3128', 'https': 'http://45.153.33.166:3128'}, {'http': 'http://132.248.196.2:8080', 'https': 'http://132.248.196.2:8080'}, {'http': 'http://176.113.73.97:3128', 'https': 'http://176.113.73.97:3128'}]

    return res


def pars_shop(proxi, url_pages):
    pass
    # value = True
    # while value:
    #     try:
    #         ip = random.choice(ipes)
    #         print(url_page)
    #         print(ip)
    #         req = requests.get(url_page,
    #                            headers={"User-Agent": UserAgent().chrome},
    #                            proxies=ip,
    #                            timeout=6)
    #
    #         print(req.status_code)
    #         soup = BeautifulSoup(req.content, 'html.parser')
    #         quits = soup.find_all(class_="text")
    #         for quit in quits:
    #             pars_result = quit.get_text()
    #         value = False
    #     except:
    #         print("Ooops")
    #

            # soup = BeautifulSoup(req.content, "html.parser")
            # positions = soup.find_all("h2")
            # for one in positions:
            #     position = one.find("a").get("title")
            #     print(position)

        # continue


def pars_shop2(url_page, check_proxy):
    value = True
    print(url_page)
    while value:
        try:
            ip = random.choice(check_proxy)
            req = requests.get(url_page,
                               headers={"User-Agent": UserAgent().chrome},
                               proxies=ip,
                               timeout=6)
            value = False
        except:
            print("Ooops!")
        else:
            print(req.status_code)
            soup = BeautifulSoup(req.content, 'html.parser')
            quits = soup.find_all(class_="text")
            for quit in quits:
                pars_result = quit.get_text()
                print(pars_result)


def pars_pages():
    lst_url = ["https://quotes.toscrape.com/page/1/"]
    url = "https://quotes.toscrape.com"
    while int(lst_url[-1][-2]) < 10:
        try:
            r = requests.get(lst_url[-1], headers={"User-Agent": UserAgent().chrome})
            soup = BeautifulSoup(r.content, "html.parser")
            finder = soup.find(class_="pager").find(class_="next").find("a").get("href")
            lst_url.append(url + finder)

        except:
          break

    return lst_url


def check_ip(proxs):
    good_proxy = []
    for prox in proxs:
        proxi = {'http': f'http://{prox}', 'https': f'http://{prox}'}
        print(proxi)
        try:
            req = requests.get("https://www.myxa.com.ua/srs/get-ip/",
                               headers={"User-Agent": UserAgent().chrome},
                               proxies=proxi,
                               timeout=6)
            if req.status_code == 200:
                good_proxy.append(proxi)
        except:
            continue
    print(good_proxy)
    return good_proxy




def main(proxs):
    url_pages = pars_pages()
    print(url_pages)
    # ipes = ip_lst()
    for url_page in url_pages:
        pars_shop(proxs, url_page)


if __name__ == "__main__":
    # a = Proxy()
    # result = a.pars_proxy()

    with open("proxy_list", "r") as proxy_f:
        proxs = proxy_f.readline().split(",")
        proxs.pop()

    # checker = check_ip(proxs)
    checker = [{'http': 'http://139.228.32.187:8080', 'https': 'http://139.228.32.187:8080'}, {'http': 'http://198.50.163.192:3129', 'https': 'http://198.50.163.192:3129'}]
    url_pages = pars_pages()

    # main(proxs)
    for url_p in url_pages:

        pars_shop2(url_p, checker)


