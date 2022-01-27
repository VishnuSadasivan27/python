text = str(input("Enter the text : "))
split_words = text.lower().split()
checked_list = []

for i in range(len(split_words)):
    checked_list.append(split_words[i])
    count = 1
    if checked_list.count(split_words[i]) <= 1:
        for j in range(i + 1, len(split_words)):
             if split_words[i] == split_words[j]:
                count += 1
        print(f'Occurences of "{split_words[i]}" is : {count}')
