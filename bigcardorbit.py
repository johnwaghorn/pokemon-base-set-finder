from bs4 import BeautifulSoup
import time
from utils.http import get_url_data, is_page_available
from utils.html import parse_http_request_data

BIGCARDORBIT_URL: str = "https://www.bigorbitcards.co.uk/pokemon/base-set/"
RESULTS_PER_PAGE: int = 24
CARD_TITLE_CLASS_NAME: str = "h2 product-title"
META_OUT_OF_STOCK_MESSAGE: str = "Out of Stock"
ZERO_IN_STOCK_MESSAGE: str = "0 in Stock"
REQUEST_INTERVAL: int = 5


def get_card_titles(parsed_html: BeautifulSoup) -> list:
    card_titles = []
    for title in parsed_html.find_all("h2", attrs={"class": CARD_TITLE_CLASS_NAME}):
        if len(title.text) > 0:
            card_titles.append(title.text)
    return card_titles


def get_card_info(parsed_html: BeautifulSoup) -> list:
    cards_list = []
    for stock_info in parsed_html.find_all("div", attrs={"class": "wrapper-buy"}):
        card_info = []
        in_stock = True
        for product_row in stock_info.find_all("span", attrs={"class": "product-row"}):
            if META_OUT_OF_STOCK_MESSAGE in product_row.text:
                in_stock = False
                continue
            else:
                product_name = product_row.find("span", attrs={"class": "product-name"})
                if not product_name:
                    continue
                else:
                    product_name = product_name.text
                product_stock = product_row.find(
                    "span", attrs={"class": "product-stock"}
                ).text
                product_price = product_row.find(
                    "span", attrs={"class": "product-price"}
                ).text
                card_info.append(f"{product_name} ~ {product_stock} ~ {product_price}")
        if not in_stock:
            card_info = META_OUT_OF_STOCK_MESSAGE
        else:
            card_info = [
                product for product in card_info if ZERO_IN_STOCK_MESSAGE not in product
            ]
        cards_list.append(card_info)
    return cards_list


def print_data(card_titles: list, card_info: list, show_out_of_stock: bool) -> None:
    card_titles_length = len(card_titles)
    if card_titles_length == 0:
        raise Exception("No cards on page.")
    if len(card_titles) == len(card_info):
        stock = zip(card_titles, card_info)
        if not show_out_of_stock:
            stock = [
                (title, info)
                for title, info in stock
                if info != META_OUT_OF_STOCK_MESSAGE
            ]
        for title, info in stock:
            print(f"{title}: {info}")
    else:
        raise Exception(
            f"Cannot zip title and stock info due to mismatch in card_titles and card_info list sizes. Card Titles len: {len(card_titles)} vs Card Info len: {len(card_info)}"
            f"\n {card_titles} \n {card_info}"
        )


def check_page(page_url: str, show_out_of_stock: bool) -> None:
    print(f"\nChecking url {page_url}...\n")
    page_data: str = get_url_data(page_url)
    parsed_html: BeautifulSoup = parse_http_request_data(page_data)
    card_titles: list = get_card_titles(parsed_html)
    card_info: list = get_card_info(parsed_html)
    print_data(card_titles, card_info, show_out_of_stock)


def check_bigcardorbit(show_out_of_stock: bool) -> None:
    url_available = True
    page_number = 1
    while url_available:
        page_url = f"{BIGCARDORBIT_URL}page-{str(page_number)}/?resultsPerPage={RESULTS_PER_PAGE}/"
        url_available = is_page_available(page_url)
        check_page(page_url=page_url, show_out_of_stock=show_out_of_stock)
        page_number += 1
        time.sleep(REQUEST_INTERVAL)
