#                                                                                     Lab 1
#                                                                                     -----
#Question 1
#----------
# firstname = input("Enter your First Name : ")
# name1 = firstname[::-1]
# lastname = input("Enter your Last Name : ")
# name2 = lastname[::-1]
# print ("Reverse:  " + name2 + " " + name1)

#-----------------------------------------------------------------------------
#Question 2
#----------
# x=int(input("Enter a number:"))
# num= (x+ ((x*10)+x) + ((x*100)+(x*10)+x))
# print("Result = " ,num)

#-----------------------------------------------------------------------------
#Question 3
#----------
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example""")

#-----------------------------------------------------------------------------
#Question 4
#----------
# r=float(input("Enter a number:"))
# v=(4.0/3.0)*3.14*r
# print("Volume of the sphere= ", v);  

#-----------------------------------------------------------------------------
#Question 5
#----------
# base = float(input("Input the base : "))
# height = float(input("Input the height : ")) 
# area = (base*height)/2 
# print("Area of Triangle = ", area)

#-----------------------------------------------------------------------------
#Question 6
#----------
# n=5;
# for i in range(n):
#    for j in range(i):
#        print ('* ', end="")
#    print('')
# for i in range(n,0,-1):
#    for j in range(i):
#        print('* ', end="")
#    print('')

#-----------------------------------------------------------------------------
#Question 7
#----------
# word = input("Enter the word you want : ")
# reverse = word[::-1]
# print("Reversed Word = " + reverse)

#-----------------------------------------------------------------------------
#Question 8
#----------
# for i in range(7):
#   if (i == 3 or i==6):
#       continue
#   print(i, end=" ")

#-----------------------------------------------------------------------------
#Question 9
#----------
# a, b = 0, 1
# while b < 50:
#    print(a, end=" ")
#    a, b = b, a+b

#-----------------------------------------------------------------------------
#Question 10
#----------
string = input("Enter a string: ")

number_digits = 0
number_letters = 0


for char in string:
    if char.isdigit():
        number_digits += 1
    elif char.isalpha():
        number_letters += 1

print("Number of digits:", number_digits)
print("Number of letters:", number_letters)