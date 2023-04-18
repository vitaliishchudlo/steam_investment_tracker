from flask import Flask, request, jsonify

app = Flask(__name__)

LINK_PREFIX = 'api_v1/for-csgo-google-sheet'


@app.route(f'/{LINK_PREFIX}/get_social_data/')
def get_social_data():
    if not request.args.get('platform'):
        return jsonify(error="You must specify a 'platform' parameter in the link")
    if not str(request.args.get('platform')).lower() in AVAILABLE_PLATFORMS:
        return jsonify(error=f"Available platforms are: {', '.join(AVAILABLE_PLATFORMS)}")
    if not request.args.get('username'):
        return jsonify(error="You must specify a 'username' parameter in the link")
    if not len(request.args.get('username')) > 4:
        return jsonify(error='Your username is not true')

    platform = request.args.get('platform')
    username = request.args.get('username')

    if 'https://' in username:
        url = True
    else:
        url = False

    if platform == 'twitter':
        if url:
            if not 'https://twitter.com/' in username:
                return jsonify(error=f'Bad url for {platform}')
        response = browser.twitter(username, url=url)
        print(response)
        if not response:
            return jsonify(error='Not found')
        return jsonify(username=username, platform=platform, followers=response['followers'],
                       following=response['following'])

    elif platform == 'tiktok':
        if url:
            if not 'https://www.tiktok.com/' in username:
                return jsonify(error=f'Bad url for {platform}')
        response = browser.tiktok(username, url=url)
        if not response:
            return jsonify(error='Not found')
        return jsonify(username=username, platform=platform, followers=response['followers'],
                       following=response['following'])

    elif platform == 'youtube':
        if not url:
            return jsonify(error='Not found')
        response = browser.youtube(username)
        return jsonify(username=username, platform=platform, followers=response['followers'])
