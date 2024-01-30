# Day 12 of 100DaysofCode

Feeling excited to start Day 12 of 100 DaysOfCode, as I started pretty Late to code. So today I have a lot of pending tasks. As well as have to document
all of that learning like this. Today I learnt about Scope and Build a project related to that called Number Guessing Game. 

I learnt through Angela Yuin Course from Udemy. 100DaysOfPython. 
Now I will start documenting like this Each and every day. 
Today, Session includes Fundamentals of Scope and there importance in Python language. as well as also applied this in real world project. 



## Table of Contents

1. [Usage](#usage)
2. [Local Variable](#Local_Scope)
3. [Global Scope](#Global_Scope)
4. [Interaction](#Interaction)
5. [global_Keyword](#global_Keyword)
6. [Contributing](#Contributing)



## Usage

Clone this repository or simply refer to the README for a quick reference on using the basic Linux commands. Feel free to customize the commands based on your needs.

```bash
git clone https://github.com/aashess/100-Days-Of-Code.git
cd day-12
python3 scope.py
```



In Python, variable scopes determine the accessibility and visibility of variables within different parts of a program. The two main types of scopes are local and global.

## Local_Scope: 

   - **Definition:** Variables defined within a function or a block of code have local scope.
   - **Visibility:** Limited to the block or function where they are defined.
   - **Lifetime:** Created when the function is called or the block is entered, and destroyed when the function exits or the block is exited.
   - **Example:**
     ```python
     def my_function():
         local_variable = 10
         print(local_variable)
     
     my_function()
     # print(local_variable)  # This line would raise an error
     ```

## Global_Scope
   - **Definition:** Variables defined outside any function or block have global scope.
   - **Visibility:** Accessible throughout the entire program.
   - **Lifetime:** Created when the program starts and exists until the program terminates.
   - **Example:**
     ```python
     global_variable = 20
     
     def my_function():
         print(global_variable)
     
     my_function()
     print(global_variable)
     ```

## Interaction
   - Local and global scopes can coexist in a program. However, a local variable with the same name as a global variable will overshadow the global variable within its scope.
   - **Example:**
     ```python
     x = 5  # Global variable
     
     def my_function():
         x = 10  # Local variable with the same name
         print(x)  # Prints the local variable
     
     my_function()
     print(x)  # Prints the global variable
     ```

## global_Keyword
   - The `global` keyword is used to indicate that a variable declared within a function has global scope.
   - **Example:**
     ```python
     def my_function():
         global global_variable
         global_variable = 30
     
     my_function()
     print(global_variable)  # Prints 30
     ```

Understanding local and global scopes is crucial for writing maintainable and modular code. Properly managing variable scopes ensures that variables are used where they are intended and minimizes unintended side effects.

## Local Variable & Global Variable 

    Here you can't change global variable with local variable. You have to define local variable somewhere above line "enimies+=1" so that you can able to increase by 1. 
``
enimies = 2

def func1():
    global enimies
    enimies+=1
    print(enimies)
    
func1()
``


-----------------------------------------------------------
NOTE: Always define global scope with Capital Letter For ex- 
TWITTER_HANDLE = www.twitter.com
 So that when it appear in autocomplete list you can understand that you don't need to modify this variable. 



 ## Contributing

If you would like to contribute to this repository, please open a pull request. Feel free to suggest new commands or improvements to existing ones.
