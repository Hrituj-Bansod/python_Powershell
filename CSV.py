import csv

with open('sample.csv' , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for lines in csv_reader:
        print(lines) 