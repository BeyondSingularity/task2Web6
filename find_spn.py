import sys
import requests


def find_spn(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"
    }
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return 0.002, 0.002
        pass
    # Преобразуем ответ в json-объект
    json_response = response.json()
    bound = json_response["response"]["GeoObjectCollection"]['featureMember'][0]['GeoObject']['boundedBy']['Envelope']
    x1, y1 = map(float, bound['lowerCorner'].split())
    x2, y2 = map(float, bound['upperCorner'].split())
    return x2 - x1, y2 - y1