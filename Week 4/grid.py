# Python program to print Even Numbers in given range

n = int(input("Enter the start number: "))

if -6 < n < 2:
    for x in range(n, 37, 7):
        for j in range(x, x + 7):
            print("{:>2}".format(j), end=" ")
        print()

