# Python-course-notes

What is Python?
 -- Python is a programming language — a way to give instructions to a computer so it can do tasks for you.
 -- Think of it like this: computers don't understand English, but they understand code. Python is one of the easiest coding languages to learn because it looks very close to plain English

 Why Python?
 -- It is simple and readable — even beginners can understand it
-- It is used in web development, data science, AI, automation, games, and more
-- It is free and works on Windows, Mac, and Linux
-- It has a huge community — millions of people use it, so help is always available

print("Hello, World!") --- Hello, World!

2 What is a Python Interpreter?
-- A Python interpreter is a program that reads your Python code and runs it line by line, one at a time

-- You write code  →  Interpreter reads it  →  Computer executes it  →  You see output

 1. Script mode — You write all your code in a .py file and run it at once. python myfile.py
 2. Interactive mode — You type one line at a time and see the result immediately. You open it by just typing python in your terminal. >>> print("Hello")
Hello

3. What is Linting in Python?
-- Linting is the process of automatically checking your code for errors, bad style, and suspicious patterns — before you even run it.

** Why is Linting important?

--- Catches mistakes early before running the code
--- Keeps your code clean and readable
--- Helps you follow good coding habits
--- Saves time — you find bugs without running the program


3. How pyhton code is executed 
-- Python --> Cpython --> Python Bytecode --> python virtual machine --> Machine code  --> ex: 01011 


4. Python has 5 main built-in data types
-- Integer ( int ) = 10 -- print(age) 
print(type(age)) --- <class 'int'>

-- Float ( float )
A decimal number — any number with a point in it. price = 99.99

-- String ( str )
Text — any characters wrapped in single or double quotes. name = "Ravi"

-- Boolean ( bool )
Only two possible values — True or False. Used for yes/no decisions. is_student = True

-- None ( NoneType )
Represents nothing or no value. Like an empty box. result = None


5. Functions in Python
-- A function is a block of code that does a specific task and can be used again and again whenever you need it

-- How to create a Function
You use the keyword def to define a function. def function_name():
ex: def greet();
print("Hello! Welcome to Python.")
greet() 

-- Types of Functions
Function with no input and no output -- def show_message():
    print("Python is awesome!")
show_message()

-- Function with Parameters ( input )
Parameters are values you pass into the function so it can work with them
def greet(name):
    print("Hello,", name)

greet("Ravi")
greet("Priya")
greet("Amit")

-- Function with Multiple Parameters
def add(a, b):
    result = a + b
    print("Sum is:", result)

add(10, 20)
add(5, 7)

-- Function with Return value ( output )
def add(a, b):
    result = a + b
    return result       # send result back

answer = add(10, 20)    # store the returned value
print(answer)           # 30


6. If, Else, Elif in Python
-- If, else, and elif are used to make decisions in your code. Your program looks at a condition and decides which block of code to run.

1. if statement
Runs a block of code only if the condition is True. if condition:
age = 20

if age >= 18:
    print("You are an adult")


2. if else statement
If the condition is True — do this. Else — do that

if condition:
    # runs if True
else:
    # runs if False

    age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

3. elif statement
elif means "else if" — used when you have more than two options

if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition2 is True
elif condition3:
    # runs if condition3 is True
else:
    # runs if none of the above are True

    marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


7. And, Or, Not — Logical Operators in Python
-- Logical operators are used to combine or modify conditions in your code. They help you make more powerful decisions by checking multiple things at once

-- and -- Both conditions must be True
-- or  -- At least one condition must be True
-- not  -- Reverses True to False and False to True


8. For Loop and While Loop in Python

** FOR LoopA for loop repeats code for each item in a sequence — like a list, a range of numbers, or a string.

for variable in sequence:

ex: for i in range(5):
    print("Hello", i)


**  WHILE Loop
A while loop keeps running as long as a condition is True. When the condition becomes False, it stops.

while condition:


ex: count = 1

while count <= 5:
    print("Count is:", count)
    count = count + 1