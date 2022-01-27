list = [4, 1.4, 53, 12, 3,44,"kerela"]
reversed_list=[]
print("The list is :",list)
for i in reversed(range(0, len(list))):
    reversed_list.append(list[i])
print("reversed list is:",reversed_list)