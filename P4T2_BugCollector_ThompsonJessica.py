# CTI 110
# Jessica Thompson
# March 14, 2018
# P4T2 - Bug Collector

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1,8):
    # Prompt the user.
    print("Enter the bugs collected for day", day)
    #Input the number of bugs.
    bugs = int(input())
    # Display the total.
    total = total + bugs

print("You collected a total of ", total, "bugs.")
