dic={"c":3,
     "a":1,
     "d":4,
     "f":6,
     "e":5,
     "b":2}
sorteddic = sorted([(value,key) for (key,value) in dic.items()])
print("sorted dictionary is")
print(sorteddic)