# Program to list prime numbers in a given range, take two inputs from user
lower = int(input("\033[1;32mEnter a lower range: \033[0m"))
upper = int(input("\033[1;32mEnter an upper range: \033[0m"))

print(f"\033[1;32mPrime numbers between {lower} and {upper} are:\033[0m")

# iterate loop from lower limit to upper limit
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(f"\033[1;32m{num}\033[0m")