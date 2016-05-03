# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the user
def find_prime(lower, upper):
    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
                print(num)

find_prime(20000, 20500)
