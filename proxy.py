import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
from time import sleep


class Proxy:
    ''' Parsing proxies-numbers from website '''
    proxy_url = "https://www.ip-adress.com/proxy-list"
    proxy_lst = []

    def __init__(self):
        r = requests.get(self.proxy_url, headers={"User-Agent": UserAgent().chrome}, timeout=6)
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


def pars_pagination():
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
            req = requests.get("https://proxy6.net/en/privacy",
                               headers={"User-Agent": UserAgent().chrome},
                               proxies=proxi,
                               timeout=10)
            if req.status_code == 200:
                good_proxy.append(proxi)
        except:
            continue
    print(good_proxy)
    return good_proxy


def pars_shop(url_page, check_proxy):
    sleep(random.uniform(2, 6))
    value = True
    print(url_page)
    while value:
        try:
            ip = random.choice(check_proxy)
            req = requests.get(url_page,
                               headers={"User-Agent": UserAgent().chrome},
                               proxies=ip,
                               timeout=10)
            value = False
        except :
            print("Oops!")
        else:
            print(req.status_code)
            soup = BeautifulSoup(req.content, 'html.parser')
            quits = soup.find_all(class_="text")
            for quit in quits:
                pars_result = quit.get_text()
                print(pars_result)


def main(proxs):
    checker = check_ip(proxs)
    url_pages = pars_pagination()
    for url_p in url_pages:
        pars_shop(url_p, checker)


if __name__ == "__main__":

    a = Proxy()
    a.pars_proxy()
    proxs = open("proxy_list").readline().split(",")
    proxs.pop()
    main(proxs)

