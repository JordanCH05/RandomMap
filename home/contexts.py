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
