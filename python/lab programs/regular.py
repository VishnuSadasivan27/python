import re
file=open("text.txt","r")
text=file.readlines()
file.close()
keyword=re.compile(r'the')
for line in text:
    if keyword.search(line):
        print(line)
