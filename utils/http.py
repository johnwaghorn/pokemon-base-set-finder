import requests
import urllib

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def get_url_data(url: str) -> str:
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Bad response from url: {response.status_code}")
    return response.text


def is_page_available(page_url) -> bool:
    try:
        urllib.request.urlopen(page_url)
        return True
    except urllib.error.HTTPError as error:
        if error.getcode() == 404:
            print("404/FINISHED")
            return False
