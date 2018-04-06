# P5T2 - Feet to Inches
# April 5, 2018
# CTI 110
# Jessica Thompson

INCHES_PER_FOOT = 12

def main():
    feet = int(input("Enter a number of feet: "))

    print(feet, "ft equals", feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

inches = feet_to_inches(1)


main()
