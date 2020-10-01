import csv
import logging
import os
import sys

default_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=default_format)


def csv_generator(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


def process(filename):
    output_filename = filename.split(".csv")[0] + "_processed.csv"
    content = csv_generator(filename)
    next(content)  # skip headers
    with open(output_filename, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["first_name", "last_name", "price", "above_100"])  # headers
        skipped = 0
        for i, (name, price) in enumerate(content):
            if name.strip():  # filter empty names
                name_list = name.strip().split(" ")
                try:
                    if name_list[0] in ["Ms.", "Miss", "Mrs.", "Mr.", "Dr."]:  # exclude salutations
                        first, last = name_list[1:3]
                    else:
                        first, last = name_list[:2]
                    writer.writerow(
                        [first, last, price.lstrip("0"), "true" if float(price.lstrip("0")) > 100 else None])
                except:
                    logging.error(f"Error on row {i + 1}: {','.join([name, price])}")
                    skipped += 1
            else:
                logging.info(f"Empty name on row {i + 1}: {','.join([name, price])}")
                skipped += 1

    logging.info(f"processing finished for {filename}" + (f" with {skipped} rows skipped" if skipped > 0 else ""))


if __name__ == "__main__":
    if len(sys.argv) == 2:  # allow input filename to be supplied from command line.
        filename = sys.argv[1]
    else:  # if not supplied then use default files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dir_path, "dataset.csv")
    process(filename)
