from datetime import datetime

import requests
from bs4 import BeautifulSoup

from exceptions import CantParseCourse


def _parse_course() -> float:
    """Service receiving data on the exchange rate"""
    raw_data = _get_course_html()
    soup = BeautifulSoup(raw_data, 'xml')
    return _parse_dollar(soup)


def _get_course_html() -> str:
    url = _get_url()
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        raise CantParseCourse


def _get_url() -> str:
    dateFormatter = "%d/%m/%Y"
    date_today = datetime.now().strftime(dateFormatter)
    return f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_today}'


def _parse_dollar(soup: BeautifulSoup) -> float:
    try:
        return float(soup.find(ID="R01235").find('Value').text.replace(',', '.'))
    except AttributeError:
        raise CantParseCourse
