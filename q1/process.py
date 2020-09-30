import csv
import datetime
import os
import sys


def csv_generator(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


def process(input, output):
    content = csv_generator(input)
    next(content)  # skip headers
    with open(output, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["first_name", "last_name", "price", "above_100"])  # headers
        for name, price in content:
            if name.strip():  # filter empty names
                name_list = name.strip().split(" ")
                if name_list[0] in ["Ms.", "Miss", "Mrs.", "Mr.", "Dr."]:  # exclude salutations
                    first, last = name_list[1:3]
                else:
                    first, last = name_list[:2]
                writer.writerow([first, last, price.lstrip("0"), "true" if float(price.lstrip("0")) > 100 else None])


if __name__ == "__main__":
    if len(sys.argv) == 3:  # allow input output filenames to be supplied from command line.
        input, output = sys.argv[1:3]
    else:  # if not supplied then use default files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        input, output = os.path.join(dir_path, "dataset.csv"), os.path.join(dir_path, "result.csv")
    process(input, output)
    print("processing finished at " + str(datetime.datetime.now()))
