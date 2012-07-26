from outagesrunner.gis import BaseGISProvider

from urllib import quote_plus as _q
import urllib2
import json

class GoogleGISProvider(BaseGISProvider):
    def get_latlong(raw):
        query_string = _q(raw)
        uri = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % query_string

        obj = urllib2.urlopen(uri)
        json_data = json.load(obj)
        try:
            lat_long = json_data['results'][0]['geometry']['location']
        except:
            return None, None

        return lat_long['lat'], lat_long['lng']
