# Consider the below code to answer further questions:
    
import numpy as np
list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_)

# Q1. Is there any difference in the data type of variables list_ and array_list? 
#     If there is then write a code to print the data types of both the variables.
# Ans.
print(type(list_))
print(type(array_list))
#     Yes, there is a difference between datatypes of these two variables.
#     list_ is of pyhton list type and array_list is of Numpy Array.

# Q2. Write a code to print the data type of each and every element of both the 
#     variables list_ and array_list.
# Ans.
import pandas as pd
a= [type(i) for i in list_]
print(pd.DataFrame(a,index=list_,columns=["Data_Type"]))
b = [type(i) for i in array_list]
print(pd.DataFrame(b,index=array_list, columns=["Data_Type"]))

# Q3. Considering the following changes in the variable, array_list:
array_list = np.array(object = list_, dtype = int)

#     Will there be any difference in the data type of the elements present in both 
#     the variables, list_ and arra_list? If so then print the data types of each 
#     and every element present in both the variables, list_ and arra_list.
# Ans.
import pandas as pd
a= [type(i) for i in list_]
print(pd.DataFrame(a,index=list_,columns=["Data_Type"]))
b = [type(i) for i in array_list]
print(pd.DataFrame(b,index=array_list,columns=["Data_Type"]))

#     The data types of each element variable list_ is same but for the elements 
#     of variable array_list is changed from Numpy string to Numpy interger.


# Consider the below code to answer further questions:
import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)
#num_array

# Q4. Write a code to find the following characteristics of variable, num_array:
#     (i)	 shape
#     (ii) size
# Ans.
#(i) For shape
np.shape(num_array)
#(ii) For size
np.size(num_array)

# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, 
#     using a numpy array creation function.
#     [Hint: The size of the array will be 9 and the shape will be (3,3).]
# Ans.
# Below is the code to create a numpy array of 3*3 matrix containing zeros only.
import numpy as np
np.zeros(shape=(3,3))
#np.shape(np.zeros(shape=(3,3)))
#np.size(np.zeros(shape=(3,3)))

# Q6. Create an identity matrix of shape (5,5) using numpy functions?
#     [Hint: An identity matrix is a matrix containing 1 diagonally and 
#     other elements will be 0.]
# Ans.
# Below is the code to get the required identity matrix.
import numpy as np
np.eye(N=5)



