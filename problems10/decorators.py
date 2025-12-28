#Question 1 Write a decorator that measures the time a function takes to execute
# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result= func(*args,**kwargs)
#         end=time.time()
#         print(f"{func.__name__} ran in {end-start}")
#         return result
#     return wrapper

# @timer
# def example(n):
#     time.sleep(n)
    
# example(2)

#Question 2 Create a decorator to print the function and the values of its arguments every time the function is called


# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_val=', '.join(str(arg) for arg in args)
#         kwargs_val=', '.join(f"{k}={val}"for k,val in kwargs.items())
#         print(f"CALLING {func.__name__} with args {args_val} and kwargs {kwargs}")
#         return func(*args,**kwargs)

#     return wrapper
# @debug
# def hello():
#     print("Hello")
    
# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")

# hello()
# greet("Jay",greeting="hola")

#Question 3 Cache returns values of a function so that when its called with the same argumenr the cached value is returned
#instead of re-executing function
import time

def cache(func):
    cache_val={}
    print(cache_val)
    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
        result=func(*args)
        cache_val[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))
print(long_running_function(2,3))

