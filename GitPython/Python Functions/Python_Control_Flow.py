
print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#A1a
print(x[:5])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
for i in x:
    if i %2 ==0:
        print(i)
# A1b:



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
y= x[:5]
# A1c:
for i in y:
    if i %2 ==0:
        print(i)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
Initials = [[name[0].upper(),name.split(" ")[1][0].upper() if " " in name else "" ] for name in names]
# A2a:
print(Initials)



print("\nQ2b\n")
# Q2b: from the list of names, create another list thehat consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
# Given list of names

space_indices = []
# list for space index
for name in names:
    indices = []
    for i in range(len(name)):
        if name[i] == " ":
            indices.append(i)
    space_indices.append(indices)

print(space_indices)


# A2b:



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
Proper_Initials = [[name[0].upper() + '.'+ name.split(" ")[1][0].upper() if " " in name else "" ] for name in names]
# A2c:
print(Proper_Initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

for sublist in list_of_lists:
    if len(sublist) == len(set(sublist)):
        print(sublist)
# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered
val_input = int(input('Enter a number greater than 100: '))
print(f"You entered:{val_input}!")
# A4a:
while val_input < 100:
    print(f"{val_input} is not valid. Enter a number greater than 100")
    val_input = int(input('Enter a number greater than 100: '))

print(f"{val_input} is valid")


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise
prime = True

for x in range(2,val_input //2 +1):
    if val_input % x == 0:
        prime = False
        print(f"{val_input} is not a prime number")
        break
if prime:
    print(f"{val_input} is a prime number")

# A4b:
