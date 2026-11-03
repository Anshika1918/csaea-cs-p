# import time
# animals = ["lamb", "sheep", "cow", "goose", "donkey"]


# print("\nOur animals:", animals)

# # for animal in animals:
# #     print("Now I'm petting a", animal)
# #     time.sleep(2)


# for i in range(5): 
#     print("Counting", i)

# for num in range(2, 11, 2):
#     print (num)



# fav_word = "Shennanigans"
# print(fav_word)
# letter_list = []

# for letter in fav_word:
#     print(letter)
#     letter_list.append(letter)



#     # Challenge 1: Sum Calculator
# # Use a for-loop to find the sum of numbers from 1 to 10.
# # ie, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# # Expected output: 55
# print()
# total=0
# for i in range(1,11):
#   total=total+1
# print(total)

# count = 0 

# while count < 5:
#     print(f"Loopin' -- We are on loop index # {count}") 
#     count += 1
#     time.sleep(0.5)




# user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to escape:")




# #Loop Control Statements

# for i in range(1,11):

#     if i == 3: 
#         print("Skipping 3")
#         continue
#     if i == 6:
#         print("Breaking at 6")
#         break
#     if i == 9:
#         pass # place holder. does nothing. will code in the future
#     print("Number", 1)

# user_input = ""
# while user_input != "7":
#     user_input = input("Clue to escape: (The Lucky Number)  ")
#     user_input== 7
#     print("Yay you escaped")



    
    
    
    
    
import random 
secret= random.randint(1,20)
for attempt in range(5):
   guess=int (input("Enter your guess: "))
   if guess == secret:
       print("You Win!")
   elif guess> secret:
       print("too high")
   else: 
     print("too low")


     