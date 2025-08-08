while True:
    # input a number
    num = int(input("Enter a number: "))
    t = num
    numLen = 0
    # iterate the loop
    while t > 0:
        numLen += 1
        t = int(t / 10)

    if numLen >= 4:  # Condition 1
        numLen_half = int(numLen / 2)
        chk = 0
        temp = num
        while temp > 0:  # iterate loop
            rem = temp % 10
            if chk == numLen_half:
                midOne = rem
            elif chk == (numLen_half - 1):
                midTwo = rem
            chk += 1
            temp = int(temp / 10)
        prod = midOne * midTwo  # Product of middle digits
        # display the result with style formatting
        print(
            "\nProduct of middle digits (" + str(midOne) + " and " + str(midTwo) + ") of " + str(num) + " is: \033[1;34m" + str(prod) + "\033[0m"
        )
        break
    else:
        print("\n\033[1;31mNumber should be 4 or more digits long. Please try again.\033[0m")