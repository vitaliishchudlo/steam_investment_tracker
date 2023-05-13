import time

from django.shortcuts import render
from django.urls import reverse
import requests
from .models import Skin
import requests
import json

def index(request):
    button_url = reverse('admin:index')
    return render(request, 'index.html', {'button_url': button_url})


def statistics(request):
    skins = Skin.objects.all()
    context = {
        'skins': skins,
    }
    return render(request, 'statistics.html', context)


def refresh(request):
    skins = Skin.objects.all()
    skin_names = [skin.name for skin in skins]

    skin_prices = {}
    base_link = f'http://18.193.224.198/?skin_name='

    for skin_name in skin_names:
        response = requests.get(base_link + skin_name)
        if response.status_code == 200:
            data = json.loads(response.text)
            skin_price = data.get('skin_price').replace('$','')
            skin_prices[skin_name] = skin_price
            print(skin_name)
            print(skin_price)
        else:
            print('Error:', response.status_code)

    print('Skins prices DICT: ', skin_prices)

    for name, price in skin_prices.items():
        try:
            skin = Skin.objects.get(name=name)
            skin.current_price = price
            skin.save()
        except Skin.DoesNotExist:
            pass

    import ipdb; ipdb.set_trace(context=5)
    return render(request, 'refresh.html', {'refreshing_started': True})
    # return render(request, 'refresh.html', {'refreshing_started': True})
