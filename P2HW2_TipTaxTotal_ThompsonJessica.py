# CTI-110 
# P2HW2 - Tip Tax Total 
# Jessica Thompson
# 2/15/2018

foodCost = float( input( "Enter the cost of meal: "))

tipAmount = 0.18 * foodCost

salesTax = .07 * foodCost

totalCost = foodCost + tipAmount + salesTax

print("Cost of meal: $", format(foodCost, ",.2f"))
print("Tip amount: $", format(tipAmount, ",.2f"))
print("Sales tax: $", format(salesTax, ",.2f"))
print("Total: $", format(totalCost, ",.2f"))
