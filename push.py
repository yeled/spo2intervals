#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import requests
import statistics
import datetime 

from intervalsicu import Intervals


# Fetch SpO2 data and calculate median
def get_median_spo2():
    url = "https://mb.spodder.com/"
    response = requests.get(url)
    data = response.json()

    # Extract spo2_value from each measurement
    spo2_values = [measurement['spo2_value'] for measurement in data]

    # Calculate and return median
    return statistics.median(spo2_values)


# Create spo2 variable with median value
spo2 = get_median_spo2()


def wellness():
    svc = Intervals("", "", strict=False)

    start = datetime.date.today()
    wellness = svc.wellness(start)
    wellness['spO2'] = spo2
    wellness = svc.wellness_put(wellness)
    pprint.pprint(wellness)


if __name__ == "__main__":
    wellness()
    print(spo2)

