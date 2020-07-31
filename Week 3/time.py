# inputs
# if statements
# valid or invalid output

# inputs
h = int(input("Enter the hours: "))
m = int(input("Enter the minutes: "))
s = int(input("Enter the seconds: "))

print("h", h)
print("m", h)
print("s", s)

# if statements
if (0 <= h <= 23) and (- 1 < m < 60) and (- 1 < s < 60):
    print("Your time is valid. ")
else:
    print("Your time is invalid. ")
