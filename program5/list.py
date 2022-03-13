names = []
count = 0
size = int(input("Enter the size of the list of names : "))
for i in range(size):
     names.append(str(input("enter names:")))
for i in names:
    for j in i:
        if j.lower() == 'a':
            count += 1

print(f'Occurences of a in the list of first names is : {count}')
