greeting= "Hello"
first_name= "Ada"
print( first_name)


second_letter= greeting[1]
print(second_letter)

word= "Supercalifragilisticepalidocious"
print("\n The word is :", word)
print("The first letter is:" ,word[1])
print( "The last letter is:" , word[-1])
print("Range of letters (non-inclusive)", word[3:7] )
print("First five letters:", word[:5])
print("Everything after the first five letters",word[5:] )
print("Last seven letters", word[-7:])
print("Step through every second charater:", word[::2])
last_name= "Fairy"
length = len(last_name)


# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote= input("Enter your favorite quote please:")
print("Your quote is", len(quote),"letters long!")

# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

the_word= input("Enter a word that is at least seven letters long:")
print( "The 2nd through 6th letters of your word are:", the_word[1:7])


# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:

first_name=input("Enter your first name:" )
last_name=input("Enter your last name:" )

print("Hello", last_name, first_name)