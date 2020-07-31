m = input("Enter the month ('January' , ...,'December'): \n ")
d = input("Enter the start day ('Monday', ..., 'Sunday'): \n ")

day = d
month = m

# number of days in a month
if month in ["January", "March", "May", "July", "August", "October", "December"]:
    x = 31
elif month in ["February"]:
    x = 28
else:
    x = 30

# Get the number of "blank spaces" we need to skip for the first week, and when to break
DAY_OFF = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
off = DAY_OFF.index(day)

print("Mo Tu We Th Fr Sa Su")

for i in range(off):
    print("  ", end=' ')

for i in range(x):
    print("%2d" % (i + 1), end=' ')

    if (i + off) % 7 == 6:
        print()
