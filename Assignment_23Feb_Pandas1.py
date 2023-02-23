# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, 
#     and 42. Then, print the series.
# Ans.
import pandas as pd
l=[4,8,15,16,23,42]
se1 = pd.Series(l)
print(se1)

# Q2. Create a variable of list type containing 10 elements in it, and apply 
#     pandas.Series function on the variable print it.
# Ans.
import pandas as pd
l1 = list(range(10))
l1
se2 = pd.Series(l1)
print(se2)

# Q3. Create a Pandas DataFrame that contains the following data:
#     Table
#     Then print the DataFrame.
# Ans.
import pandas as pd
data1={"Name":["Alice", "Bob", "Claire"], "Age":[25,30,27], "Gender":["Female", "Male", "Female"]}
df1 = pd.DataFrame(data1)
df1

# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? 
#     Explain with an example.
# Ans.
#     A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional 
#     array, or a table with rows and columns.

#     Series can only contain single list with index, whereas dataframe can be 
#     made of more than one series or we can say that a dataframe is a collection 
#     of series that can be used to analyse the data.

import pandas as pd
data1={"Name":["Alice", "Bob", "Claire"], "Age":[25,30,27], "Gender":["Female", "Male", "Female"]}
df1 = pd.DataFrame(data1)
df1
se3 = df1["Name"]
se3
#     Here df1 is a Dataframe which contains collection of series such as se3.

# Q5. What are some common functions you can use to manipulate data in a Pandas 
#     DataFrame? Can you give an example of when you might use one of these functions?
# Ans.
#     There are several common functions available in Pandas that you can use to 
#     manipulate data in a Pandas DataFrame. Some of these functions include:

#     head() and tail() - Used to view the top and bottom rows of the DataFrame, respectively.
df1.head(1)
#     info() - Used to get information about the DataFrame, including the data types, 
#     number of non-null values, and memory usage.
df1.info()
#     describe() - Used to get summary statistics of the DataFrame, including the 
#     count, mean, standard deviation, minimum, and maximum values.
df1.describe()
#     drop() - Used to drop specified rows or columns from the DataFrame.
df1.drop(["Gender"],axis=1)
#     fillna() - Used to fill missing values in the DataFrame with a specified value or method.
df1.fillna(0)
#     groupby() - Used to group the DataFrame by one or more columns and perform 
#     aggregate operations on the groups.
df1.groupby(["Age"]).sum()
#     sort_values() - Used to sort the DataFrame by one or more columns.
df1.sort_values(['Age'], ascending=[True])

# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
# Ans.
#     Series – 1D labeled homogeneous array, sizeimmutable, data values are mutable
#     Data Frames – 2D labeled, size-mutable tabular structure with heterogenic columns,
#     data values are mutable
import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
data.loc[1, 'B'] = 10
print(data)

#     Panel – 3D labeled size mutable array, heterogeneous data, data values are mutable

# Q7. Create a DataFrame using multiple Series. Explain with an example.
# Ans.
import pandas as pd

# create a Series for each column of the DataFrame
names = pd.Series(['Alice', 'Bob', 'Charlie'])
ages = pd.Series([25, 30, 35])
genders = pd.Series(['F', 'M', 'M'])

# create a dictionary of Series
data = {'Name': names, 'Age': ages, 'Gender': genders}

# create a DataFrame using the dictionary of Series
df = pd.DataFrame(data)

# display the DataFrame
print(df)

















