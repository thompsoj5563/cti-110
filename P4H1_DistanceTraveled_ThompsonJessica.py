#CTI 110
#Jessica Thompson
#March 15, 2018
#P4H1 - Distance Traveled

speed = int(input("Enter the speed in mph: "))

hours = int(input("How many hours were traveled?: "))

print("Hours \t Distance Traveled")
print("-----------------------------------")


for hours in [1, 2, 3]:
    distance = speed * hours
    print(hours, "\t", distance)
