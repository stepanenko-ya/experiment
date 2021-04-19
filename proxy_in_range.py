import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
from random import uniform

def check_ip(proxs):
    print("check_ip".upper())
    good_proxy = []
    for prox in proxs:
        proxi = {'http': f'http://{prox}', 'https': f'http://{prox}'}
        print(proxi)
        try:
            req = requests.get("https://quotes.toscrape.com/",
                               headers={"User-Agent": UserAgent().chrome},
                               proxies=proxi,
                               timeout=10)

            if req.status_code == 200:
                print(req.status_code)
                good_proxy.append(proxi)
        except:
            continue
    print(good_proxy)
    return good_proxy


def main(check_proxy):
    print("MAIN")
    proxy_url = "https://proxy6.net/en/privacy"
    count = 0
    value = True
    while value:
        for i in range(10):
            ip = random.choice(check_proxy)
            count += 1
            try:
                r = requests.get(proxy_url,
                                 headers={"User-Agent": UserAgent().chrome},
                                 proxies=ip,
                                 timeout=10)
                value = False
            except:
                print(count, ip)
                print('Oops!')

            else:
                soup = BeautifulSoup(r.text, "html.parser")
                f = soup.find(class_="dotd clickselect").get_text()
                print(count, ip)
                print(f)


with open("proxy_list", "r") as proxy_f:
    proxs = proxy_f.readline().split(",")
    proxs.pop()
checker = check_ip(proxs)
main(checker)
