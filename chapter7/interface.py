import requests


class HTTPClient:

    def __init__(self):
        self._sync_session = requests.Session()

    def request(self, *args, **kwargs):
        with self._sync_session.request(*args, **kwargs) as rep:
            rep.encoding = 'utf-8'
        return rep


client = HTTPClient()
response = client.request('GET', r'http://localhost:8080/test')
print(response.status_code, response.text)
from json import load
with open(r'D:\Program Files\JetBrains\imooc\chapter7\demo.json', 'r', encoding='utf-8') as f:
    json_data = load(f)
response2 = client.request('POST', r'http://localhost:8080/api/db', json=json_data)
print(response2.status_code, response2.text)
