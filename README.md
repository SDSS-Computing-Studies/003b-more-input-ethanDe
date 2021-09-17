## SDSS Computing Studies Python Assignment
### Assignment #3b MOre Input() (Total Marks 10)

Objectives:
* Use the input() function to retrieve information from the keyboard
* Use the round() function to round to integers
* Use the round() function to round to specific decimal places
* Use the math.ceil() function to round up
* Use the math.floor() function to round down

Formatting can be very important when working with numbers.  You may want to round to a specific number of decimal places,  or round appropriately. There are also times when you might want to round down or round up all the time!

round()
The round() function can be used to round a float and change the value to an integer
```
x = 3.3
x = round(x)
print(x)
print( type(x) )
```
What is the value of x after you use the round command?
What is the variable type?
Check using the python interpreter for the answer!

The round() function can also be used to round to a specific number of decimal places
```
x = 9.2398372
x = round(x,3)
print(x)
```
The answer would clearly be of type "float", but the number has now been rounded to 3 decimal places

math.ceil() and math.floor()
These functions are used when you want to round up or round down.  There are specific times when you might want to round down.  For example, when banks do interest calculations for how much money they need to give you, they ALWAYS round down.  But if they are calculating how much money you pay them, they ALWAYS round up!
We need to import the math library in order to use these functions:
```
x = 3.2
x = math.ceil(x)
print(x)

y = math.floor(3.5)
print(y)
```

### 4 Tasks (8 marks)

##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the rate of interest expressed as a percentage.  Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.20 interest. 
(2 points) 

##### Task 2
A population can be modeled by the following:
future population = (current population)*(1+r)^(time in years) 
Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
Calculate the expected future population

Enter the population: 25000000
Enter the rate of growth in percent: 2.1
Enter the number of days: 12
There will be 25017087 people after 12 days

##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

##### Task 4
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make appple _FOOD_ and _THINGS_ pies!.