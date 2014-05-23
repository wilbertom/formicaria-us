import requests
from toolz import keyfilter


WEBSITE = 'http://schoolofants.org/'
BASE = WEBSITE + 'gather_locations/%s'
ALL = BASE % 'all'
EVENTS = BASE % 'events'
DETAILS = BASE % 'details'

def lat_lons():
    """
    Returns a list of latitudes and longitudes
    from where people have send sample ants.

    """
    return requests.get(ALL).json()

def details(lat_lon):
    """
    Gives more details about a lat_lon from the lat_lons function.

    """
    return {'location': lat_lon,
            # we remove the events field because it contains some user's name
            'data': keyfilter(lambda k: k != 'events', requests.post(DETAILS, data=lat_lon).json())}

def get_all():
    """
    Returns a list filled with all the data.

    """
    return map(details, lat_lons())


