#!python3
"""
Assignment: Exchange rate
The current exchange rate is 1.25 CAD per 1 USD
Create a program that asks the user for the number of Canadian Dollars they have
and then have the program display how many USD that is equivalent to:
You may need to use rounding or decimal formatting


example
How many Canadian Dollars do you have? 10
That is worth $8.00 USD

How many Canadian Dollars do you have? 1.25
That is worth $1.00 USD
"""
import math

population = float(input("Enter the current population: "))
rgrowth = float(input("Enter the rate of growth: "))
time = int(input("Enter the time in days: "))
futurepopulation = (population)*(1 + (rgrowth / 100))**(time/365)
futurepopulation = round(futurepopulation)
print(f"there will be {futurepopulation} people after {time} days")