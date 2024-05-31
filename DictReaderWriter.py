import csv

with open('sample.csv' , 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('new_files.csv' , 'w') as csv_file :
        fieldnames = ['period' , 'count']

        csv_writer = csv.DictWriter(new_files , filednames = fieldnames , delimiter="\t")

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
