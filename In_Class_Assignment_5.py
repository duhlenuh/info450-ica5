#!/usr/bin/env python
# coding: utf-8

# In Class Assignment #5: File IO, Recursion
# Submit this assignment completed, in its own repository, as a GITHUB LINK. Cite your sources as always



# # # PART 1. 
# Read in "numbers.txt" using the "open file" method we learned in class. Save the contents in a list variable called "L"

# In[1]:
filename = "numbers.txt"

# In[2]:
L = []

# In[3]:
with open(filename) as file_object:
    for line in file_object:
        L.append(line)

# In[4]:
L
# # RESULT: ['10, 32, 70, 42, 34, 35, 46, 88, 10, 10, 22, 97, 22, 37, 75, 99, 46, 63, 8, 51, 8, 7, 4, 66, 24, 94, 76, 48, 14, 58']



# # # PART 2. 
# Write a Python function called "sum_recursive()" that takes a positive integer "n" as an input and 
# uses recursion to calculate the *sum of all integers* from 1 to "n". Your function should return the sum.

# For example, if n is 5, your function should calculate and return the sum 1 + 2 + 3 + 4 + 5 = 15.

# You can assume that the input n will always be a positive integer.
# You should not use any built-in functions or methods that directly solve this problem (e.g. sum() or range()), 
# and you should use recursion to solve the problem.

# In[5]:
def sum_recursive(n):
    # check if n = 1 (positive integer)
    if n == 1:
        return n
    # use recursion to calculate sum of all integers from 1 to n
    else:
        # return sum
        return n + sum_recursive(n-1)

# In[6]:
# ex: if n = 5, function should calculate and return the sum 1 + 2 + 3 + 4 + 5 = 15
result = sum_recursive(5)
print(result)
# # RESULT: 15

# In[7]:
result = sum_recursive(1)
print(result)
# # RESULT: 1



# # # PART 3.
# Write a Python function called "looping()" that takes a list of integers, runs each integer through "sum_recursive()", and returns the list of recursively summed integers.
# ie. if your list is [2, 5, 3], your function output should be [3, 15, 6]

# In[8]:
def looping(integer_list):
    # initialize empty list
    result_list = []
    # run each integer in list through "sum_recursive()" function
    for n in integer_list:
        # append result of recursive sum to int_list
        result_list.append(sum_recursive(n))
    # return list of recursively summed integers
    return result_list

# In[9]:
result = looping([2, 5, 3])
print(result)
# # RESULT: [3, 15, 6]



# # # PART 4. 
# You probably saw this coming by now..
# Please run the contents of the "numbers.txt" file (you completed in PART 1) through your "looping()" function

# SOURCE: geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/

# In[10]:
with open(filename) as file_object:
    # reads contents of file as a whole
    lines = file_object.read()
    # converts contents to integer and splits by comma using split() method
    num = [int(line) for line in lines.split(",")]
    # pass num through looping() function
    result = looping(num)
    # store in result and print result
    print(result)
# # RESULT: [55, 528, 2485, 903, 595, 630, 1081, 3916, 55, 55, 253, 4753, 253, 703, 2850, 4950, 1081, 2016, 36, 1326, 36, 28, 10, 2211, 300, 4465, 2926, 1176, 105, 1711]
