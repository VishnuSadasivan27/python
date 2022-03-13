word = str(input('Enter the word : '))
for i in range(len(word)):
    print(f'{word[i]} -> {ord(word[i])}')