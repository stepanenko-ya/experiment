import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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
        print(len(self.proxy_lst))
        header = {"User-Agent": UserAgent().chrome}
        for pr in self.proxy_lst:
            prox= {'http': "http://" + pr, 'https': "http://" + pr}
            print(prox)
            try:
                main_r = requests.get("https://www.myxa.com.ua/srs/get-ip/", headers=header, proxies=prox)
                print(main_r)
            except:
                continue

            # url_proxy =  + x
            # print(x)
            #
            # try:
            #     main_r = requests.get("https://whoer.net/ru", headers=header, proxies={'http': "http://" + pr, 'https': "http://" + pr})
            #     print(pr)
            #     print(main_r)
            #
            #     soup = BeautifulSoup(main_r.content, 'html.parser')
            #     your_pi = soup.find(class_="button_icon your-ip").get_text()
            #     print(f"YOUR proxy adress:   {your_pi.strip()}")
            #
            # except:
            #
            #     continue

a = Proxy()
result = a.pars_proxy()


