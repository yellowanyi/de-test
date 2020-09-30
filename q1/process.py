import csv


def get_csv_content(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


content = get_csv_content("dataset.csv")

with open("result.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["first_name", "last_name", "price", "above_100"])  # headers
    next(content)  # skip headers
    for name, price in content:
        if name.strip():  # filter empty names
            name_list = name.strip().split(" ")
            if len(name_list) == 2:
                first, last = name_list
            else:
                if name_list[0] in ["Ms.", "Miss", "Mrs.", "Mr.", "Dr."]:
                    first, last = name_list[1:3]
                else:
                    first, last = name_list[:2]
            writer.writerow([first, last, price.lstrip("0"), "true" if float(price.lstrip("0")) > 100 else None])
