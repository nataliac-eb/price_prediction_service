import csv
import statistics
import sys

class price:

    CSV_FILE = '/Users/nataliac/eventbrite/price_prediction_service/eng_training/python/ebengtraining.csv'

    def __init__(self, country_code, event_category_id):
        self.prices = self.load_data()
        self.country = country_code
        self.category = event_category_id

    def __str__(self):
        return str(self.get_prediction(self.country, self.category))

    def get_prediction(self,country_code, event_category_id):
        """Returns the mean and standard deviation for purchases for the provided country and event category.

        :Parameters:
            - `country_code` (str)
            - `event_category` (str): Human-friendly alias for a Category ID.

        :Returns:
        Dictionary with 'mean' and 'standard_deviation' as keys and floats as values.
        """
        # using context manager: i don't need to close the file.
        values=[]
        i=0
        for i in range(0,len(self.prices)):
            if self.prices[i][2]==country_code and self.prices[i][3]==event_category_id:
                values.append(float(self.prices[i][4]))

        if values:
            mean = statistics.mean(values)
            standard_deviation = statistics.stdev(values)

            return {'mean':mean, 'standard_deviation':standard_deviation}

    def load_data(self):
        with open(self.CSV_FILE, 'rt') as csvprices:
            # as default takes the first row as the header.
            prices = list(csv.reader(csvprices, delimiter=","))

        return prices