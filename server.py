import time

from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

LINK_PREFIX = 'api_v1/for-csgo-google-sheet'
NEEDED_ARGUMENT_IN_LINK = 'skin_link'


class Browser:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        if not self.driver:
            self.create_driver()
        return self.driver

    def close(self):
        self.driver.quit()


@app.route('/')
def index():
    if not request.args.get(NEEDED_ARGUMENT_IN_LINK):
        return jsonify(error=f"You must specify a '{NEEDED_ARGUMENT_IN_LINK}' parameter in the link")
    skin_link = request.args.get(NEEDED_ARGUMENT_IN_LINK)
    driver = Browser().get_driver()
    try:
        res = driver.get(skin_link)
        element_name = driver.find_element(By.ID, 'largeiteminfo_item_name')
        element_price = driver.find_element(By.CLASS_NAME, 'market_commodity_order_summary')

        print('Link: ', skin_link)
        print('Element name: ', element_name.text)

        driver.execute_script("arguments[0].scrollIntoView();", element_price)
        time.sleep(1)

        print('Element price: ', element_price.text)
        print('Element price: ', element_price.text.split('$'))
        print('Element price: ', element_price.text.split('$')[-1])


        print('At the end of the method')
        time.sleep(15)
        return res
    except Exception:
        pass
    finally:
        driver.close()



if __name__ == '__main__':
    print(
        f'http://192.168.0.105:5000?{NEEDED_ARGUMENT_IN_LINK}=https://steamcommunity.com/market/listings/730/Revolution%20Case')
    app.run(host='0.0.0.0', debug=True)
