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
            prox = {'http': "http://" + pr, 'https': "http://" + pr}

            try:
                test = requests.get("https://www.myxa.com.ua/srs/get-ip/", proxies=prox, timeout=6)
                if test.status_code == 200:
                    print(type(prox))

                        # good_prox.append(prox)
            except:
                continue
        return "ok"


def ip_lst():
    res = [{'http': 'http://148.72.152.156:3128', 'https': 'http://148.72.152.156:3128'}, {'http': 'http://3.141.186.75:3128', 'https': 'http://3.141.186.75:3128'}, {'http': 'http://45.153.33.166:3128', 'https': 'http://45.153.33.166:3128'}, {'http': 'http://132.248.196.2:8080', 'https': 'http://132.248.196.2:8080'}, {'http': 'http://176.113.73.97:3128', 'https': 'http://176.113.73.97:3128'}]

    return res


def pars_shop(ipes, url_page):
    value = True
    while value:
        try:
            ip = random.choice(ipes)
            print(url_page)
            print(ip)
            req = requests.get(url_page,
                               headers={"User-Agent": UserAgent().chrome},
                               proxies=ip,
                               timeout=6)

            print(req.status_code)
            soup = BeautifulSoup(req.content, 'html.parser')
            quits = soup.find_all(class_="text")
            for quit in quits:
                pars_result = quit.get_text()
            value = False
        except:
            print("Ooops")


            # soup = BeautifulSoup(req.content, "html.parser")
            # positions = soup.find_all("h2")
            # for one in positions:
            #     position = one.find("a").get("title")
            #     print(position)


        # continue


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


def main():
    url_pages = pars_pages()
    ipes = ip_lst()
    for url_page in url_pages:
        pars_shop(ipes, url_page)


if __name__ == "__main__":
    a = Proxy()
    result = a.pars_proxy()
    # main()


