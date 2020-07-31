
def rem(a, b):  # function to calculate remainder
    return a % b


Year = int(input("Enter the First year: "))  # accepting input from user
yr2 = int(input("Enter the Second year: "))
while Year <= yr2:  # continues till the last year range
    k = rem(Year, yr2)
    t1 = rem(Year - 1, 4)
    t2 = rem(Year - 1, 100)
    t3 = rem(Year - 1, 400)
    t4 = 1 + 5 * t1 + 4 * t2 + 6 * t3
    day = rem(t4, 7)  # checking for day
    if day == 0:
        print("The 1st of January ", Year, " falls on a Sunday.")
    elif day == 1:
        print("The 1st of January ", Year, " falls on a Monday.")
    elif day == 2:
        print("The 1st of January ", Year, " falls on a Tuesday.")
    elif day == 3:
        print("The 1st of January ", Year, " falls on a Wednesday.")
    elif day == 4:
        print("The 1st of January ", Year, " falls on a Thursday.")
    elif day == 5:
        print("The 1st of January ", Year, " falls on a Friday.")
    else:
        print("The 1st of January ", Year, " falls on a Saturday.")

    Year = Year + 1  # increasing the year

