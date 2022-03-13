import csv
with open("mycsv.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("Name       Contribution")
    print("--------------------")
    for i in d:
        print(i['Name'], i['Contribution'])
