#!/usr/bin/env python3
import json
from pathlib import Path
import re
import csv
import argparse
import datetime

reg = re.compile(r"([0-9]+[ ]*[.][ ]*\w*).*poop\D*(\d+)",
                 flags=re.IGNORECASE | re.DOTALL)


def parse_file(filename):
    with open(filename, encoding="utf8") as file:
        data = json.load(file)

    parsed_data = []
    for message in data["messages"]:
        content = message["content"]
        match = reg.search(content)
        if (match):
            date = ". ".join("".join(match.group(1).split()).split("."))
            poop_count = match.group(2)
            parsed_data.append({"Date": date, "Poops": poop_count})

    return parsed_data


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", metavar="dir", help="Input dir", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    for path in Path(args.d).glob("*.json"):
        data = parse_file(path)

        with open(f"{Path(args.d).joinpath(path.stem)}.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Poops"])
            writer.writeheader()
            writer.writerows(data)
