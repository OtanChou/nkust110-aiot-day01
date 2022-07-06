import csv
with open('data.csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        h = int(row['height'])
        w = int(row['weight'])
        bmi = round(w/((h/100)**2), 2)
        print(row['name'],"'s bmi is ", bmi)