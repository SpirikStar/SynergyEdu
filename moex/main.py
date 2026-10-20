import requests
import json


class Moex:
    def __init__(self, url: str):
        self.url = url
        self.get_market()

    def connect(self) -> (bool, bytes):
        response = requests.get(url=self.url)
        if response.status_code != 200:
            return False, bytes
        return True, response

    def get_market(self):
        is_code, response = self.connect()
        if not is_code:
            return
        market = json.loads(response.content)
        if 'marketdata' not in market:
            return
        info_market = market['marketdata']['data']
        # TODO: Создать программу, которая анализирует все ценные бумаги и сохраняет в JSON файл.
        # TODO: ВИД: {'название': [{'price', 'date+time'}, {}, .., {}]}
        # TODO: Все записи должны быть уникальные внутри JSON. 
        # TODO: ? 


moex = Moex(
    url="https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json"
)
