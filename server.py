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


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.headless = False
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


@app.route('/')
def index():
    if not request.args.get(NEEDED_ARGUMENT_IN_LINK):
        return jsonify(error=f"You must specify a '{NEEDED_ARGUMENT_IN_LINK}' parameter in the link")

    skin_link = request.args.get(NEEDED_ARGUMENT_IN_LINK)
    skin_link = skin_link.replace(' ', '%20')

    driver = create_driver()
    try:
        driver.get(skin_link)
        element_name = driver.find_element(By.ID, 'largeiteminfo_item_name')
        name_of_skin_text = element_name.text

        element_of_sales = driver.find_element(By.CLASS_NAME, 'market_commodity_order_summary')
        driver.execute_script("arguments[0].scrollIntoView();", element_of_sales)
        time.sleep(1)

        try:
            lowest_price_text = element_of_sales.text.split('$')[-1]
            count_of_sales_text = element_of_sales.text.split(' ')[0]
        except Exception:
            print('refreshing')
            driver.refresh()
            time.sleep(3)
            driver.execute_script("arguments[0].scrollIntoView();", element_of_sales)
            time.sleep(1)
            lowest_price_text = element_of_sales.text.split('$')[-1]
            count_of_sales_text = element_of_sales.text.split(' ')[0]

        return jsonify(title_of_skin=name_of_skin_text, lowest_price=lowest_price_text,
                       count_of_sales=count_of_sales_text)
    except Exception as err:
        print('\n\n ERROR: ', err)
    finally:
        driver.quit()


if __name__ == '__main__':
    app.run()
