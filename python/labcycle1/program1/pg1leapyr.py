startyear=int(input("enter the starting  year"))
endyear=int(input("enter the last year"))
if(endyear>startyear):
  for year in range( startyear , endyear+1):
    if( year % 4 == 0) and (year % 100 != 0 or  year % 400 == 0):
       print(f"{year}:is a leap year")
else:
    print("entered year has an error")