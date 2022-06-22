from datetime import datetime

import requests
from bs4 import BeautifulSoup


def _get_course_html() -> str:
    url = _get_url()
    response = requests.get(url)
    if response.ok:
        return response.text


def _get_url() -> str:
    dateFormatter = "%d/%m/%Y"
    date_today = datetime.now().strftime(dateFormatter)
    return f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_today}'


def parse_course() -> float:
    raw_data = _get_course_html()
    soup = BeautifulSoup(raw_data, 'xml')
    return _parse_dollar(soup)


def _parse_dollar(soup: BeautifulSoup) -> float:
    return float(soup.find(ID="R01235").find('Value').text.replace(',', '.'))
