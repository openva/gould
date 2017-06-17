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

    # Retrieve the JSON for this month.
    # Yes, we've hard-coded "2015," because Dominion has done the same. See
    # https://github.com/openva/gould/issues/2 for details.
    url = 'https://www.dominionenergy.com/api/smartpricing/getmonth?year=' \
        + str(tomorrow.strftime('%Y')) \
        + '&monthname=' \
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
    designation = str.lower(str(days[str(tomorrow.strftime('%-d'))]))

    # Select the rate table and periods for tomorrow's date and designation.
    for season in RATES:
        if tomorrow >= RATES[season]['date_start'] \
            and tomorrow <= RATES[season]['date_end']:
            rate_table = RATES[season]['designation'][designation]
            periods = RATES[season]['periods']
            break

    # Combine the rate table and periods.
    combined = []
    for id in periods:
        tmp = {}
        tmp['start'] = periods[id]['start']
        tmp['end'] = periods[id]['end']
        tmp['rate'] = rate_table[id]
        combined.append(tmp)

    # Add a header stanza.
    output = {}
    output['meta'] = {}
    output['meta']['generated'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    output['meta']['provider'] = 'Dominion'
    output['meta']['state'] = 'VA'
    output['meta']['documentation'] = 'https://github.com/openva/gould/'
    output['date'] = tomorrow.strftime('%Y-%m-%d')
    output['schedule'] = combined

    # Send the result to stdout
    print json.dumps(output)

if __name__ == "__main__":
    main()
