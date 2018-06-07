import csv
import statistics
import sys

CSV_FILE = '/Users/nataliac/eventbrite/price_prediction_service/eng_training/python/ebengtraining.csv'

def get_prediction(country_code, event_category_id):
    """Returns the mean and standard deviation for purchases for the provided country and event category.

    :Parameters:
        - `country_code` (str)
        - `event_category` (str): Human-friendly alias for a Category ID.

    :Returns:
    Dictionary with 'mean' and 'standard_deviation' as keys and floats as values.
    """
    with open(CSV_FILE, 'rt') as csvprices:
        prices = list(csv.reader(csvprices, delimiter=","))

        values=[]
        i=0
        for i in range(0,len(prices)):
            if prices[i][2]==country_code and prices[i][3]==event_category_id:
                values.append(float(prices[i][4]))

        if values:
            mean = statistics.mean(values)
            standard_deviation = statistics.stdev(values)

            return {'mean':mean, 'standard_deviation':standard_deviation}


if __name__ == '__main__':
    country = str(sys.argv[1])
    category_id = str(sys.argv[2])
    print("for", country, category_id)
    res = get_prediction(country, category_id)
    print(res)
