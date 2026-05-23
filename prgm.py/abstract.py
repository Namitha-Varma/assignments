# from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount,balance):
#         try:
#             if amount<=0:
#                 raise ValueError
#             else:
#                 print("Payment processing")
#                 balance-=amount
#                 print(balance)
#         except ValueError:
#             print("enter a valid amount")

# class UPIPayent(Payment):
#     def __init__(self,balance):
#         self.__balance=balance
#     def pay(self,amount):
#         super().pay(amount,self.__balance)
        

# account = UPIPayent(50000)
# account.pay(1000)





#even or odd
# n = 6
# if n / 2:
#     print("even number")
# else:
#     print("odd number")


#divisible by 5 but not by 10
# n = 30
# if n % 5 == 0:
#     print("satisfy")
# elif n % 10 == 0:
#     print("unsatisfy")

#biggest among two numbers
# a = 4
# b = 7
# if a>b:
#     print(a,"biggest")
# else :
#     print(b,"biggest")

#divisible by 2,3 and 6
# n = 18
# if n / 2 and n /3 and n / 6:
#     print(n,"satisfy")

#voting eligibility
# age = 19
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

#student pass/fail based on all subjects >=35
# maths = 40
# physics = 48
# chemistry = 30
# if maths >= 35 and physics >= 35 and chemistry >= 35 :
#     print("pass")
# else:
#     print("fail")

#passed if any one subject >=35
# aths = 40
# physics = 48
# chemistry = 30
# if maths >= 35 or physics >= 35 or chemistry >= 35 :
#     print("pass")
# else:
#     print("fail")

#passed if any two subjectes>=35
# maths = 40
# physics = 20
# chemistry = 36

# if ((maths >= 35 and physics >= 35) or
#     (maths >= 35 and chemistry >= 35) or
#     (physics >= 35 and chemistry >= 35)):
#     print("Pass")
# else:
#     print("Fail")

#biggest among 3 numbers
# a = 7
# b = 4
# c = 9
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else :
#     c>a and c>b
#     print(c)

#smallest among three numbers
# a = 7
# b = 4
# c = 9
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# else :
#     c<a and c<b
#     print(c)

# perfect square root or not
# import math
# number = int(input("enter a number:"))

# # Find square root
# root = int(math.sqrt(number))

# # Check if square of root is equal to the number
# if root * root == number:
#     print("Perfect square")
# else:
#     print("Not a perfect square")

# Cars Required for Members (Max 5 per car)
# Python program to calculate cars needed
# import math
# members = 17
# # Each car can hold 5 people
# cars_needed = math.ceil(members / 5)
# print("Cars needed =", cars_needed)

# 


# import sys

# input_data = list(map(int, sys.stdin.read().split()))

# n = input_data[0]
# m = input_data[1]

# v = input_data[2:2 + n]
# d = input_data[2 + n:2 + 2 * n]


# # Count how many meals give at least x taste points
# def count_meals(x):
#     total = 0
#     for i in range(n):
#         if v[i] >= x:
#             total += (v[i] - x) // d[i] + 1
#     return total


# # Binary search for threshold
# low, high = 1, max(v) + 1

# while low < high:
#     mid = (low + high + 1) // 2
#     if count_meals(mid) >= m:
#         low = mid
#     else:
#         high = mid - 1

# threshold = low 

# # Compute answer
# total_meals = 0
# answer = 0

# for i in range(n):
#     if v[i] >= threshold:
#         k = (v[i] - threshold) // d[i] + 1

#         # Sum of arithmetic sequence:
#         # v[i] + (v[i]-d[i]) + ... (k terms)
#         last = v[i] - (k - 1) * d[i]
#         answer += k * (v[i] + last) // 2

#         total_meals += k

# # Remove extra meals if we selected more than m
# answer -= (total_meals - m) * threshold

# print(answer)
# h = ['Hello Guys', True, [1,4,6,8]]
# print(h[0][6:11])
# print(h[2][0:3:11])

# 8989
# cikt
# 8.0
# @@@
# False("9898",False)

# slicing and indexing

# d = [{"a":["cricket", "foot ball"],
#       "b":("9898",False)},
#       "78.0",
#       8765,
#       "@6@8@"
#       ]
# print(d[0]["a"][0][0:10:2])
# print(d[0]["b"][0][::-1])
# print(d[0]["b"][1])
# print(d[1][1:4])
# print(d[3][::2])
# print(d[0]["b"][0:2:1])

# characters -->conditions
# "A"<=ch<="Z"
#  "a"<=ch<="z"
# "0"<=ch<="9"
#  ord() -->chr to ASCII
#  chr() -->ASCII to chr

# WAP to check a given character is alphabet or not
# ch = input("Enter a character:")
# if "A"<=ch<="z" or "a"<=ch<="z" :
#     print("Alphabet")
# else:
#     print("Not an alphabet")

# # for digit
# ch = input("Enter a character:")
# if "0"<=ch<="9" :
#    print("Digit")


#special characters
# ch = input("Enter a character:")
# if "A"<=ch<="Z" and "a"<=ch<="z" and "0"<=ch<="9" :
#     print(" characters")
# else:
#     print("special characters")


# 
# ch = input("enter a character:")
# if 'A'<=ch<='Z' or "a"<=ch<="z":
#     print(ord(ch),ch)
# elif "0"<=ch<="9":
#     a=ord(ch)+1
#     print(a,chr(a))
# else:
#     l=[]
#     l.append(ord(ch))
#     print(l,ch)


#if ch is alphabet print mid value, if digit store in dictionary, if special character , reverse it
# ch = input("enter a character:")
# if 'A'<=ch<='Z' or "a"<=ch<="z":
#     print(ch[len(ch)//2])
# elif "0"<=ch<="9":
#     d={}
#     d[ch[0]]=ord(ch[0])
#     print(d)
# else:
#     print(ch[::-1])

# single value ,multi value
# data = eval(input("enter any data:"))
# if type(data) in (int,float,bool,complex,None):
#     print("single value data type")
# elif type(data) in [str,tuple,list,set,dict]:
#     print("multi value data type")


# the middle element of a given list is odd or not, if it is odd then print oddd then print the number else directly print the number
# l=[30, 40, 7, 67, 78]
# mid_index = len(l) // 2
# mid_value = l[mid_index]
# if mid_value % 2 != 0:
#     print("Odd")
#     print(mid_value)
# else:
#     print(mid_value)



# vowels
# ch = input('enter a character:')
# vowels = "a,e,i,o,u,A,E,I,O,U"
# if ch in vowels:
#     next_char = chr(ord(ch) + 1)
#     print("Next character is:", next_char)
# else:
#     print("Entered character is not a vowel")


#  a multi valued data 
# data = eval(input("enter data"))
# if type(data) in (str, list,tuple,set, dict):
#     t = (data,)
#     print(t)


# WAp if is already fixed with "not" print string, else add "not" to that string:
# s = input('enter a str:')
# if s.startswith("not") :
#     print(str)
# else:
#     print("not "+s)













   
