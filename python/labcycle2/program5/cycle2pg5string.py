string =input("enter the string")
print("the orginal string:",string)
char = string[0]
string = string.replace(char,"$")
string=char+string[1:]
print(string)
