#CTI 110
#Jessica Thompson
#April 5, 2018
#P5T1 - Kilometer Converter

CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float(input("Enter a distance in kilometers: "))
    
    show_miles(kilometers)


def show_miles(km):
    miles = km * CONVERSION_FACTOR

    print(km, "kilometers equals", miles, "miles.")

main()
