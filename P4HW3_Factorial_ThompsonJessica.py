#CTI 110
#Jessica Thompson
#March 19, 2018
#P4HW3 - Factorial

num = int(input("Enter a nonnegative integer? "))

fac = 1

for i in range(1, num + 1):
    fac = fac * i

print("The factorial of ", num, " is ", fac)
