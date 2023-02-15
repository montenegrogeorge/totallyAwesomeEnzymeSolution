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
    json_url = "https://data.sfgov.org/resource/rqzj-sfat.json"
    unionsq_coor = (37.788037692341184, -122.4073609530195)
    fac_type = "Truck"
    japanese_food = ["japan", "poke"]
    filters = ['facilitytype', 'fooditems', 'latitude', 'longitude']

    # FN Get JSON from website
    def get_json(self):
        try:
            with urllib.request.urlopen(self.json_url) as url:
                json_data = json.load(url)

            return json_data
        except ValueError:
            print("Error Pulling JSON from URL")

    # Clean JSON of incomplete data
    def clean_json(self, json_data=None):
        if json_data is None:
            json_data = self.get_json()

        for j in self.filters:
            for i in json_data:
                if j not in i:
                    json_data.remove(i)

        return json_data

    # FN to Filter List of Objects
    def filter_json(self, json_data=None):
        if json_data is None:
            json_data = self.clean_json()

        data = []

        for entry in json_data:
            if entry['facilitytype'] == self.fac_type:
                for j in self.japanese_food:
                    if re.search(j, entry['fooditems'].lower()):
                        data.append(entry)

        return data

    # create tuples of coordinates
    def create_coor(self, json_data=None):
        if json_data is None:
            json_data = self.filter_json()

        coors = {}

        for i in json_data:
            coors[i['applicant'] + ' - ' + i['address']] = geopy.distance.geodesic((i['latitude'], i['longitude']),
                                                                                   self.unionsq_coor).miles

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
    print(enzyme.filter_json())
    print(enzyme.create_coor())
    # print(enzyme.closest_to_union())
