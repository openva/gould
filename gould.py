#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Determines the rate structure for tomorrow that's advertised by Dominion (the
Virginia electricial utility) and creates a JSON file containing that data.
"""

import os
import sys
import urllib, json
import time
import datetime as dt
import yaml

# Load the rates file.
RATES = yaml.safe_load(open('rates.yml'))

def main():
    """The main program function."""

    # Get tomorrow's year, month (spelled out), and date (not left-padded).
    tomorrow = dt.date.today() + dt.timedelta(days=1)

    # Retrieve the JSON for this month
    url = 'https://www.dom.com/api/smart-pricing/years/' \
        + str(tomorrow.strftime('%Y')) + '/months/' \
        + str(tomorrow.strftime('%B'))
    response = urllib.urlopen(url)
    calendar = json.loads(response.read())

    # Copy every "days" element into a dict.
    days = {}
    for week in calendar['weeks']:
        for day in week['days']:
            if day['designation'] != None:
                days[day['day']] = day['designation']


    # Get the designation for tomorrow.
    designation = days[str(tomorrow.strftime('%d'))]

    # Select the rate table and periods for tomorrow's date and designation.
    for season in RATES:
        if tomorrow >= dt.datetime.strptime(season['date_start'], '%Y-%m-%d') \
            and tomorrow <= dt.datetime.strptime(season['date_end'], '%Y-%m-%d'):
            rate_table = season['designation'][designation]
            periods = season['periods']
            break

    # Combine the rate table and periods.
    print rate_table
    print periods

    # Send the result to stdout

if __name__ == "__main__":
    main()
