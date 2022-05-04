import random
from decimal import *

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

from .forms import MapForm
from .models import Map


def index(request):
    """ A view to return the index page """
    form = MapForm()

    if request.method == 'POST':
        form = MapForm(request.POST)

        if form.is_valid():
            map = form.save()
            return redirect(reverse('map', args=[map.id]))

    context = {
        'form': form
    }

    return render(request, 'home/index.html', context)


def map(request, map_id):
    """ View Map """
    map = get_object_or_404(Map, pk=map_id)

    directions = ("North", "South", "East", "West")

    dests = map.no_of_dests
    dist = map.distance

    init_lat = map.latitude
    init_lon = map.longitude

    lat = init_lat + Decimal(0)
    lon = init_lon + Decimal(0)

    for x in range(dests):
        # A higher range for y adds more chance of a distant destination
        for y in range(10000):
            ran = random.randint(0, 3)

            if directions[ran] == "North":
                lat += Decimal(dist)
                lon += Decimal(0)
            elif directions[ran] == "South":
                lat -= Decimal(dist)
                lon += Decimal(0)
            elif directions[ran] == "East":
                lon += Decimal(dist)
                lat += Decimal(0)
            elif directions[ran] == "West":
                lon -= Decimal(dist)
                lat += Decimal(0)
        
        print("-------------------------------")
        print(f'Waypoint {x + 1}')
        globals()['lat%s' % (x + 1)] = lat
        globals()['lon%s' % (x + 1)] = lon
        print(lat, lon)

    print("-------------------------------")
    
    # Parameters for embeded Google map

    origin = f'{float(init_lat)}+{float(init_lon)}'

    mode = 'walking'

    waypoints = ''

    for i in range(dests - 1):
        wlat = globals()['lat%s' % (i + 1)]
        wlon = globals()['lon%s' % (i + 1)]
        waypoints += f'{wlat}+{wlon}|'

    waypoints = waypoints[:-1]

    print('waypoints' + waypoints)

    destination = f'{lat}+{lon}'

    maptype = 'satellite'

    api_key = settings.GOOGLE_API_KEY

    if waypoints:

        src = ( f'https://www.google.com/maps/embed/v1/directions?origin={origin}&mode={mode}'
            f'&waypoints={waypoints}&destination={destination}&maptype={maptype}'
            f'&key={api_key}')

    else: 
        src = ( f'https://www.google.com/maps/embed/v1/directions?origin={origin}&mode={mode}'
            f'&destination={destination}&maptype={maptype}'
            f'&key={api_key}')

    context = {
        'map': map,
        'src': src,
    }

    return render(request, 'home/map.html', context)
