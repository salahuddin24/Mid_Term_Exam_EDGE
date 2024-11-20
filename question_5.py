# question : Given a list of integers, write a program that creates a new list containing only the numbers greater than 10 from the original list [5, 12, 7, 18, 3, 22, 9] and print the new list.

lists = [5, 12, 7, 18, 3, 22, 9]
newlist = []
for list in lists:
    if list > 10:
        newlist.append(list)

print(newlist)
























