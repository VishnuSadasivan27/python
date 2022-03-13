import csv
field_name = ['No', 'Company', 'Car Model']
car = [{'No': 1,'Company':'benz','Car Model':'cH'},
       {'No': 2,'Company':'land rover','Car Model':'Xxuv'},
       {'No': 3,'Company':'Maruti Suzuki','Car Model': 'Swift'},
       {'No': 4,'Company':'ferari', 'Car Model':'rH'},
       {'No': 5,'Company':'Toyota', 'Car Model':'Fortuner'}]
with open('b.csv', 'w') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('b.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter='|')
    for r in d:
        print(','.join(r))
