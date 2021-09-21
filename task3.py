#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 5 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

first = float(input("Enter the first price: "))
second = float(input("Enter the second price: "))
third = float(input("Enter the third price: "))
fourth = float(input("Enter the fourth price: "))
fifth = float(input("Enter the fifth price: "))

tax = (first + second + third + fourth + fifth) * 0.12
tax = round(tax, 2)
subtotal = (first + second + third + fourth + fifth)
subtotal = round(subtotal, 2)
total = (first + second + third + fourth + fifth + tax)
total = round(total, 2)

print(f"Your subtotal is ${subtotal} and your taxes total ${tax} for a total of ${total}")


