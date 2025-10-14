#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
#%% the humble print statement
'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.

   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.

   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]

   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

wrong_add_function(arg_str_1,arg_str_2)


# In[10]:


#1.a
#Using the print() function only, get the wrong_add_function to print out where
#it is making a mistake, given the expected output for ex, "we are making an error 
#in the loop", which you would put near the loop. 
#Structure the print() statement to show what the expected output ought to be
#ia f-strings: ie "The correct answer is#supposed to be: [...]".9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

def wrong_add_function(numbers):
    print(f"DEBUG: Starting `wrong_add_function` with input: {numbers=}")
    for i in range(len(numbers)):
        total = 0
        total += numbers[i]
        print(f"DEBUG: Starting `wrong_add_function` with input: {numbers=}")
        return (total)

one_a = [5,10,15]
result = wrong_add_function(one_a)
expected_sum = sum(one_a)
print("\n--- Identifying the error ---")
print(f"The incorrect result is: {result}")
print(f"The correct answer is supposed to be: {expected_sum}")
print("we are making an error in the loop because 'total' is reset to 0 every time.")
#1.b
#Then, changing as little as possible, modify the function, using the same 
#general structure to output the correct answer. Call this new function 
#correct_add_function() 
def correct_add_function(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

one_b = [5,10,15]
result = correct_add_function(one_b)
expected_sum = sum(one_b)
print(f"The correct result is: {result}")



# In[ ]:


#2.a NO idea what Im supposed to do here
#Update the numeric section of the function with your changes from 1 for both 
#2.b and 2.c


# In[9]:


#2b
def string_section(input_1, input_2):
    output = []
    for element_1, element_2 in zip(input_1, input_2):
        if isinstance(element_1, str) and isinstance(element_2, str):
            output.append(element_1 + element_2)

    try:
        # Check for type errors in input_1
        for n, item in enumerate(input_1):
            if not isinstance(item, str):
                raise TypeError(f"Your input argument [1] at element [{n}] is not of the expected type. Please change this and rerun.")

        # Check for type errors in input_2
        for n, item in enumerate(input_2):
            if not isinstance(item, str):
                raise TypeError(f"Your input argument [2] at element [{n}] is not of the expected type. Please change this and rerun.")

        # If no TypeError is raised, call the original function
        return string_section(input_1, input_2)

    except TypeError as e:
        return str(e)




invalid_input_1 = ["5", "2", 5]
invalid_input_2 = ["3", "1", "0"]
result_invalid = exception_add_function(invalid_input_1, invalid_input_2)
print(f"Result with invalid input: {result_invalid}")






# In[2]:


#2c-#Without modifying the string section code itself or the input directly, 
#write a try, except block that catches the issue with the input below and 
#gets it to process via the string section. IE, do not, outside the function,
#change the values of arg_str_1 or arg_str_2. Name this function 
##correction_add_function(), i.e you will not be updating the wrong_add_function,
#you will simply handle the error of wrong inputs in a seperate function, you want
#the wrong_add_function to output its current result you are only bolstering the 
#function for edge cases .
def wrong_add_function(arg1, arg2):
    # integer section
    if all(isinstance(i, int) for i in arg1) and \
       all(isinstance(i, int) for i in arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = sum(arg1[arg1_index] + i for i in arg2)
            arg1[arg1_index] = arg_2_sum  
            arg1_index += 1
        return arg1
    # string section
    elif all(isinstance(i, str) for i in arg1) and \
         all(isinstance(i, str) for i in arg2):
        arg1_index = 0
        while arg1_index < len(arg1):
            arg_2_sum = ''.join(arg2)
            arg1[arg1_index] = arg1[arg1_index] + arg_2_sum
            arg1_index += 1
        return arg1
    else:

        raise TypeError("Inputs are not consistently integer or string lists.")

def correction_add_function(input_1, input_2):
    try:

        return wrong_add_function(input_1, input_2)
    except TypeError:

        corrected_input_1 = [str(item) for item in input_1]
        corrected_input_2 = [str(item) for item in input_2]


        return wrong_add_function(corrected_input_1, corrected_input_2)

# Original input with mixed types
arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]


result = correction_add_function(arg_str_1, arg_str_2)
print(result)


# In[ ]:




