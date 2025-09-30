#!/usr/bin/env python
# coding: utf-8

# In[1]:


#your_py_program.py input_list
#1 Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with a while loop. Note: the input will contain only integers or lists. 


def find_and_increment_innermost(input_list):
    lists_to_process = [input_list]
    innermost_list = None
    while lists_to_process:
        current_list = lists_to_process.pop(0)
        has_sublist = False

        for item in current_list:
            if isinstance(item,list):
                lists_to_process.append(item)
                has_sublist = True
        if not has_sublist:
            innermost_list = current_list
    if innermost_list is not None:
        result = [item + 1 for item in innermost_list]
        return result
    return[]
input_list = [1,2,3,4,[5,6,7,[8,9]]]
result = find_and_increment_innermost(input_list)
print(result)



# In[ ]:




