import csv

input_file = "employees_data.csv"
output_file = "cleaned_data.csv"

with open(input_file, "r") as infile, open(output_file, "w" , newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    def is_valid_row(row):
        if len(row) == len(header):
            return True
        return False

    for row in reader:
        if is_valid_row(row):
            writer.writerow(row)






