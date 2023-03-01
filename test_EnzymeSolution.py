from unittest import TestCase

from EnzymeSolution import EnzymeSolution


class TestEnzymeSolution(TestCase):

    json_no_foodTruck = []
    json_one_solution = [{"applicant": "Ziaurehman Amini", "address": "123 Somewhere",
                          "facilitytype": "Truck", "fooditems": "Japanese Food",
                          "latitude": "37.794331003246846", "longitude": "-122.39581105302317"}]
    json_clean_solution = [{"applicant": "Ziaurehman Amini", "address": "123 Somewhere",
                            "facilitytype": "Truck", "fooditems": "Japanese Food",
                            "latitude": "37.794331003246846", "longitude": "-122.39581105302317"},
                           {"applicant": "George", "facilitytype": "Truck",
                            "latitude": "50.794331003246846", "longitude": "-200.39581105302317"}]
    json_filters_solution = [{"applicant": "Ziaurehman Amini", "address": "123 Somewhere", "facilitytype": "Truck",
                              "fooditems": "Japanese Food",
                              "latitude": "37.794331003246846", "longitude": "-122.39581105302317"},
                             {"applicant": "George", "facilitytype": "Cart", "fooditems": "Japanese Food",
                              "latitude": "50.794331003246846", "longitude": "-200.39581105302317"}]
    json_create_coors = {'Ziaurehman Amini - 123 Somewhere': 0.7668004789003019}
    json_closest = {'Ziaurehman Amini - 123 Somewhere': 0.7668004789003019,
                    'George Poke - 124 Somewhere': 1.7668004789003019,
                    'Sushi and More - 543 Somewhere': 2.7668004789003019}
    closest = 'Ziaurehman Amini - 123 Somewhere'
    enzyme = EnzymeSolution()

    def test_clean_json(self):
        self.assertEqual(self.json_one_solution, self.enzyme.clean_json(self.json_one_solution))

        self.assertEqual(self.json_one_solution, self.enzyme.clean_json(self.json_clean_solution))

    def test_filter_json(self):
        self.assertEqual(self.json_one_solution, self.enzyme.filter_json(self.json_filters_solution))

    def test_create_coor(self):
        self.assertEqual(self.json_create_coors, self.enzyme.create_coor(self.json_one_solution))

    def test_closest_to_union(self):
        self.assertEqual(self.closest, self.enzyme.closest_to_union(self.json_closest))
