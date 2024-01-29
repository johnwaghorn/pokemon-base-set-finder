from bs4 import BeautifulSoup
import time
from utils.http import get_url_data, is_page_available
from utils.html import parse_http_request_data

BIGCARDORBIT_URL: str = "https://www.bigorbitcards.co.uk/pokemon/base-set/"
RESULTS_PER_PAGE: str = "24"
CARD_TITLE_CLASS_NAME: str = "h2 product-title"
META_OUT_OF_STOCK_STRING: str = "Out of Stock"
ZERO_IN_STOCK_STRING: str = "0 in Stock"
REQUEST_INTERVAL: int = 5


def parse_page_html(parsed_html: BeautifulSoup) -> None:
    card_titles: list = get_card_titles(parsed_html)
    card_info: list = get_card_condition_stock_and_price(parsed_html)
    print_data(card_titles, card_info)


def check_page(page_url: str) -> None:
    print(f"\nChecking url {page_url}...\n")
    page_data: str = get_url_data(page_url)
    page_html: BeautifulSoup = parse_http_request_data(page_data)
    parse_page_html(page_html)


def check_bigcardorbit() -> None:
    url_available = True
    page_number = 1
    while url_available:
        page_url = f"{BIGCARDORBIT_URL}page-{str(page_number)}/?resultsPerPage={RESULTS_PER_PAGE}/"
        url_available = is_page_available(page_url)
        check_page(page_url=page_url)
        page_number += 1
        time.sleep(REQUEST_INTERVAL)


def get_card_titles(parsed_html: BeautifulSoup) -> list:
    card_titles = []
    for title in parsed_html.find_all("h2", attrs={"class": CARD_TITLE_CLASS_NAME}):
        if len(title.text) > 0:
            card_titles.append(title.text)
    return card_titles


def get_card_condition_stock_and_price(parsed_html: BeautifulSoup) -> list:
    cards_list = []
    for stock_info in parsed_html.find_all("div", attrs={"class": "wrapper-buy"}):
        card_info = []
        in_stock = True
        for product_row in stock_info.find_all("span", attrs={"class": "product-row"}):
            if META_OUT_OF_STOCK_STRING in product_row.text:
                in_stock = False
                continue
            else:
                product_name = product_row.find("span", attrs={"class": "product-name"})
                if not product_name:
                    continue
                else:
                    product_name = product_name.text
                product_stock = product_row.find("span", attrs={"class": "product-stock"}).text
                product_price = product_row.find("span", attrs={"class": "product-price"}).text
                card_info.append(f'{product_name} ~ {product_stock} ~ {product_price}')
        if not in_stock:
            card_info = META_OUT_OF_STOCK_STRING
        else:
            card_info = [product for product in card_info if ZERO_IN_STOCK_STRING not in product]
        cards_list.append(card_info)
    return cards_list


def print_data(card_titles: list, card_info: list) -> None:
    card_titles_length = len(card_titles)
    if card_titles_length == 0:
        raise Exception("No cards on page.")
    if len(card_titles) == len(card_info):
        for title, info in zip(card_titles, card_info):
            print(f"{title}: {info}")
    else:
        raise Exception(
            f"Cannot zip title and stock info due to mismatch in card_titles and card_info list sizes. Card Titles len: {len(card_titles)} vs Card Info len: {len(card_info)}"
            f"\n {card_titles} \n {card_info}"
        )
