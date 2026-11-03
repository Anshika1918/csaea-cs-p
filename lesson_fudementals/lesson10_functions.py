def say_hi():
    print("hi")
def say_bye():
    print("bye")

say_hi()
say_bye()
say_hi()
say_bye()

def express_this(e):
    return e 
expression= express_this(1+2)
print(expression)

def greeter(name):
    return f"Hi",{name}
first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")
print(first, second,third)


def remainder(a,b):
     return a % b
result=remainder(10,3)
print(result)




def is_far(distance):
    

    if distance >= 100:
        return "That's far"
    if distance < 100 and distance > 20:
        return "That's not too far"
    if distance <= 20:
        return "Hey that's pretty closeby!"


distance1= is_far(50)
distance2=is_far(190)
distance3=is_far(80)
distance4= is_far(20) 


print(distance1, distance2, distance3, distance4)

num=input("Give Me a number you want doubled:")
def want_doubled(num):
    return num * 2

num1= want_doubled(num)
num2= want_doubled(num1)
num3= want_doubled(num2)
num4= want_doubled(num3)
num5= want_doubled(num4)
print(num1, num2, num3, num4, num5 )











def doubler(num, times):
    doubled_numbers = []
    number = num

    for n in range(times):
        number = number * 2
        doubled_numbers.append(number)
        print(doubled_numbers)

    print(doubled_numbers)
    return doubled_numbers

doubler(1, 5)



def adder(a, b):
    print(a + b)
    return a + b

def subtractor(a, b): 
    print (a - b)
    return a - b

def multiplier(a, b):
    print(a * b)
    return a * b

def divider(a, b):
    print(a / b)
    return a / b

adder(3,2)
subtractor(3,2)
multiplier(3,2)
divider(3,2)




def average(a, b, c, d, e,):
    sum = a + b + c + d + e
    quotent = sum / 5
    print(quotent)
    return quotent

average(1, 2, 3, 4, 5)






def is_even(a):
    if a % 2 == 0:
        print("Even")
        return "Even"
    else:
        print("Odd")
        return "Odd"

is_even(2)




def analyze_word(word):
    
    count = 0
    print(count)
    for letter in (word):
        if letter in "aeiou":
            count = count + 1
    return f"There are {count} vowels in the word." 


vowels = analyze_word("mississippi")
print(vowels)

