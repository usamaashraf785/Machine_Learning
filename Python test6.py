# a = int(input("Enter a starting Value:"))
# b = int(input("Enter a Last value:"))
#
# ls = list(range(a,b+1))
# print(ls)
#
# even_numbers = []
# odd_numbers = []
# for i in ls:
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
# print(even_numbers)
# print(odd_numbers)

# Question No 2

# Write a python program that takes two numeric inputs x and y.
# a) The program should take numeric inputs continously.
# b) The program should ensure the range of x and y is between 0 and 1. If either one of the input values is out of range, smaller than 0 or greater than 1, then the program should quit.
# c) Implement the XOR gate, where the program returns 1 if both x and y values are different , otherwise, it returns 0. The program should work for floating-point values
#
# while True:
#
#
#     x = float(input("Enter X: "))
#     y = float(input("Enter Y: "))
#     if ((x >= 1) & (y >= 1)) or ((x <= 0) & (y <= 0)):
#
#     # if (0 >= x) or (x <= 1):
#     #     pass
#         break
#     if (x == y):
#         print("1")
#     else:
#         print("0")
#
# print("Quite")

# 1. Write a Python program to print the following string in a specific format (see the
# output).
# Twinkle, twinkle, little star,
#        How I wonder what you are!
#                Up above the world so high,
#                Like a diamond in the sky.
#Twinkle, twinkle, little star,
#       How I wonder what you are


# \n, //,
# print("Twinkle, twinkle, little star,")
# print("\t\tHow I wonder what you are!")
# print("\t\t\t\tUp above the world so high,")
# print("\t\t\t\tLike a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("\t\tHow I wonder what you are")


# 4. Write a Python program which accepts the radius of a circle from the user and compute
# the area.
# from math import pi
# r = float(input("Enter Radius:"))
# areas = pi * (r**2)
#
# print(areas)

 # 5. Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

# first_name = input("Enter First name:")
# last_name = input("Enter Last name:")
#
# rev_fn = first_name[::-1]
# rev_ln = last_name[::-1]
# print(rev_fn,rev_ln)

# from math import  factorial
#
# print(factorial(5))
#


# 10.Write a Python program to sum all the numeric items in a list?

# ls = [2,3,'A',4,'y', 9.5 , 10.3]
# num = 0
# for i in ls:
#     if (type(i) == int) or (type(i) == float):
#         num += i
# print(num)

# 12. Take a list, say for example this one:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# #  Write a program that prints out all the elements of the list that are less than 5.
# for i in a:
#     if (i<5):
#         print(i)

# 6. Write a Python script to check if a given key already exists in a
# dictionary
# dic1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# def func():
#     ky = input("Enter a Key:")
#     for i in dic1.keys():
#         if (ky == i):
#             print("Key is already existed!")
#             break
#         else:
#             print("Key is not existed!")
#             break
#
# func()










# user input = "ahmed.gillani@uet.edu.pk"
# user input = "abc.def@dfki.de"

# firtname = ahmed , abc
# lastname = gillani, def
# email = uet.edu.pk, dfki.de

user_email = input("Enter Your Email:")

# first_name = ""
# last_name = ""

# for i in user_email:
# email1 = user_email.split('@')[1]
# names = user_email.split('@')[0].split('.')
# first_name = names[0]
# second_name = names[1]
# emails = email1[1]
# print(first_name)
# print(second_name)
# print(email1)

floc = user_email.find(".")

print("Firest Name:",user_email[:floc])

lloc = user_email.find("@")

print("Last Name:", user_email[floc+1:lloc])

print("Email:", user_email[lloc+1:])









