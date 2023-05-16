import requests
import re
import requests
import json


# url = "https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20AWP%20%7C%20Hyper%20Beast%20%28Minimal%20Wear%29"
# name = 'm4a1-s printstream field-tested'
# name = 'USP-S | Printstream Field-Tested'
name = 'Revolution Case'
url = f"https://steamcommunity.com/market/search?appid=730&q={name}"

url = url.replace(' ', '+')
print(url, '||||')
response = requests.get(url)
html = response.text


match = re.search(r'data-currency="1">(\$?\d+\.\d{2})', html)
if match:
    value = match.group(1)
    print(value)


# search_word = 'Market_LoadOrderSpread('
#
# skin_nameid = html[html.index(search_word) + 1]
#
# print('Skin ID: ', skin_nameid)
#
# target_url = f'https://steamcommunity.com/market/itemordershistogram?country=US&language=english&currency=1&item_nameid={skin_nameid}&two_factor=0'
#
#
#
# url = "https://steamcommunity.com/market/itemordershistogram"
# params = {
#     "country": "US",
#     "language": "english",
#     "currency": "1",
#     "item_nameid": skin_nameid,
#     "two_factor": "0"
# }
#
# response = requests.get(url, params=params)
#
# if response.status_code == 200:
#     data = json.loads(response.text)
#     print(data)
#     print('\n\n')
#
#     print(data['sell_order_graph'][0][0])
# else:
#     print("Failed to retrieve data. Status code:", response.status_code)






import ipdb; ipdb.set_trace(context=5)






# import requests
# import re
# import requests
# import json
#
#
# url = "https://steamcommunity.com/market/search?appid=730&q=StatTrak%E2%84%A2+AWP+%7C+Hyper+Beast+Minimal+Wear"
#
# response = requests.get(url)
# html = response.text
#
# print(html)
#
# match = re.search(r'data-currency="1">(\$?\d+\.\d{2})', html)
# if match:
#     value = match.group(1)
#     print(value)
