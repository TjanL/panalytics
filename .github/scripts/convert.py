import json
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
    parser.add_argument("-i", metavar="file",
                        help="Input json file", required=True)
    parser.add_argument("-o", metavar="file", default=f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.csv',
                        help="Output file")
    args = parser.parse_args()

    return vars(args)


if __name__ == "__main__":
    args = parse_args()
    data = parse_file(args["i"])

    with open(args["o"], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Poops"])
        writer.writeheader()
        writer.writerows(data)
