#!/usr/bin/env python3
import datetime
import argparse

this_month_first_day = datetime.date.today().replace(day=1)
prev_month_last_day = this_month_first_day - datetime.timedelta(days=1)
prev_month_first_day = prev_month_last_day.replace(day=1)

parser = argparse.ArgumentParser()
parser.add_argument("--last", action="store_true")
args = parser.parse_args()

if args.last:
    print(prev_month_last_day)
else:
    print(prev_month_first_day)