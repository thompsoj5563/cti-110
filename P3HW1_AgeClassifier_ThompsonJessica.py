# CTI-110 
# P3HW1 - Age Classifier 
# Jessica Thompson
# 02/22/2018
#

age = int(input("Enter the person's age: "))
def main():
    if age <= 1:
        print("This person is an infant.")
    elif age < 13:
        print("This person is a child.")
    elif age < 20:
        print("This person is a teenager.")
    if age >= 20:
        print("This person is an adult.")

main()
