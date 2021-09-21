#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

first = str(input("Insert name: ")).strip()
second = str(input("Insert adjective: ")).strip()
third = str(input("Insert food: ")).strip()
fourth = str(input("Insert adjective: ")).strip()
fifth = str(input("Insert noun: ")).strip()
sixth = str(input("Insert place: ")).strip()
seventh = str(input("Insert verb: ")).strip()
eighth = str(input("Insert adverb: ")).strip()
ninth = str(input("Insert food: ")).strip()
tenth = str(input("Insert thing: ")).strip()

print(f"Today we picked apple from {first}'s Orchard. I had no idea there were so many different varieties of apples. I ate {second} apples straight off the tree that tasted like {third}. Then there was a {fourth} apple that looked like a {fifth}.  When our bag was full, we went on a free hay ride to {sixth} and back. It ended at a hay pile where we got to {seventh} {eighth}. I can hardly wait to get home and cook with the apples. We are going to make apple {ninth} and {tenth} pies!")
