import requests

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
    Gives more details about a lat_lon from the lat_lons function
    """
    return requests.post(DETAILS, data=lat_lon).json()



