import requests
import geocoder


def getReverseGeoCoding():
    geocodeobj = geocoder.ip('me')

    lat = geocodeobj.latlng[0]
    longg = geocodeobj.latlng[1]

    url = 'http://apis.mapmyindia.com/advancedmaps/v1/' + \
        'bdc_7a0c4dc8dcdc48e28dd49eb96ccd7e9f' + \
        '/rev_geocode?lat='+str(lat)+'&lng='+str(longg)
    r = requests.get(url=url)

    data = r.json()
    district = data['results'][0]['district'].split(' ')[0]
    state = data['results'][0]['state']

    return {"state": state, "district": district}