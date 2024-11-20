# question : write a function is_even(n) that checks if a number n is even and print "Even " if it is, and " Odd" if it is not.
def is_even(n):
    if n <= 0:
        print("Enter a positive numbers : ")
    elif n % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(4)  # Output: Even
is_even(7)  # Output: Odd

















