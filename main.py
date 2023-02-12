import json
import urllib.request
import geopy.distance
import re

'''
Using the data available at https://data.sfgov.org/resource/rqzj-sfat.json 
find out which opened japanese food truck is the closest to union square.

We are looking for:
-completeness
-style
-and testing.
'''


class EnzymeSolution:
    # CONST Class Variables
    JSON_URL = "https://data.sfgov.org/resource/rqzj-sfat.json"
    UNIONSQ_COOR = (37.788037692341184, -122.4073609530195)
    FAC_TYPE = "Truck"
    JAPANESE_FOOD = ["japan", "poke", "japanese"]
    FILTERS = ['facilitytype', 'fooditems']

    # FN Get JSON from website
    def get_json(self):
        with urllib.request.urlopen(self.JSON_URL) as url:
            json_data = json.load(url)

            return json_data

    # Parse JSON into objects
    def clean_json(self):
        json_data = self.get_json()

        for j in self.FILTERS:
            for i in json_data:
                if j not in i:
                    json_data.remove(i)

        return json_data

    # FN to Filter List of Objects
    def filter_json(self, food_list=None):
        if food_list is None:
            food_list = self.JAPANESE_FOOD

        data = []

        for i in self.clean_json():
            if i['facilitytype'] == self.FAC_TYPE:
                for j in self.JAPANESE_FOOD:
                    if re.search(j, i['fooditems'].lower()):
                        data.append(i)

        return data

    # create tuples of coordinates
    def create_coor(self, json_data=None):
        if json_data is None:
            json_data = self.filter_json()

        coors = {}

        for i in json_data:
            coors[i['applicant'] + ' - ' + i['address']] = geopy.distance.geodesic((i['latitude'], i['longitude']),
                                                                                   self.UNIONSQ_COOR).miles

        return coors

    # FN Calculate distance to Union Square
    def closest_to_union(self, distances=None):
        if distances is None:
            distances = self.create_coor()

        return min(distances, key=distances.get)

    def __init__(self):
        pass


if __name__ == '__main__':
    enzyme = EnzymeSolution()

    print(enzyme.closest_to_union())
