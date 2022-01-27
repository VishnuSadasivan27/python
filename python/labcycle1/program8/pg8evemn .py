list=[32,4,11,15,17,18,19,21,23,66]
list2=[]
print(list)
for i in list:
    if i % 2!=0:
        list2.append(i)
print("list after removing even:")
print(list2)