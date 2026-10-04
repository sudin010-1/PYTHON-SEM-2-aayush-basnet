# 10. Countdown Timer
# Start from a given number and count down to 1,
# decreasing the number by 1 each time.

num = int(input("Enter a number to start countdown: "))

while num >= 1:
    print(num)
    num -= 1

print("Time's up!")
