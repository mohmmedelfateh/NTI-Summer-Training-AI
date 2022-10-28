# Q1
# str1 = "nasffjdlvwldcpoduuuuu"
# vowels = ['a','e','i','o','u']
# count=0
# for x in str1:
#     if x in vowels:
#         count=count+1
#
# print(count)

# Q2
# length=input('YOUR LENGTH: ')
# start=input('YOUR START: ')
# def array_gen(length,start):
#     list1=[]
#     for x in range(length):
#         start=start+1
#         list1.append(start)
#     print(list1)
# array_gen(5,6)

# Q3
# list2=[]
# for x in range(5):
#     inp=int(input("INPUT YOUR NUMBER: "))
#     list2.append(inp)
# print(list2)
# print('Ascending')
# list2.sort()
# print(list2)
# print('Descending')
# list2.sort(reverse=True)
# print(list2)

# Q4
# num=int(input('YOUR NUMBER: '))
# def number_check():
#     if num % 3 == 0 :
#         return ('Fizz')
#     elif num % 5 == 0 :
#         return ('Buzz')
#     elif num % 15 ==0 :
#         return ('FizzBuzz')
# print(number_check())

# Q5
# def reverse_str(str1=str(input('INPUT YOUR STRING: '))):
#     str0=str1[::-1]
#     return print(str0)
# reverse_str()

# Q6
# from math import pi
# import math
# RADIUS = int(input('INPUT YOUR RADIUS: '))
# area=math.pi*math.pow(RADIUS,2)
# print("YOUR area: " ,area)
# circumference = math.pi*RADIUS*2
# print("YOUR circumference: " ,circumference)

# Q7

# import re
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# def check(email):
#     if (re.search(regex, email)):
#         return("Valid Email")
#     else:
#         return("Invalid Email")

# name=input("enter your name")
# if name :
#     email = str(input("enter your email"))
#     if email :
#         x = check(email)
#         if x == "Invalid Email":
#             print(x)
#             print(name)
#         else:
#             print(name)
#             print(email)

# Q8

# str3='sajdpoifsapjfontinti'
# str3.lower
# x = str3.count('nti')
# print(x)

# Q9

# def alphabetical_substrings(word):
#     current_sequence = []
#     last_letter = ''
#
#     for letter in word:
#         if letter >= last_letter:
#             current_sequence.append(letter)
#         else:
#             yield ''.join(current_sequence)
#             current_sequence = []
#         last_letter = letter
#
#     if current_sequence:
#         yield ''.join(current_sequence)
# def longest_substring_in_alphabetical_order(word):
#     return max(alphabetical_substrings(word), key=len)

# print(longest_substring_in_alphabetical_order('abscdefghldksdkjsa'))
