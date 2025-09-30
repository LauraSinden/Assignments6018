#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2. Write the a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. This is to be done with recursion. Note: the input will contain only integers or lists.
#recursive_inner_plus.py

def find_and_increment_innermost(input_list):
    def recursive_helper(sublist):
        innermost_found = True
        for item in sublist:
            if isinstance(item,list):
                innermost_found = False
                result = recursive_helper(item)
                if result is not None:
                    return result
        if innermost_found:
            return[element + 1 for element in sublist]
        return None

    return recursive_helper(input_list)

input_list = [1,2,3,4,[5,6,7,[8,9]]]
result = find_and_increment_innermost(input_list)
print(result)




# In[ ]:




