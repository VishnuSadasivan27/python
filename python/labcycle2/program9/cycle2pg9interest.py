import math
p=float(input("enter the principle amount:"))
r=float(input("enter the rate:"))
t=int(input("enter the time span:"))
amount=p*(pow((1+r/100),t))
print(amount)
compound_interest=amount-p
print("The compound interest is",compound_interest)

