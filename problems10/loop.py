#Question 1 Count Positive numbers 
# number=[1,-2,3,-4,5,6,-7,-8,9,10]
# positive_num_count=0
# for num in number:
#     if(num>0):
#         positive_num_count += 1
# print("Final Count of Positive Number is: ",positive_num_count)

#Question 2 Sum of Even Numbers : Calculate even numbers up to given number n
# n=10
# sum_even=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even+=i    
# print("Sum of Even numbers : ",sum_even)

#Question 3 Multiplication Table Printer skip the fifth iteration
# n=int(input("Enter number you want multiplication : "))
# for i in range(1,11):
#     if i==5:
#         continue
#     print(n,"x",i,"=",n*i)

#Question 4 Reverse a String using loop
# input_str="abcde"
# reversed_str=''
# for char in input_str:
#     reversed_str=char+reversed_str
# print(reversed_str)

#Question 5 Find First non repeated character
# input_str="tweets"
# for char in input_str:
#     if input_str.count(char) == 1:
#         print("Char is ",char)
#         break

#Question 6 Factorial 
# num=5
# fact=1
# while num>0:
#     fact*=num
#     num-=1
# print(fact)

#Question 7 Validate Input keep asking user number between 1 and 10 until entered
# while True:
#     num=int(input("Enter a Number : "))
#     if 1<=num <=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number Enter again ")

#Question 8 Prime Number check if number is prime or not
# num=6
# isPrime=True
# if num>1:
#     for i in range(2,num):
#         if (num % i)==0:
#             isPrime=False
#             break
# print(num,"is",isPrime)

#Question 9 Check if all elements in list are unique 
# items=["apple","banana","orange","apple","mango"]
# unique_item=set()
# for item in items:
#     if item in unique_item:
#         print("DUPLICATE ",item)
#         break
#     unique_item.add(item)

#Question 10 Implement Exponential Backoff stratergy double wait time between retries starting from 1 sec but stop at 5 retries
# import time

# wait_time=1
# max_retries=5
# attempts=0

# while attempts<max_retries:
#     print("Attempt ",attempts+1,"wait time",wait_time)
#     time.sleep(wait_time)
#     wait_time *=2
#     attempts+=1
