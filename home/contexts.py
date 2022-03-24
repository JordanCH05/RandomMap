import random
import webbrowser
from decimal import *


def init_parameters(request):
    """
    precision is 7 to allow 4 decimal places
    and up to 3 figures before the decimal
    as the max longitude is 180
    """
    getcontext().prec = 7

    # Initial coordinates
    # Home
    init_lat = 0
    init_lon = 0
    dests = 0
    directions = ("North", "South", "East", "West")

    # Change for number of destinations

    dests = 10

    distances = {
        "Near": 0.0001,
        "Medium": 0.001,
        "Far": 0.01,
        "Wherever you are": 0.1,
    }

    dist = distances["Wherever you are"]

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

    """
    Mode Options:
    driving,
    walking (which prefers pedestrian paths and sidewalks, where available),
    bicycling (which routes via bike paths and preferred streets where available),
    transit,
    or flying.
    """
    mode = 'walking'

    waypoints = ''

    for i in range(dests - 1):
        wlat = globals()['lat%s' % (i + 1)]
        wlon = globals()['lon%s' % (i + 1)]
        waypoints += f'{wlat}+{wlon}|'

    waypoints = waypoints[:-1]

    destination = f'{lat}+{lon}'


    # roadmap or satellite
    maptype = 'satellite'

    # Create src for iframe
    src = ( f'https://www.google.com/maps/embed/v1/directions?origin={origin}&mode={mode}'
            f'&waypoints={waypoints}&destination={destination}&maptype={maptype}'
            f'&key=AIzaSyDSS3HZZYNloBpAPxuocppckTe78oGiueI')

    # Create html script
    html = f'<html><iframe width="100%" height="100%" style="border:0" loading="lazy" allowfullscreen src="{src}"></iframe></html>'

    # Create html file
    ran_map = open('google_map_embed.html', 'w')
    ran_map.write(html)
    ran_map.close()

    # Open file in browser in new tab
    webbrowser.open_new_tab('google_map_embed.html')
