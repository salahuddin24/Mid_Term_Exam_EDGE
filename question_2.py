# question : write a function divisible_by_3-or_5(n) that prints number from 1 to n. For numbers divisible by 3, print "Divisible by 3" . For numbers divisible by 5, print "Divisible by 5". if a number is divisibel by both, print " Divisible by both".
def divisible_by_3_or_5(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num}, Divisible by both")
        elif num % 3 == 0:
            print(f"{num}, Divisible by 3")
        elif num % 5 == 0:
            print(f"{num}, Divisible by 5")
        else:
            print(num)
divisible_by_3_or_5(5)



