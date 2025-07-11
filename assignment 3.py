
# assignment 3 part 1 :  Calculate Factorial Using a Function


n=int(input('enter the number : '))
m = n
def factorial(n):
    if n < 2  :
        return n * n
    else :
        return n * (factorial(n-1))
result = factorial(n)

print('factorial of' , m , ' is :', result)


#assignment 3 part 2 : Using the Math Module for Calculations

number=int(input('enter the number : '))

import math
print('square root :',math.sqrt(number))
print('loharithm :',math.log(number))
print('sine :',math.sin(number))