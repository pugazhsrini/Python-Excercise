#combine two sorted list
a=[1,2,4,5]
b=[6,3,7,8,9,10]
print(sorted(a+b))



# The missing number

def find_missing_number(b):
    n = len(b) + 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(b)  
    return expected_sum - actual_sum  

b = [1, 2, 4, 5]
print(find_missing_number(b))



# Factorial of a number:

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=4
print(factorial(n))