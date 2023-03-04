import requests
from bs4 import BeautifulSoup
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
def price_search(cur):
    info = []
    info.append(cur)
    def get_info(url):
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.text, 'lxml')
        number = soup.find('span', attrs={'style':'display: none;'}).text
        adress = soup.find('h1', class_='header-h0').text
        info.append(adress)
        info.append(number)

    def get_best_price(currency):
        url = f'https://www.banki.ru/products/currency/cash/{currency}/sankt-peterburg/'
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.text, 'lxml')
        best_result = soup.find('div', class_="table-flex__cell trades-table__name")
        href = best_result.find('a').get('href')
        href = 'https://www.banki.ru' + href
        bprice = best_result.find_next_sibling()
        buy_price = bprice.get('data-currencies-rate-buy')
        time = bprice.find('div', class_="trades-table__refresh-time").text
        sprice = bprice.find_next_sibling()
        sell_price = sprice.get('data-currencies-rate-sell')
        get_info(href)
        info.append(buy_price)
        info.append(sell_price)
        info.append(time.replace("\n",""))
    get_best_price(cur)
    print(info)

price_search('usd')