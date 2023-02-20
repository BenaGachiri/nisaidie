# import functions

# x=functions.add(50,9)
# x=functions.difference(60,14)




# from functions import add 
# =add(30,50)


import operators
import others
import trig

sin_of_angle




operator=input("enter operator:")
if operator=="cube":
 num=eval(input("enter number:"))
 x=others.cube(num)
 print(x)



elif operator=="sin":
    angle=eval(input("enter angle in degrees"))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle)


    
else:
    num1=eval(input("enter number1:"))
    num2=eval(input("enter number2:"))


if operator=="*":
    r=operators.multiply(num1,num2)
    print(r)
elif operator=="/":
    r=operators.divide(num1,num2)
    print(r)

elif operator=="*"or"x"or"X":
   
    r=operator.multiply(num1,num2)
    print(r)

    r=operator.cube(num1)
    print(7)


