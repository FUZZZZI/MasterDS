# Consider following code to answer further questions:

import pandas as pd
course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration =  [2,3,6,4]
df = pd.DataFrame(data = {'course_name' : course_name, 'duration' : duration})
#df
# Q1. Write a code to print the data present in the second row of the dataframe, df.
# Ans.
df.loc[1]

# Q2. What is the difference between the functions loc and iloc in pandas.DataFrame?
# Ans.
#     loc consider named indexes wheras iloc considers inbuilt indexes.
#     For example:- Here loc considers column name to give the result and 
#                   iloc consideres column index
df.loc[1,"course_name"]
df.iloc[1, 0]

# Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and 
#     store it in the variable, new_df then find the output for both new_df.loc[2] 
#     and new_df.iloc[2].
#     Did you observe any difference in both the outputs? If so then explain it.
df
new_df = df.reindex([3,0,1,2])
new_df
new_df.loc[2]
new_df.iloc[2]
#     Yes, there is a difference, loc returns 2nd indexed row and iloc returns 3rd row from top

# Consider the below code to answer further questions:
import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]

#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
#df1

# Q4. Write a code to find the following statistical measurements for the above
#     dataframe df1:
#     (i) 	mean of each and every column present in the dataframe.
#     (ii) standard deviation of column, ‘column_2’
# Ans.
# (i)
df1.mean()
# (ii)
df1["column_2"].std()

# Q5. Replace the data present in the second row of column, ‘column_2’ by a 
#     string variable then find the mean of column, column_2.
#     If you are getting errors in executing it then explain why.
#     [Hint: To replace the data use df1.loc[] and equate this to string 
#            data of your choice.]
# Ans.
df1.loc[2, "column_2"] = "pwskills"
df1
df1["column_2"].mean()
#     Yes, geeting error because flot ans str data type is given to calculate mean.

# Q6. What do you understand about the windows function in pandas and list 
#     the types of windows functions?
# Ans.
#     The window functions in Pandas are used to perform some sort of calculations 
#     across a set of rows that are interrelated with the current row.
#     Windows function in Pandas can be broadly divided into three categories namely- 
#     1. Aggregate 
#        Group; Rolling, and Expanding
#     2. Ranking 
#        Row numbers (reset_index(),cumcount()); Rank(default_rank, min_rank, 
#                  NA_bottom, descending); Dense Rank; Percent; N-Tile/qcut()
#     3. Value
#        Lag/Lead; First/Last/nth

# Q7. Write a code to print only the current month and year at the time of 
#     answering this question.
#     [Hint: Use pandas.datetime function]
# Ans.
pd.datetime.now().strftime('%B %Y')

# Q8. Write a Python program that takes in two dates as input (in the format 
#     YYYY-MM-DD) and calculates the difference between them in days, hours, and 
#     minutes using Pandas time delta. The program should prompt the user to 
#     enter the dates and display the result.
# Ans.
import pandas as pd
Date1 = input("Insert date1 in 'YYYY-MM-DD' format: ")
Date2 = input("Insert date2 in 'YYYY-MM-DD' format: ")
Date11 = pd.to_datetime(Date1)
Date22 = pd.to_datetime(Date2)
diff= Date22-Date11
days = diff.days
hours = diff.seconds // 3600
minutes = (diff.seconds // 60)%60
print(f"The difference between give dates is {days} days, {hours} hours and {minutes} minutes. ")

# Q9. Write a python program that reads a CSV file containing categorical data 
#     and converts a specified column to a categorical data type. The program 
#     should prompt the user to enter the file path, column name, and category 
#     order, and then display the sorted data.
# Ans.
import pandas as pd
file_path = input("Enter the csv file path: ")
column_name = input("Enter the column name to convert to categorical: ")
category_order = input("Enter the category order (comma-seperated): ").split(",")

#Read the csv file to pandas dataframe
df = pd.read_csv(file_path)
#df

#Convert the specified column to categorical data type
df[column_name] = pd.Categorical(df[column_name],categories=category_order)

#Sort the dataframe by the specified column
df.sort_values(by=[column_name], axis=0, inplace=True)

print(df)

# Q10. Write a Python program that reads a CSV file containing sales data for 
#      different products and visualizes the data using a stacked bar chart to show 
#      the sales of each product category over time. The program should prompt the 
#      user to enter the file path and display the chart.
# Ans.
#      Asuumptions: Here assumption is taken for column names like "sales", "product_category","date".
import pandas as pd
#prompt user to get the csv file path
file_path = input("Enter the csv file path: ")

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Pivot the DataFrame to create a table of sales by product category and date
df_pivot = df.pivot(index='date', columns='product_category', values='sales')

# Create a stacked bar chart of the sales by product category and date
ax = df_pivot.plot(kind='bar', stacked=True)

# Set the title and axis labels of the chart
ax.set_title('Sales by Product Category')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')

# Display the chart
ax.figure.show()           

# Q11. You are given a CSV file containing student data that includes the student
#      ID and their test score. Write a Python program that reads the CSV file, 
#      calculates the mean, median, and mode of the test scores, and displays 
#      the results in a table.

#      The program should do the following:

#      Prompt the user to enter the file path of the CSV file containing the student data.
#      Read the CSV file into a Pandas DataFrame.
#      Calculate the mean, median, and mode of the test scores using Pandas tools.
#      Display the mean, median, and mode in a table.

#      Assume the CSV file contains the following columns:
#      Student ID: The ID of the student.
#      Test Score: The score of the student's test.

#      Assume that the CSV file student_data.csv contains the following data:
# Student ID, Test Score
# 1,85
# 2,90
# 3,80
# 4,75
# 5,85
# 6,82
# 7,78
# 8,85
# 9,90
# 10,85
# Ans.
import pandas as pd

# Prompt the user to enter the file path of the CSV file containing the student data.
#file_path = input("Enter the csv file path: ")
file_path = "C:/Users/Y0VWTS9/Y0VWTS9/Trainings/Python/students.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Calculate the mean, median, and mode of the test scores using Pandas tools.
smean = df["Test Score"].mean()
smedian = df["Test Score"].median()
smode = df["Test Score"].mode()[0]

#Display the mean, median, and mode in a table.
result = pd.DataFrame({"Statistics":["Mean", "Median", "Mode"], "Value":[smean, smedian, smode]})
print(result)
