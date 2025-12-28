#Question 1 Write a function and return the dquare of a number
# def square_of_num(number):
#     return number**2
# res=square_of_num(7)
# print(res)

#Question 2 Functions with multiple params a functions that takes 2 numbers as parameters & return sum
# def sum_of_numbers(number1,number2):
#     return number1+number2
# print(sum_of_numbers(10,20))

#Question 3 Write a function multiply that multiplies two numbers but can also accept and multiply strings
# def multiply(a,b):
#     return a*b
# print(multiply(8,6))
# print(multiply('a',4))

#Question 4 Create a function that returns both area and circumference of a circle given its radius CIR:2πr Area:πr^2
# import math
# def circle_stats(radius):
#     area = math.pi* radius*radius
#     circumference=2*math.pi*radius
#     return round(area,2),round(circumference,2)
# a,c=circle_stats(10)
# print("Area",a,"Circumference",c)  
    
#Question 5 Write a function that greets a user.If no name is provided it should greet with a defaukt name
# def greet(name="User"):
#     return "Hello "+name+'!'
# print(greet("Jay"))

#Question 6 Lambda function create to compute the cube of a number
# cube=lambda x: x**3
# print(cube(3))

#Question 7 Write a function that takes a varialbe number of args and returns their sum
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2))
# print(sum_all(1,3,2,4))
# print(sum_all(1,2,3,4,5))

#Question 8 Create a funcction that accepts any number of keyword args and prints them in the format key:value
# def print_kwargs(**kwargs):
#     for key,val in kwargs.items():
#         print(f"{key}:{val}")
# print_kwargs(name="Jay")
# print_kwargs(name='gaurav', surname="jawalkar")
# print_kwargs(age=23)

#Question 9 Write a generator function that yields even numbers up to specified limit
# def even_number(number):
#     for i in range(2,number+1,2):
#         yield i
# for num in even_number(10):
#     print(num)

#Question 10 Recursive function to calculate the factorial of a number
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(17))