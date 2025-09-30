#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3. Write a python program that, given an input list, will filter the input above a user defined threshold. This is to be done with a standard function.
#That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]


def filter_by_threshold(input_list, threshold):
    three_a = []
    for number in input_list:
        if number <= threshold:
            three_a.append(number)
    return three_a

input_list = [1,2,3,4,5,6,7,8,9]
threshold = 6
result = filter_by_threshold(input_list, threshold)
print(result)




# In[ ]:




