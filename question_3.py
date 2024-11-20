# question : write a python program to remove all even numbers from the list [2, 3, 5, 7, 8, 10, 11, 12, 13, 14] and print the updated list.
lists =  [2, 3, 5, 7, 8, 11, 12, 13, 14, 10]
updatedList = []
for num in lists:
    if num % 2 != 0:
        updatedList.append(num)
    # if num % 2 == 0:
    #     print(num)
    #     lists.remove(num)
# print(lists)
print(updatedList)
#*** another way
# updated_list = [num for num in lists if num % 2 != 0]
# print(updated_list)








