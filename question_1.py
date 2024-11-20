# question : Write a python program that asks the user to input a sentence. Use a for loop to count how many words in the sentence contain the letter "e". Prite the total count of such words.
from itertools import count

sentence = input("Enter a sentence : ")
count = 0
for sen in sentence:
    if sen == "e" or sen=="E":
        count += 1
print(f"The character 'e' occurs {count} times in the sentence.")




