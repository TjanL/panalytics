#!/usr/bin/env python3
import argparse
import csv
import datetime
import json
import locale
import re
from pathlib import Path

reg = re.compile(r"([0-9]+)\.*\s*(\w*).*poop.*(\d+)",
                 flags=re.IGNORECASE | re.DOTALL)


def parse_file(filename, month):
    with open(filename, encoding="utf8") as file:
        data = json.load(file)

    parsed_data = []
    for message in data["messages"]:
        content = message["content"]
        match = reg.search(content)
        if match and match.group(2).lower() == month:
            date = f"{match.group(1)}. {match.group(2)}"
            poop_count = match.group(3)
            parsed_data.append({"Date": date, "Poops": poop_count})

    return parsed_data


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", metavar="dir", help="Input dir", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "sl_SI")
    args = parse_args()
    for path in Path(args.d).glob("*.json"):
        this_month_first_day = datetime.date.today().replace(day=1)
        prev_month_last_day = this_month_first_day - datetime.timedelta(days=1)
        prev_month = prev_month_last_day.strftime("%B")

        data = parse_file(path, prev_month)

        with open(f"{Path(args.d).joinpath(path.stem)}.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Poops"])
            writer.writeheader()
            writer.writerows(data)
