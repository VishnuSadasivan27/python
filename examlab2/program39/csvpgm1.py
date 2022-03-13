import csv
with open("mycsv.csv") as csvfil:
    d = csv.reader(csvfil)
    count=0
    fsa = []
    for i in d:
        count = count + 1
        print(i)
        if count > 10:
           break
