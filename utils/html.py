from bs4 import BeautifulSoup


def parse_http_request_data(data: str) -> BeautifulSoup:
    return BeautifulSoup(data, "html.parser")
