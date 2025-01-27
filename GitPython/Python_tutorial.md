# Python for beginners
Python is a high level language, and as of September 2024, the 3rd most popular computing language sitting behind JavaScript (JS) and 
HTML/CSS. The latter being open source meaning Python is actually the second most popular. This
leads conveniently into the primary benefits of leaning Python:
- Open source with a large community and an ever growing supporting libraries  
- Multiplatform
- Built on C 
- Often the Language of choice for Data Scientists and AI (not the buzzword, the full implementation including NLP, LLM's and Deep Learning)
---
## Installing Python
Firstly, install the Python software, this is the console that our code will run on. Use [this](https://www.python.org/) link and follow the instructions 
based on you OS version. It is recommended especially for beginners that [PyCharm](https://www.jetbrains.com/pycharm/) is the Integrated Development Environment of choice.
There is a free version (Community Edition) which will be more than enough to utilise the important features of Python.
Another editor choice could be [VSCode](https://code.visualstudio.com/) but it is recommended to use Pycharm. As usual, follow the instructions and specify the location
you want the IDE to installed at.
---
## Your first project
Select New Project and feel free to change the name. You will now be greeted with a sample project syntax
and a project tabe to your left. This project tab displact all current files read by PyCharm. Typically called 
version environment or "venv". To create our first project, right click on the `venv` region of you IDE and select new
Python file. Give it the name "HELLO_WORLD". Now we can input our code and be on our way to become an amazing or at least
seviceable developer.
<br>
Using an IDE like PyCharm is extremely effective for training and error checking due to a feature
coined `ReSharper`. You will see this a lot in other IDE's because of the extensive code navigation benefits on top of the 
previously mentioned benefits of editors made by JetBrains. The downside is the resource requirement but if your system 
can handle the resource tax, it can be worth purhasing <br>
---
## Hello World! 
```python
print("Hello World!")
```
As you are typing the syntax you will notice Pycharm makintg suggestions for you. Seeing your syntax as an option of the 
drop down list is a good sanity check of working code.<br>
Use the shortcut `Ctrl`+`Shift`+ `F10` to run your code. You can also right click the file and select `Run`.
You will now be greeted with a console log appearing at the bottom of your screen by default. It will print the 
text "Hello World", and it will also state "Process finished with exit code 0". This means there were no errors.
It is a good start. And welcome to the developer world!!! <br>
---
### Commenting on code 

While writing code it is extremely important to comment on your code within the IDE. There are two main reasons: <br>
- Readablity. Others need to be able to read and interpret what your code it trying to accomplish. If you have no comments,
problems with group projects and handovers are sure to follow
- Reflection. For you, it is also important because ideas can slip away very easily and yo ucan lose your train of thought.
You can also return to a program you developed after some time and without any commments it will be very difficult to improve or revise
the code.
# So please, save your's and your colleague's time by commenting your code. We thank you in advance
## So how do we comment?
There are two main ways:
```python
# Single line comment whatever is included in this line after the hash is greyed out

"""
This is a multi line comment. Very useful when diagnosing problems too
"""
```
---
## Data types, operators and loops

This is not an exhaustive list. This it a reference to get familiar with for beginner to intermediate Python programming.
The second aim is to condense any descriptions into categories alongside types for quick reference t ospeed up learning.

| **Category**   | **Type/Concept** | **Description**                                      | **Example Syntax**                                  |
|----------------|----------------|------------------------------------------------------|-----------------------------------------------------|
| **Data Types** | **int**        | Integer type, whole numbers                          | `x = 10`                                            |
|                | **float**      | Floating-point numbers, decimals                     | `x = 3.14`                                          |
|                | **complex**    | Complex numbers with real and imaginary parts        | `x = 2 + 3j`                                        |
|                | **str**        | String, a sequence of characters                     | `x = "Hello"` or `x = 'Hello'`                      |
|                | **bool**       | Boolean type, logical values `True` or `False`       | `x = True` or `x = False`                           |
|                | **list**       | Ordered, mutable collection of elements              | `x = [1, 2, 3]`                                     |
|                | **tuple**      | Ordered, immutable collection of elements            | `x = (1, 2, 3)`                                     |
|                | **dict**       | Key-value pairs, unordered and mutable               | `x = {"key": "value"}`                              |
|                | **NoneType**   | Represents the absence of value                      | `x = None`                                          |
|                | **range**      | Immutable sequence of numbers, often used in loops   | `x = range(0, 10)`                                  |
| **Loops**      | **for loop**   | Iterates over a sequence (list, string, range, etc.) | `for i in range(5): print(i)`                       |
|                | **while loop** | Repeats as long as a condition is `True`             | `while x < 5: print(x); x += 1`                     |
|                | **nested loop** | Loop inside another loop                             | `for i in range(3): for j in range(2): print(i, j)` |
|                | **break**      | Exits the current loop                               | `for i in range(5): if i == 3: break`               |
|                | **continue**   | Skips to the next iteration of the loop.             | `for i in range(5): if i == 3: continue`            |
|                | **else with loops** | Executes if the loop completes without `break`.      | `for i in range(5): ... else: print("Done")`        |
|                | **+**          | Add                                                  | `4+4` will store `8`                                |
| **Operators**  | **-**          | Subtract                                             | `4-4` will store `0`                                |
|                | **/**          | Divide                                               | `4/4` will store `1`                                |
|                |   **%**       |   Modulo- Divide by a number and find the remainder   | `10 % 4` will store `2`                             |
|                |    *      |   Multiply   | `4*4` will store `16`                               |

---
## Important notes (Control flow)
When dealing with data, the concept of **control flow** becomes very important. With this in mind, we will tackle functions and varaibles at the same time.
### What is control flow?
Control flow is aboout decisions with data using automated processes to solve problems. A primitive case of this is the example 
will involve conditional statements. Here is an example: <br>
```python
time_of_day = 1
if time_of_day>5 and time_of_day<12:
    print('Good Morning')
elif time_of_day >12 and time_of_day<18:
    print('Good Afternoon')
else:
    print ('Good Evening')
```
With different values of `time_of_day` we get different outputs. Notice that `time_of_day` can also be representative of a 
variable when using numerical functions

---
We have arrived at functions, one of the most important features of Python. This will require a lot of practice but the premise is simple.
You define a set of intructions that you will call frequently or at least enough times that self containing it in a sub program will improve effeciency.
This knowledge path will lead to `abstraction` which is a core concept of Object Oriented Programming.

### How it works
First step is to define the function and give it a name <br>
```python
def python_test(first_name, last_name):
```
Now this in itself will not work but it is the first line that details what will be used. We will take two 
arguments into this function and something will happen. Next we can detail what we want this function to do.
In this case we will concatenate these two strings to return the full name of someone who has just entered their details.
```python
def python_test(first_name, last_name):
    return first_name + ' ' + last_name
```
When we call this function, we have to pass the arguments into the function to generate an output. <br>
Please go through the documentation [here](https://docs.python.org/3/library/functions.html) regarding python functions.
It will be expedient to your development.