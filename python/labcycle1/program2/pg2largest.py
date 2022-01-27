a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("enter the third number:"))
d = max(a,b,c)
print(d)
if(a>b) and (a>c):
    larg=a
elif(b>a) and (b>c):
    larg=b
else:
    larg = c
print("largest of the three number is:",larg)