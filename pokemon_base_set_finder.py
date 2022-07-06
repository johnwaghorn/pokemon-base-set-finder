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
    base_url = "https://www.bigorbitcards.co.uk/pokemon/base-set/"
    parsed_html = get_and_parse_page_data(base_url)
    process_data(parsed_html)
    print(f"\nBuy from here:{base_url}\n")

    url_available = True
    page_number = 2
    i = 0
    while url_available:
        page_url = f"{base_url}page-{str(page_number)}/"
        try:
            urllib.request.urlopen(page_url)
        except urllib.error.HTTPError as e:
            if e.getcode() == 404:
                url_available = False
                sys.exit("404 error or FINISHED")
        page_soup = get_and_parse_page_data(page_url)
        page_number += 1
        process_data(page_soup)
        print(f"\nBuy from here: {page_url}\n")
        i += 1


def get_and_parse_page_data(url) -> BeautifulSoup:
    request = requests.get(url, headers=HEADERS)
    data = request.text
    return BeautifulSoup(data, "html.parser")


def process_data(parsed_html):
    card_titles: list = get_card_titles(parsed_html)
    card_info: list = get_card_price_and_stock(parsed_html)
    output_data(card_titles, card_info)


def get_card_titles(parsed_html) -> list:
    card_titles = []
    for title in parsed_html.find_all("a", attrs={"class": "product-title"}):
        if len(title.text) > 0:
            card_titles.append(title.text)
    card_titles = sorted(set(card_titles))
    return card_titles


def get_card_price_and_stock(parsed_html) -> list:
    card_info = []
    for info in parsed_html.find_all(
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
        raise Exception("Mismatch in card_titles and card_info list sizes")


if __name__ == "__main__":
    get_data()
