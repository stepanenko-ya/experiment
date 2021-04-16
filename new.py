import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

main_r = requests.get("http://www.freeproxylists.net/ru/",
                      headers={"user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'})
print(main_r.status_code)
soup = BeautifulSoup(main_r.content, "html.parser")
