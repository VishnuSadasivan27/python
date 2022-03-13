list=[200,50,40,60,111,1111,300,6,7,12,34]
list2=[]
for value in list:
    if value>100:
        list2.append("over")
    else :
        list2.append(value)
print(list2)