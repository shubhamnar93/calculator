import os
from calculator_art import logo
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multipy(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operators={
    "+":add,
    "-":sub,
    "*":multipy,
    "/":divide,
}
stop="no"
while stop=="no":
 countinue="yes"
 os.system("cls")
 print(logo)
 n1=float(input("whats the 1st number: "))
 for operations in operators:
     print(operations)
 while countinue=="yes":
     operation_symbol=input("chose operation from above line: ")
     n2=float(input("whats the 2nd number: "))
     function=operators[operation_symbol]
     ans=function(n1,n2)
     print(f"{n1}{operation_symbol}{n2} = {ans}")
     countinue=input("Do you want to countinue 'yes' or 'no': ")
     n1=ans
 stop=input("do you want to stop 'yes' or 'no': ")