print("Generate a list of four digit numbers in a given range with all their digits even and the number is a "
      "perfect square.")
l_limit = int(input("Enter the lower limit : "))
h_limit = int(input("Enter the higher limit : "))
print("The numbers which are perfect square within the given limits are : ")
for i in range(l_limit, h_limit + 1):
    if i ** 0.5 == int(i ** 0.5):
        print(f'{i}, ', end=' ')
