list1 = [5, 6, 32, 6, 2]
list2 = [39, 4, 6, 2]

print(f'List 1 : {list1}')
print(f'List 2 : {list2}')
print("\n")
print(" checking list are of same length:")
if len(list1) == len(list2):
    print(f"The length of the both lists are same i.e. {len(list1)}")
else:
    print(f"The lengths of two lists are different !! list1 -> {len(list1)} and list2 -> {len(list2)}")

print("checking list sums to same value:")
list1_sum = sum(list1)
list2_sum = sum(list2)
print("")
if list1_sum == list2_sum:
    print(f"The list sums are equal i.e. {list2_sum}")
else:
    print(f"The list sums are diiferent : sum of list1 -> {list1_sum} and sum of list2 -> {list2_sum}")

print("")
print("checking if any value occur in both")
for i in list1:
    if i in list2:
        print(f"{i} occurs in both")