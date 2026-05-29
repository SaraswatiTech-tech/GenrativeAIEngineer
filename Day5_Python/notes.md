## Functions in Python : 
function is reusable block of code is used to perform task 

## Function Creation in python 
in python we should create function using def keyword .
example : def function_name():
               print("hello)

* calling function 
function_name()

## Parameters
Parameters are values passed into a function 
example : def greet(name):
          print("Hello", name)

* calling function 
          greet("saraswati")

 ## Return Statement 
 Return send the value back from the function
 example : def add(a,b):
 return a+b
* calling function
 result = add(10, 5)
print(result)

## Default Arguments

Default arguments are used when no value is provided.
example : def greet(name="Guest"):
    print("Hello", name)
* Calling function 
greet("Saraswati")
greet()