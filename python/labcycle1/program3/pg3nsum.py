n = int(input("Enter the first number:"))
mult=1
sum=0
for i in range(1,n+1):
   mult = int(mult*n)
   sum = int(sum+mult)
print("the sum of n number is:",sum)
