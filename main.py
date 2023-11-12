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

utensils = {'fork', 'spoon', 'knife'}
dishes = {'plate', 'bowl', 'cup', 'knife'}

utensils.add('Jar')
# utensils.pop()
dishes.update(utensils)
# print(utensils.intersection(dishes))

print(dishes)
