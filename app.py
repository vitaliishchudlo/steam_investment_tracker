import re
from logging import getLogger

import requests
from flask import Flask, request, jsonify

from app_loger import AppLogger

app = Flask(__name__)
logger = getLogger('AppLogger')

# LINK_PREFIX = 'api_v1/for-csgo-google-sheet'
NEEDED_ARGUMENT_IN_LINK = 'skin_name'


@app.route('/')
def index():
    logger.info('New request. Start checking the request...')
    if not request.args.get(NEEDED_ARGUMENT_IN_LINK):
        logger.warning(f'Request failed, because bad {NEEDED_ARGUMENT_IN_LINK}')
        return jsonify(error=f"You must specify a '{NEEDED_ARGUMENT_IN_LINK}' parameter in the link")

    logger.info('Request is good. Start the execution of the request...')

    skin_name = request.args.get(NEEDED_ARGUMENT_IN_LINK).replace(' ', '+')
    skin_search_link = f"https://steamcommunity.com/market/search?appid=730&q={skin_name}"
    logger.info(f'Skin search link created -> {skin_search_link}')

    try:
        logger.info('Starting to opening the link...')
        response = requests.get(skin_search_link)
        html = response.text
        logger.info('Got the response from server. Starting to process the response...')
        match = re.search(r'data-currency="1">(\$?\d+\.\d{2})', html)
        if match:
            skin_price = match.group(1)
            logger.info(f'Price of skin found -> ${skin_price}. Returning response...')
            return jsonify(skin_price=skin_price)
        else:
            return jsonify(skin_price='not found', skin_link=skin_search_link)
    except Exception as err:
        print('1')
        logger.info(f'"Try block" is broken. Link: {skin_search_link} ||| TraceBack: {err}')
        return jsonify(skin_price='error', skin_link=skin_search_link, traceback=err)


if __name__ == '__main__':
    AppLogger()
    app.run()
