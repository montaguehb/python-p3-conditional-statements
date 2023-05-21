#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    return("Access denied", "Access granted")[username.lower() == 'admin' and password == '12345']

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature < 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num

def calculator(operation, num1, num2):
    # your code here
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "/": num1 / num2,
        "*": num1 * num2
    }
    temp = operations.get(operation, None)
    if(not temp):
        print("Invalid operation!")
    return temp 
