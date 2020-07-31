n = int(input("Enter a number: "))

start = n
stop  = n + 41
step  = 7

if n>-6 and n<2:
  for i in range(start, stop, step):
    print(i, end=" ")
    print()