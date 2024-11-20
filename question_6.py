# question : Write a function sum_of_evens(n) that calculates and returns the sum of all even numbers from 1 to n. Use a for loop in your implementation.
number = int(input("Enter any integer number : "))

def sum_of_evens(number):
    sum = 0
    for num in range(1, number+1):
        if num % 2 == 0:
            sum += num
    return sum
result = sum_of_evens(number)
print(result)










