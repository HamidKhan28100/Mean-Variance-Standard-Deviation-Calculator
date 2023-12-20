#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
# Defining the function calculate
def calculate(list_of_numbers):
    if len(list_of_numbers) != 9:
        # Raise value error if the list not contain 9 numbers
        raise ValueError('The list must contain nine numbers:')
    # converting the list of numbers to a 3*3 numpy array
    array = np.array(list_of_numbers).reshape(3,3)
    
    ''' Calculating the mean, variance, standard deviation, max, min, sum
     along rows (axis=0), columns (axis=1), and the flattened matrix using numpy
     and converting the results to Python lists for a dictionary '''
    result = {
        'mean': [array.mean(axis=0).tolist(),array.mean(axis=1).tolist(),array.flatten().mean().tolist()],
        'variance': [array.var(axis=0).tolist(),array.var(axis=1).tolist(),array.flatten().var().tolist()],
        'standard deviation': [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.flatten().std().tolist()],
        'max': [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.flatten().max().tolist()],
        'min': [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.flatten().min().tolist()],
        'sum': [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.flatten().sum().tolist()]
    }
    formatted_result = "{\n"
    for key, value in result.items():
        formatted_result += f"  '{key}': {value},\n"
    formatted_result = formatted_result.rstrip(',\n')
    formatted_result += "\n}"
    
    return formatted_result
    


# In[ ]:




