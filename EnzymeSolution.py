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
    filters = ['facilitytype', 'fooditems', 'latitude', 'longitude', 'applicant', 'address']

    japanese_trucks = []

    # FN Get JSON from website
    def get_json(self, json_url=None):
        if json_url is None:
            json_url = self.json_url

        try:
            with urllib.request.urlopen(json_url) as url:
                json_data = json.load(url)
                self.japanese_trucks = json_data
        except ValueError:
            print("Error Pulling JSON from URL")

    # Clean JSON of incomplete data
    def clean_json(self, json_data=None):
        if json_data is None:
            json_data = self.japanese_trucks

        for j in self.filters:
            for i in json_data:
                if j not in i:
                    json_data.remove(i)

        self.japanese_trucks = json_data

    # FN to Filter List of Objects
    def filter_json(self, json_data=None):
        if json_data is None:
            json_data = self.japanese_trucks

        data = []

        for entry in json_data:
            if entry['facilitytype'] == self.fac_type:
                for j in self.japanese_food:
                    if re.search(j, entry['fooditems'].lower()):
                        data.append(entry)

        self.japanese_trucks = data

    # create tuples of coordinates
    def create_coor(self, json_data=None):
        if json_data is None:
            json_data = self.japanese_trucks

        for i in json_data:
            i['distance'] = geopy.distance.geodesic((i['latitude'], i['longitude']), self.unionsq_coor).miles

        self.japanese_trucks = json_data

    def sort_list(self, json_data=None):
        if json_data is None:
            json_data = self.japanese_trucks

        self.japanese_trucks = sorted(json_data, key=lambda d: d['distance'])

    # # FN Calculate distance to Union Square
    def closest_to_union(self, url=None, distances=None):
        self.get_json(url)
        self.clean_json(distances)
        self.filter_json(self.clean_json(distances))
        self.create_coor(self.filter_json(self.clean_json(distances)))
        self.sort_list(self.create_coor(self.filter_json(self.clean_json(distances))))

        if distances is None:
            distances = self.japanese_trucks

        return distances[0]['applicant'] + ' at ' + distances[0]['address'] + ' with a distance of ' + str(distances[0]['distance']) + ' miles'

    def __init__(self):
        pass


if __name__ == '__main__':
    enzyme = EnzymeSolution()

    print(enzyme.closest_to_union())
