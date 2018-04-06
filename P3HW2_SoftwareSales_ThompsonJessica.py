# CTI-110 
# P3HW1 - Software Sales
# Jessica Thompson
# 02/23/2018
#

numberofpackages = int(input("Enter the number of packages purchased: "))

packageprice = 99

def main():
    if numberofpackages < 10:
        discount = 0
    elif numberofpackages < 20:
        discount = .10
    elif numberofpackages < 50:
        discount = .20
    elif numberofpackages < 100:
        discount = .30
    elif numberofpackages >= 100:
        discount = .40

    subtotal = numberofpackages * packageprice
    discountamount = discount * subtotal
    total = subtotal - discountamount

    print("Amount of discount: $", format(discountamount, ",.2f"))
    print("Total: $", format(total, ",.2f"))

main()
