# Write a program that prints all the prime numbers less than 1000. You can write
# this program by creating a list of prime numbers. To begin, the list is empty.
# Then you write two nested for loops. The outer for loop runs through all the
# numbers from 2 to 999. The inner for loop runs through the list of prime
# numbers. If the next number in the outer for loop is not divisible by any of the
# prime numbers, then it is prime and can be printed as a prime and added to the
# list of primes. To add an element. ie, to a list, lst, you can write lst.append(e).
# This program uses both the guess and check pattern and the accumulator
# pattern to build the list of prime numbers.
primes = []

for number in range(2, 1000):

    is_prime = True

    for prime in primes:

        if number % prime == 0:
            is_prime = False
            break

    if is_prime:
        print(number)
        primes.append(number)



