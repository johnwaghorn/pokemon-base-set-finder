import sys
import re
import urllib
from bs4 import BeautifulSoup
import requests

RED = "\033[1;31m"
BLUE = "\033[1;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

sys.stdout.write(RED)


def get_data():
    print("\nStarting... \n")
    url = "https://www.bigorbitcards.co.uk/pokemon/base-set/"
    req = requests.get(url, headers=HEADERS)
    data = req.text
    soup = BeautifulSoup(data, "html.parser")
    process_data(soup)
    print(f"\nBuy from here:{url}\n")

    notUrlEnumMax = True
    urlEnum = 2
    i = 0
    while notUrlEnumMax:
        url2 = (
            "https://www.bigorbitcards.co.uk/pokemon/base-set/page-"
            + str(urlEnum)
            + "/"
        )
        try:
            urllib.request.urlopen(url2)
        except urllib.error.HTTPError as e:
            if e.getcode() == 404:
                notUrlEnumMax = False
                sys.exit("404 error or FINISHED")

        req2 = requests.get(url2, headers=HEADERS)
        data2 = req2.text
        soup2 = BeautifulSoup(data2, "html.parser")
        urlEnum += 1
        process_data(soup2)
        print(f"\nBuy from here: {url2}\n")
        i += 1


def process_data(soup):
    card_titles: list = get_card_titles(soup)
    card_info: list = get_card_price_and_stock(soup)
    output_data(card_titles, card_info)


def get_card_titles(soup) -> list:
    card_titles = []
    for title in soup.find_all("a", attrs={"class": "product-title"}):
        if len(title.text) > 0:
            card_titles.append(title.text)
    card_titles = sorted(set(card_titles))
    return card_titles


def get_card_price_and_stock(soup) -> list:
    card_info = []
    for info in soup.find_all(
        "div", attrs={"class": "ty-control-group product-list-field"}
    ):
        if len(info.text) > 0:
            info = re.sub(r"\n", "", info.text)
            info = re.sub(r"\t", "", info)
            info = re.sub(r"\xa0", " - ", info)
            card_info.append(info)
    return card_info


def output_data(card_titles: list, card_info: list) -> None:
    if len(card_titles) == len(card_info):
        for title, info in zip(card_titles, card_info):
            print(f"{title} -- {info}")
    else:
        raise (Exception)


if __name__ == "__main__":
    get_data()
