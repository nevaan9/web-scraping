from bs4 import BeautifulSoup
import requests
import random
from lxml.html import fromstring
from itertools import cycle

# Get proxies


def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                              i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


proxies = get_proxies()
proxy_pool = cycle(proxies)
user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

book_data = []

isbn = "1411404017"
amz_url = "https://www.amazon.com/s?k=" + isbn
# Pick a random user agent
user_agent = random.choice(user_agent_list)
# Set the headers
# headers = {'User-Agent': user_agent}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# We need to MASK a real request as much as we can
# So open a brwser in INCOGNITO WINDOW - Send a request to AMAZON - Go to this website: https://curl.trillworks.com/ - Copy paste the cURL (right click request in network tab) to the box
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': user_agent,
    'sec-fetch-mode': 'no-cors',
    'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'Sec-Fetch-Mode': 'no-cors',
    'Referer': 'https://www.amazon.com/s?k='+isbn,
    'User-Agent': user_agent,
    'Origin': 'https://www.amazon.com',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Upgrade-Insecure-Requests': '1',
    'cookie': 'session-id=130-8046335-3136147; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=134-3400041-2996463; x-wl-uid=11FdN2hgaJHmW5GWmoFny1r0JoP3M/I/nxBnQDbERAhlBvzQmx7GaSgEkkmTlAD8f66HARYNhHmo=; session-token=2TXhJo8siv+Y31QyRewbYdSJsGgHySHv5lHaPxgNpWd39dYuK7pclzzkk7Cc9Vh8994Dtv5teM/Vrmh42bbY3da/qYODnixH0Yjkmuf1yy8AAJ7C1bux+qDh/3gu+3S766mqYyOXTgcGTqH1HveJtd2Tkf4timMQt87h1zKmK/iHZ2eFoBBQGP7743ohODKiCs7EmxjGyS/z5W+956GaDmBrLrPZ8iPeLaicoVV+erew+cYDdFdiECbxT3La4aTq; csm-hit=tb:0V2EKV1RKW698T2616JK+s-0V2EKV1RKW698T2616JK|1587949571329&t:1587949571329&adb:adblk_no',
    'referer': 'https://www.amazon.com/s?k='+isbn,
}

# Proxy
proxy = next(proxy_pool)
http = "http://" + proxy
https = "https://" + proxy
print(amz_url)
print(headers)
print(proxy)
print(http)
print(https)
amz_s = requests.get(amz_url, headers=headers, proxies={"http": http, "https": https}, verify=False).text
amz_soup = BeautifulSoup(amz_s)
name = amz_soup.select("span.a-size-medium")
print(name)
