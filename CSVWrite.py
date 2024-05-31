import csv
with open('sample.csv' , 'r') as cssv_file:
    csv_reader = csv.reader(cssv_file)

    with open('new_file.csv' , 'w') as csv_file :
        csv_writer = csv.writer(csv_file , delimiter="-")

        for line in csv_reader:
            csv_writer.writerow(line)