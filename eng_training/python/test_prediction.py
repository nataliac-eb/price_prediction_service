import statistics
import unittest

from prediction import price

class test_prediction():

    def set_up():
        self.country = "US"
        self.category = "101"

    def statistics_calc(self, data):
        # es una buena idea calcularlo a mano
        return {"mean":statistics.mean(data), 'standard_deviation':statistics.stdev(data)}

    def test_result_by_country(self):
        precios = price(self.country, self.category)
        data = price.load_data()
        calc = self.statistics_calc(data)
        self.assertEqual(precios, calc)

