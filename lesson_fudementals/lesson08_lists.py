
empty_list=[]


animals=["Donkey", "pangolin", "blobfish"]
numbers=[2,4,6,8,10]
mixed=["piffle", 42, True, 9.99]

print("Animals list:", animals)
print("Numbers list:", numbers)
print("Mixed data types list", mixed)

print(animals[2])
print(numbers[4])
print(mixed[0])

animals[-1] = "babirusa"
print(animals)

animals.append("glass frog")

print(animals)

animals.insert(2,"aye-aye")
print(animals)

last_animal = animals.pop()
print(last_animal)
print(animals)


# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*
list_no=[ 1, 2, 3, 4, 5, 6 ] 
new_int=input(f"Enter an integer:")
list_no[4] = new_int
print(list_no)

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Numbers:", nums)

print("Length of list:", len(nums))
print("Min:", min(nums))
print("Max:", min(nums))
print("Sum", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)


if "cat" in animals:
    print("Cat is in the list")
else:
    print("cat not in list")



### Challenge 3: Number Stats

# Create a list of five floats called measurements.
# Print the length, minimum, maximum, and sum of the list using built-in functions.

measure=[4.1, 3.4, 9.8, 8.9, 4.5 ]

print("Length of list:", len(measure))
print("Min:", min(measure))
print("Max:", max(measure))
print("Sum", sum(measure))
