
string=str(input("enter the string"))
vowels="aeiou"
string = string.casefold()
count = {}.fromkeys(vowels, 0)
for character in string:
    if character in count:
        count[character] += 1
print(count)