import csv
with open('gender_lname.csv', "r", encoding="utf-8") as fp:
       csv_reader = csv.reader(fp)
       data = list(csv_reader)
for row in data:
    if "楠梓" in row[1]:
        print(row[2], row[3], row[4])