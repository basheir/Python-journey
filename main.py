# NESTED LOOP
#
# rows = int(input("Enter how many rows: "))
# columns = int(input("Enter how many column: "))
# symbol = input("Enter the symbol you want use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# LOOP CONTROL STATEMENT


# BREAK
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# CONTINUE

# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")


# PASS

# for i in range(1, 21):
#     if i == 20:
#         pass
#     else:
#         print(i)


# LIST

# food = ['pizza', 'hamburger', 'hotdog', 'spagheti']
# food.append('Passto')
# food.append('A Rice')
# # food.pop()
# food.insert(1, 'cake')
# food.sort()
#
# for i in food:
#     print(i)


# 2D list  = a list of lists

# drink = ['coffee', 'soda', 'tea']
# dinner = ['pizza', 'hamburger', 'hotdog']
# dessert = ['cake', 'ice cream']

#
# food = [drink, dinner, dessert]
#
# for i in food:
#     print(i)


# TUPLE - COLLECTION OF ORDERED AND UNCHANGEABLE USED TO  GROUP TOGETHER RELATED DATA.
# student = ('Bashir', 33, 'male')
# print(student.count('Bashir'))
# print(student.index('male'))

# for x in student:
#     print(x)
#
# if "Bashir" in student:
#     print("Bashir is here! ")


# SET - COLLECTION WHICH IS UNORDERED, UNINDEXED. NO DUPLICATE VALUES

# utensils = {'fork', 'spoon', 'knife'}
# dishes = {'plate', 'bowl', 'cup', 'knife'}
#
# utensils.add('Jar')
# utensils.pop()
# dishes.update(utensils)
# print(utensils.intersection(dishes))
# print(dishes)

# Dictionary - A changeable, unordered collection of unique key:values pairs
#              fast because they use hashing , allow us to access a values quickly

# capitals = {'USA': 'Washinton DC',
#             'Somalia':'Mogadishu',
#             'India': 'New Delhi',
#             'Russia': 'Mosco',
#             'Germany': 'Berlin'}

# print(capitals.get('Ethiopia'))
# print(capitals.items())
# print(capitals.values())
# print(capitals.keys())
#
# for key,value in capitals.items():
#     print(key + ', ' + value)

# FUNCTION IN PYTHON - a block of code which is executed only when it is called
# first function

# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def hello(name, age, address):
#     print('Hello, ' + name + ' you are ' + str(age) + ' years old' + ' your location ' + address)
#
#
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# address = input("Enter your address: ")
# hello(name, age, address)


# Return statement - Function send Python values/objects back to the caller.
#                   These values/objects are known as the function's return value

# def multiply(number1, number2):
#     return number1 * number2
#
#
# num1 = int(input("Enter first number: "))
# numb2 = int(input("Enter second number: "))
# x = multiply(num1, numb2)
# print(x)


# KEYWORD ARGUMENT - arguments preceded by an identifier when we pass them to a full function
#                     The order of the arguments does not matter, unlike positional argument
#                     Python knows the names of the arguments that our function receive.


# def hello(firstname, middlename, lastname):
#     print('Hello, ' + firstname + ' ' + middlename + ' ' + lastname)
#
#
# hello(lastname="Abdilahi", middlename='Mahad', firstname='Bashir')
# hello(lastname="Abdilahi", middlename='Mahad', firstname='Faadumo')


# NESTED FUNCTION CALLS - function calls inside other function

# num = input("Enter a whole number positive number: ")
# # num = float(num)
# # num = abs(num)
# # num = round(num)
#
# print(round(abs(float(num))))

# RANDOM - RANDOM METHOD

# import random
#
# x = random.randint(1,6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissorss']
# z = random.choice(myList)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
# random.shuffle(cards)
#
# print(cards)

# Exception Handling

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input('Enter a number to divide by: '))
#     result = numerator / denominator
#
# except ValueError as e:
#     print(e)
#     print('Enter only number please')
# except ZeroDivisionError as e:
#     print(e)
#     print(e, ', You cannot divide by zero!')
# except Exception as e:
#     print(e)
#     print('Something went wrong!')
# else:
#     print(result)


# MODULES -  a file that containing python code. May contain a function, class, etc.
#            used with modular programming, which is separate a program into parts

# import  messages
# import messages as msg
# from messages import *
# from  messages import hello,bye
# hello()
# bye()

# help('modules')


# SIMPLE GAGE

import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print('computer: ', computer)
        print('player', player)
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('computer: ', computer)
            print('player', player)
            print('You lose!')
        if computer == 'scissors':
            print('computer: ', computer)
            print('player', player)
            print('You win!')

    elif player == 'scissors':
        if computer == 'rock':
            print('computer: ', computer)
            print('player', player)
            print('You lose!')
        if computer == 'paper':
            print('computer: ', computer)
            print('player', player)
            print('You win!')

    elif player == 'paper':
        if computer == 'scissors':
            print('computer: ', computer)
            print('player', player)
            print('You lose!')
        if computer == 'rock':
            print('computer: ', computer)
            print('player', player)
            print('You win!')
    play_again = input("Play again! (yes/no): ").lower()
    if play_again != 'yes':
        break
print("Bye!")
