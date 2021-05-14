from typing import Final

import requests
from bs4 import BeautifulSoup


class Parser:
    # noinspection SpellCheckingInspection
    URL: Final[str] = 'https://rusind.ru/' \
                      'raspredelenie-naseleniya-rossii-po-vozrastnym-gruppam.html'

    @property
    def data(self) -> list[tuple[int, int]]:
        html = requests.get(self.URL).content
        bs = BeautifulSoup(html, features='html.parser')

        # noinspection SpellCheckingInspection
        rows = bs.find('table', id='tablepress-4').find_all('tr')[1:]

        men = [int(row.find_all('td')[2].text.replace(' ', '')) for row in rows]
        women = [int(row.find_all('td')[3].text.replace(' ', '')) for row in rows]

        return list(zip(men, women))
