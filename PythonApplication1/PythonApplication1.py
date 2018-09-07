#Basic Python Personal Tutorial based on Intro Session Slides



    # 1. Built-In Functions


print('Hello World')
# get the name of the user
name= input('what is your name?')# In python no need semicolons, line end indicates that, and also indentations indicates curly brackets for functions
# input function returns what ever the user types as input and takes an option parameter of message to the user

#print a greeting to the command line
print ('hello', name)

#isinstance (object,type) checks if object is of type (explanation of parameters) and returns a bool (true or false)
#check if name is a string
# Two ways to print this 
print (isinstance(name,str))
#is_name_str = isinstance(name, str)
#print('isinstance on name returned %s' % (is_name_str))

#len(object) to check the length of an object, String takes one byte of space per character
# get the length of your name
# Two ways to print this, 2nd way by creating a variable for length where no need to specify type (AUTO CHECK FEATURE WHEN COMPILING-PYTHON)
print ('Length of the name string is',len(name))
# name_length = len(name)
# print('name is {} characters long'.format(name_length))


import os

# the path to the file we are currently using
file_path = os.path.realpath(__file__)

# __file__ is the name of the file we are using
print('the current file is', __file__)

print('the path for the current file is', file_path)


    #2. Built-In Data Types
# Data types overview:
# (A)numeric types: integers, float and complex
# (B)sequences types: strings, list, tuple, range
# (C)collection types: dicitionary, set

        #(A) Numeric- means mutable
sum = 4 + 5 + 6

integer_average = sum // 3
float_average = sum / 3

print(integer_average, float_average)

if isinstance(integer_average, int):
    print("integer_average is an int")

if isinstance(float_average, float):
    print("float_average is a float")

# make a complex number
imaginary = 2 + 3j

print(imaginary)

print(isinstance(imaginary, complex))

# square a number
square = 7 ** 2

print(square)

print(isinstance(square, int))

        #(B) str type- Immutable, constructor '' or ""
#str can contain zero characters, known as an empty string

#str_name.replace(old,new,count)
#returns new string with occurences of old in the string replaced with new count number of times (a limitation)

#str_name.split(sep=None,maxsplit=-1)
#returns a list of strings on the string "sep"
# you can limit number of splits

name= 'john smith'
first,last= name.split(' ',1)# splitting first and last name
print(name)
print(first)
print(last)
#change john's last name
name=name.replace(last,'hamilton')
print(name)


        #(C)Sequence Types
#((I))List- stores zero or more objects (mutable)
#((II))Tuple-stores zero or more objects (immutable)
#((III))range-sequence of numbers (immutable)


            #((I))List type class methods- mutable and constructor: list() or []
#a_list.append(object)// adds "object" to end of a_list
#a_list.clear(), a_list.remove(object)// removes first occurence of "object" from a_list
#a_list.sort()// for lists where all objects have same type


a_l = [2, 3, 4, 1]
print(a_l)

a_l.append('a')
print(a_l)
a_l.remove('a')
print(a_l)

a_l.sort()
print(a_l)

a_l.clear()
print(a_l)

            #((II)) Tuple type, constructor tuple() or ()

## All possible examples of what a tuple can store
a_tuple = ()
print(a_tuple)

b_list = [2, 3]
b_tuple = tuple(b_list)# Takes the elements in b_list and puts as elements in a empty tuple
print(b_tuple)

c_tuple = (1, 'a', a_tuple, b_list)# a_tuple an empty tuple and b_list a list with 2 elements are shown as subsets (as their originals)- see below for output
print(c_tuple)# (1, a, (), [2,3])

d_tuple = ([], (), str(), int())# displays the empty equivalents for each data type object on the tuple- see below for output
print(d_tuple)# ([],(),"",0)- (empty list, empty tuple, empty string, zero/empty int)

            #((III))- Range type, constructor: range(), format (Max, Min(excluding), Diff) provides a range, list of numbers within these constructor specified boundaries

a_range = range(12, -30, -4)

# can be used to make other sequences
a_list = list(a_range)
print('a_list has ', a_list)
print('a_range is ', tuple(a_range))

b_range = range(0, 11, 2)
print('b_range is ', tuple(b_range))

# mostly used for iteration
for number in b_range:
    print(number)



    #3. Collection Types (mutable)
#(A) set: used to store a collection of unordered items
#(B) dict-ionary: a collection of keys where each key maps to a specific value

        #(A) set, constructor: set() or {}
# A collection of unique(*), immutable objects (refering to themselves)
# Useful for removing duplicates from a sequence**
# sets don't record an objects position


a_list = [1, 2, 3, 2, 4]
b_tuple = (5, 1, 2, 3, 2, 4, 3, 5)
c_str = 'abbcddde'

a_set = set(a_list)
b_set = set(b_tuple)
c_set = set(c_str)
d_set = {b_tuple, c_str}# will not change the objects within (this case the objects are b_tuple and c_str) will only delete either of the objects if one is the duplicate of the other

print(a_set)
print(b_set)
print(c_set)
print(d_set)#check output for proof

        #(B)dict, constructor: dict() or {}
# A mapping of an immutable object to a mutable object
# Very useful for doing fast lookups

# key in my_dict// my dict takes "key" as a variable, returns true or false
#a= my_dict[key]// returns the object mapped to by "key" in my_dict
#my_dict[key]= object// maps key in my_dict to object

name_to_age = {
    'john': 23,
    'alice': 21.5,
    'hank': 'N/A'
}

print("john's age is ", name_to_age['john'])
print('alisson' in name_to_age)
print('alisson' not in name_to_age)
print(name_to_age)
name_to_age['hank'] = 25
print(name_to_age)


    #4. Built in Constants
    #None (absence), True and False
    # Bool types, true and false
    #bool (any value and type), each has representative true or false states which are then returned as bool type: True or false depending on input
    #Boolean logic
    #All values equate to true execpt constants like 0,0.0,0.0f None and False that represent false. Also empty "",'', (), [], set(), range(0) are also false. Anything else=True
    
#Understand each ove the example below
bool_a = True
bool_b = False
bool_c = bool(True)# True
bool_d = bool(False)# False
bool_e = bool(1)#True
bool_f = bool(0)#False
bool_g = bool(-4.5)#True

print(isinstance(bool_a, bool))# isinstance checks if bool_a is of bool type, which it is so isinstance returns True
print(bool_a and bool_b)# (bool_a-value and bool_b-value)-> (True and False)-> equals False, so returns False
print(bool_a or bool_b)# True
print(bool_a and bool_c)# True
print(not bool_a)#False

    #5. Control Structures
#if, while and for (for takes a sequence as an argument, others bool values)
# coding in python, either use four spaces or one tab, the style recommends four spaces


counter = 1

while counter <= 10:
    print(counter)

    if counter == 5:
        print('we are halfway there')

    # counter += 1 equivalent to counter = counter + 1
    counter += 1



a_range = range(1, 10, 1)

# this for loop will execute 10 times
# since there are 10 numbers in a_range

for number in a_range:
    print(number)

    if number == 7:
        print(number, ' this is the last prime below 10')


    #6.Functions

    # Here is an example, definition with body first then calling the function from outside
    # Do not need to specific parameters' data type
def function_name(arg_1, arg_2):
    print(arg_1)
    print(arg_2)

    return_value = arg_1 + arg_2

    return return_value


result = function_name('abc', 'def')
print(result)


    #7. Examples
    # Sample Application: Designing a program to remove all of the empty folders from a directory
    #Loop through all folders in the directory checking if each folder is empty or not, if a folder is empty remove it, if not empty keep it
    #os.path.isdir(path)- checks if the path is a directory or not, if true return true else return false
    #os.rmdir(path)- removes directory at path if it is empty
    #os.listdir(path)- returns names of path's immediate children
    #os.path.join(path,child)-returns a string in the format "path\child"

    # so here is sample function that takes a directory as input and returns nothing
import os
   
def RemoveEmpties(target_dictionary):
        range_directories=os.listdir(target_dictionary)

        for directories in range_directories:
            smaller_path=os.path.join(target_dictionary,directories)
            if not os.path.isdir(smaller_path):
               continue
            if not os.listdir(smaller_path):
                os.rmdir(smaller_path)      
         
target_dicitonary1= input('Please enter the desired directory?\n')

if not os.path.isdir(target_dictionary1):
        print('the directory you entered is invalid')
        exit()
    
RemoveEmpties(target_dictionary1)


            

    #Here is Version 1 of a solution
    #Here is Version 2- using a function just like above
    #Here is Version3- using a new built in function os.walk(path,topdown) or bottomdown generating file names in a directory

    #os.walk(path,topdown)
    #generate the file names in a directory and its subdirectories topdown or bottom up.
    
    #yields a tuple of (dirpath, dirnames, filenames)
    #dirpath: the path to the directory
    #dirnames: the names of the sub-directories in dirpath
    #filenames: the name of the files in dirpath

    # using this funciton we can redefine the RemoveEmpties function like this

    #def remove_empties(target_directory):
    #"""Remove all empty directories from a directory.

    #Keyword arguments:
    #target_directory -- the directory containing the empty directories
    #"""
    #for root, dirs, files in os.walk(target_directory, topdown=False):
    #    for directory in dirs:
    #        directory_path = os.path.join(root, directory)

    #        if not os.listdir(directory_path):
    #            os.rmdir(directory_path)
    #            print(directory_path)

