# question: Write a recursive function count_down(n) that prints numbers from n down to 1. Use the function to count down from 5.
def count_down(n):
    if n <= 0:
        return 
    print(n)
    count_down(n-1)
count_down(5)































