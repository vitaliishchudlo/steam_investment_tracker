import threading

from django.shortcuts import render
from django.urls import reverse
from .models import Skin
import requests
import json
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from django.utils import timezone

REFRESHING_PROCESS = False

"""
IT IS TMP VARIANT. THE PRINTS WILL BE REMOVED IN THE FUTURE
"""

def index(request):
    button_url = reverse('admin:index')
    
    return render(request, 'index.html', {'button_url': button_url})


def statistics(request):
    skins = Skin.objects.all()
    context = {
        'skins': skins,
    }
    
    return render(request, 'statistics.html', context)


def refreshing_skins_price():
    # UnComment it in the future
    # five_minutes_ago = timezone.now() - timedelta(minutes=5)
    # skins = Skin.objects.filter(modified_date__lte=five_minutes_ago)
    # skin_names = [skin.name for skin in skins]

    skins = Skin.objects.all().order_by('-id')
    skin_names = [skin.name for skin in skins]

    base_link = f'http://18.193.224.198/?skin_name='

    for skin_name in skin_names:
        print('The link: ', base_link + skin_name)
        response = requests.get(base_link + skin_name)
        if response.status_code == 200:
            data = json.loads(response.text)
            skin_price = data.get('skin_price').replace('$', '')
            if not skin_price == 'not found':
                try:
                    skin = Skin.objects.get(name=skin_name)
                    skin.current_price = skin_price
                    skin.save()
                    print(f'Skin name: {skin_name} | Skin price: {skin_price}')
                except Skin.DoesNotExist:
                    pass
        else:
            print('Error:', response.status_code)


def start_refreshing_skins_price():
    global REFRESHING_PROCESS
    REFRESHING_PROCESS = True

    refreshing_skins_price()

    REFRESHING_PROCESS = False


def refresh(request):
    global REFRESHING_PROCESS
    if REFRESHING_PROCESS:
        return render(request, 'refresh.html', {'refreshing_started': False})
    else:
        thread = threading.Thread(target=start_refreshing_skins_price)
        thread.start()
        
        return render(request, 'refresh.html', {'refreshing_started': True})
